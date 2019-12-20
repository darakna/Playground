__author__ = 'darakna'
import socket

def main(dest_name):
    print("starting...")
    dest_addr = socket.gethostbyname(dest_name)
    port = 33434
    max_hops = 30
    icmp = socket.getprotobyname('icmp')
    udp = socket.getprotobyname('udp')
    ttl = 1
    while True:
        recv_socket = socket.socket(socket.AF_INET, socket.SOCK_RAW, icmp)
        send_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM, udp)
        send_socket.setsockopt(socket.SOL_IP, socket.IP_TTL, ttl)
        recv_socket.bind((b"", port))
        send_socket.sendto(b"", (dest_name, port))
        curr_addr = None
        curr_name = None
        print("trying...")
        try:
            _, curr_addr = recv_socket.recvfrom(512)
            curr_addr = curr_addr[0]
            print("more trying...")
            try:
                curr_name = socket.gethostbyaddr(curr_addr)[0]
            except socket.error:
                curr_name = curr_addr
        except socket.error:
            print("failing with: ...[%]" % socket.error)
            pass
        finally:
            send_socket.close()
            recv_socket.close()

        if curr_addr is not None:
            curr_host = "%s (%s)" % (curr_name, curr_addr)
        else:
            curr_host = "*"
        print("%d\t%s" % (ttl, curr_host))

        ttl += 1
        if curr_addr == dest_addr or ttl > max_hops:
            print("done...")
            break

if __name__ == "__main__":
    main('8.8.8.8')