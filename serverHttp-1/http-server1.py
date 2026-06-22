#coding:utf-8

import http.server
# import socketserver

PORT=80
ADDRESS=("",PORT)

server=http.server.HTTPServer

handler= http.server.CGIHTTPRequestHandler
handler.cgi_directories=['/']

httpd= server(ADDRESS, handler)
print(f"serveur demarre sur le port {PORT}")

httpd.serve_forever()