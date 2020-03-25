#!/usr/bin/env python3

from http.server import BaseHTTPRequestHandler, HTTPServer, HTTPStatus

hostName = "0.0.0.0"
serverPort = 8080

response = '''{
  "apiVersion": "authorization.k8s.io/v1beta1",
  "kind": "SubjectAccessReview",
  "status": {
    "allowed": true
  }
}'''

class MyServer(BaseHTTPRequestHandler):
    def send_allow_response(self):
        content_length = self.headers['Content-Length']
        body = b''
        if content_length is not None:
            body = self.rfile.read(int(str(content_length)))

        print(self.headers)
        print(body.decode('utf-8'))

        self.send_response_only(HTTPStatus.OK)
        self.send_header('Content-Type', 'application/json')
        self.end_headers()
        self.wfile.write(bytes(response, 'UTF-8'))

    def do_GET(self):
        self.send_allow_response()

    def do_POST(self):
        self.send_allow_response()


if __name__ == '__main__':
    webServer = HTTPServer((hostName, serverPort), MyServer)
    print("Server started http://%s:%s" % (hostName, serverPort))

    try:
        webServer.serve_forever()
    except KeyboardInterrupt:
        pass

    webServer.server_close()
    print("Server stopped.")