#coding;utf-8

import http.server
import socketserver

PORT=80
ADDRESS=("",PORT)

handler= http.server.SimpleHTTPRequestHandler
httpd = socketserver.TCPServer(ADDRESS, handler)

print(f"serveur demarre sur le port {PORT}")

httpd.serve_forever()