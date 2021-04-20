#!/usr/bin/sudo python3

import socket
import struct
import sys

from formatter import Formatter
from get_RIPE.RIPE_data import get_data_by_ip


def main(dest_name, hops):
    dest_addr = socket.gethostbyname(dest_name)
    port = 5000
    max_hops = hops
    icmp = socket.getprotobyname('icmp')
    udp = socket.getprotobyname('udp')
    ttl = 1

    print('#\t' + Formatter(
        150, 'host name', 'host address', 'AS', 'country', 'provider'
    ).get_string(), end='\n\n')

    while True:
        recv_socket = socket.socket(socket.AF_INET, socket.SOCK_RAW, icmp)
        send_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM, udp)
        send_socket.setsockopt(socket.SOL_IP, socket.IP_TTL, ttl)

        timeout = struct.pack("ll", 1, 0)
        recv_socket.setsockopt(socket.SOL_SOCKET, socket.SO_RCVTIMEO, timeout)

        recv_socket.bind(("", port))
        print(f"{ttl}", end='\t')
        send_socket.sendto(b"", (dest_name, port))
        curr_addr = None
        curr_name = None
        finished = False
        tries = 3
        while not finished and tries > 0:
            try:
                _, curr_addr = recv_socket.recvfrom(512)
                finished = True
                curr_addr = curr_addr[0]
                try:
                    curr_name = socket.gethostbyaddr(curr_addr)[0]
                except socket.error:
                    curr_name = curr_addr
            except socket.error:
                tries = tries - 1
                print("*", end=' ')

        send_socket.close()
        recv_socket.close()

        if not finished:
            pass

        if curr_addr is not None:
            ripe_data = get_data_by_ip(curr_addr)
            formatted_str = Formatter(150, curr_name,
                                      curr_addr,
                                      ripe_data.as_,
                                      ripe_data.country,
                                      ripe_data.provider)

            curr_host = formatted_str.get_string()
        else:
            curr_host = ""
        print(f"{curr_host}\n")

        ttl += 1
        if curr_addr == dest_addr or ttl > max_hops:
            break


if __name__ == "__main__":
    main(sys.argv[1], sys.argv[2])
