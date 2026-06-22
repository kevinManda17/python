import http.server 
import socketserver

port = 80 
address= ('', port)

handler = http.server.SimpleHTTPRequestHandler
http = socketserver.TCPServer(address , handler)

print(f'Le serveur demarre sur le port {port}')

http.serve_forever()

