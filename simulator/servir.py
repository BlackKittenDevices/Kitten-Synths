# Serves this folder at http://localhost:8000 and opens the SLOOP demo (mock mode, no FM-1).
import http.server, socketserver, webbrowser, os
os.chdir(os.path.dirname(os.path.abspath(__file__)))
http.server.SimpleHTTPRequestHandler.extensions_map.update({".wasm": "application/wasm", ".js": "text/javascript"})
socketserver.TCPServer.allow_reuse_address = True
with socketserver.TCPServer(("127.0.0.1", 8000), http.server.SimpleHTTPRequestHandler) as s:
    webbrowser.open("http://localhost:8000/index.html?mock=1")
    print("Demo at http://localhost:8000/index.html?mock=1  (Ctrl+C to stop)")
    s.serve_forever()
