def generate_random():
    import random
    return random.randint(1, 100)

def handle_request(request_text: str) -> str:
    try:
        # 极简解析：只看第一行
        request_line = request_text.splitlines()[0]
        method, path, _ = request_line.split()

        if method == "GET" and path == "/random":
            result = generate_random()
            body = str(result)
            return http_response(200, body)

        else:
            return http_response(404, "Not Found")

    except Exception as e:
        # 统一兜底错误
        return http_response(500, f"Internal Server Error: {e}")
    
def http_response(status_code: int, body: str) -> str:
    return (
        f"HTTP/1.1 {status_code} OK\r\n"
        f"Content-Length: {len(body)}\r\n"
        f"Content-Type: text/plain\r\n"
        f"\r\n"
        f"{body}"
    )

import socket

def run_server(host="127.0.0.1", port=8080):
    server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server.bind((host, port))
    server.listen(5)

    print(f"Listening on http://{host}:{port}")

    while True:
        conn, addr = server.accept()
        with conn:
            request = conn.recv(1024).decode()
            response = handle_request(request)
            conn.sendall(response.encode())

if __name__ == "__main__":
    run_server()
