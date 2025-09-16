#!/usr/bin/env python3
import http.server
import socketserver
import os

# 현재 디렉토리에서 서버 실행
PORT = 8080

class MyHTTPRequestHandler(http.server.SimpleHTTPRequestHandler):
    def end_headers(self):
        self.send_header('Cache-Control', 'no-cache, no-store, must-revalidate')
        self.send_header('Pragma', 'no-cache')
        self.send_header('Expires', '0')
        super().end_headers()

if __name__ == "__main__":
    os.chdir(os.path.dirname(os.path.abspath(__file__)))

    with socketserver.TCPServer(("", PORT), MyHTTPRequestHandler) as httpd:
        print(f"서버가 http://localhost:{PORT}에서 실행 중입니다.")
        print("브라우저에서 http://localhost:8080/index.html 로 접속하세요.")
        print("서버를 중지하려면 Ctrl+C를 누르세요.")
        try:
            httpd.serve_forever()
        except KeyboardInterrupt:
            print("\n서버를 중지합니다.")
            httpd.shutdown()