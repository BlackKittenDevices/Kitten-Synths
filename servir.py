# Kitten Synths: serves this folder on http://localhost:8766 and opens the installer (site/webapp/installer/).
# Needs Python 3 and Chrome or Edge. Plug the FM-1 in, press install in the page.
# The simulator (no FM-1 needed): http://localhost:8766/simulator/index.html?mock=1
import http.server, socketserver, webbrowser, os
os.chdir(os.path.dirname(os.path.abspath(__file__)))
H = http.server.SimpleHTTPRequestHandler
H.extensions_map.update({".wasm": "application/wasm", ".js": "text/javascript", ".fwsc": "application/octet-stream"})
socketserver.TCPServer.allow_reuse_address = True
with socketserver.TCPServer(("127.0.0.1", 8766), H) as s:
    webbrowser.open("http://localhost:8766/site/webapp/installer/")
    print("Installer: http://localhost:8766/site/webapp/installer/   Simulator: http://localhost:8766/simulator/index.html?mock=1   (Ctrl+C to stop)")
    s.serve_forever()
