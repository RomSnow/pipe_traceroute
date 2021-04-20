import socket


def read_data(src: str) -> str:
    out_str = ''
    sock = socket.create_connection(('whois.ripe.net', 43))
    sock.settimeout(0.5)
    sock.send(f'-r --resource {src}\n'.encode())

    while True:
        try:
            buffer = sock.recv(2048)
        except socket.timeout:
            break

        if not buffer:
            break

        out_str += buffer.decode()

    return out_str


if __name__ == '__main__':
    print(read_data('8.8.8.8'))
