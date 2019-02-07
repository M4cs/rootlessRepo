import http.server
import socketserver
import os
import threading


def runServer():
    PORT = 8081
    web_dir = os.getcwd()
    os.chdir(web_dir)

    Handler = http.server.SimpleHTTPRequestHandler
    httpd = socketserver.TCPServer(("", PORT), Handler)
    httpd.serve_forever()

def start():
    serverStart = threading.Thread(target=runServer)
    serverStart.start()
    print("""
Welcome to Insidirepo!

Your server is already running on port 8081.

On Windows run ipconfig to get your local ip.
On MacOS and Linux run ifconifg to get your local ip.
""")

start()
