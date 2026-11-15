"""Flash lab: builds the firmware as is, then with one variant of the build, and reports the sizes as annotations.
   usage: flashlab.py VARIANT   (run inside the SLOOP tree, after the toolchain and the SDK are in place)"""
import os, re, subprocess, sys

V = sys.argv[1]
HOME = os.path.expanduser("~")
OBJDUMP = f"{HOME}/.jieli/toolchain/common/bin/objdump"


def build():
    subprocess.run("bash ./build.sh --release 2.8-kitten > /tmp/lab-build.log 2>&1", shell=True, check=False)
    ok = os.path.exists("build/felucca.bin")
    return ok


def size():
    return os.path.getsize("build/felucca.bin")


def syms():
    out = subprocess.run([OBJDUMP, "-t", "build/felucca.elf"], capture_output=True, text=True).stdout
    d = {}
    for ln in out.splitlines():
        t = ln.split()
        if len(t) < 5:
            continue
        sec = next((x for x in t if x.startswith(".")), None)
        if not sec:
            continue
        try:
            i = t.index(sec)
            sz = int(t[i + 1], 16)
        except (ValueError, IndexError):
            continue
        d[t[-1]] = (sz, sec)
    return d


def note(title, msg):
    print(f"::notice title={title}::{msg[:1400]}")


def patch(path, old, new, count=1):
    s = open(path).read()
    assert old in s, (path, old)
    open(path, "w").write(s.replace(old, new, count))


if not build():
    print("::error title=LAB::the base build failed: " + open("/tmp/lab-build.log").read()[-600:].replace("\n", "|"))
    sys.exit(1)
base = size()
bs = syms()
note("LAB-BASE", f"{V}: base image {base} B")
top = sorted(bs.items(), key=lambda kv: -kv[1][0])[:40]
note("LAB-TOP1", ";".join(f"{n} {s}" for n, (s, _) in top[:20]))
note("LAB-TOP2", ";".join(f"{n} {s}" for n, (s, _) in top[20:40]))
sec = {}
for n, (s, sc) in bs.items():
    k = re.sub(r"^(\.[a-z_]+)\..*", r"\1", sc)
    sec[k] = sec.get(k, 0) + s
note("LAB-SECTIONS", ";".join(f"{k} {v}" for k, v in sorted(sec.items(), key=lambda kv: -kv[1])))

if V == "base":
    sys.exit(0)

B = "tools/build.py"
if V in ("oz", "oz-gc-data"):
    patch(B, '"-Os", "-ffunction-sections"', '"-Oz", "-ffunction-sections"')
if V in ("gc", "gc-data", "oz-gc-data"):
    patch(B, 'tc("pi32v2/bin/ld", "-T", FW / "app.ld"', 'tc("pi32v2/bin/ld", "--gc-sections", "-e", "_start", "-T", FW / "app.ld"')
if V in ("data", "gc-data", "oz-gc-data"):
    patch(B, '"-ffunction-sections", "-fno-builtin"', '"-ffunction-sections", "-fdata-sections", "-fno-builtin"')
if V == "merge":
    patch(B, '"-ffunction-sections", "-fno-builtin"', '"-ffunction-sections", "-fno-builtin", "-fmerge-all-constants"')
if V == "nounwind":
    patch(B, '"-ffunction-sections", "-fno-builtin"', '"-ffunction-sections", "-fno-builtin", "-fno-unwind-tables", "-fno-asynchronous-unwind-tables"')
os.remove("build/felucca.bin")
if not build():
    print("::error title=LAB::variant build failed: " + open("/tmp/lab-build.log").read()[-800:].replace("\n", "|"))
    sys.exit(1)
n = size()
ns = syms()
gone = [k for k in bs if k not in ns and bs[k][0] > 0]
note("LAB-RESULT", f"{V}: {n} B, {n - base:+d} B against the base; symbols gone {len(gone)}")
note("LAB-GONE", ";".join(f"{k} {bs[k][0]}" for k in sorted(gone, key=lambda k: -bs[k][0])[:60]))
