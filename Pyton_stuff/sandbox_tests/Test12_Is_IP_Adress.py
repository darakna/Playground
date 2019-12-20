__author__ = 'darakna'
import socket
def is_valid_ipv4_address(address):
    try:
        socket.inet_pton(socket.AF_INET, address)
    except AttributeError:  # no inet_pton here, sorry
        try:
            socket.inet_aton(address)
        except socket.error:
            return False
        return address.count('.') == 3
    except socket.error:  # not a valid address
        return False

    return True

def is_valid_ipv6_address(address):
    try:
        socket.inet_pton(socket.AF_INET6, address)
    except socket.error:  # not a valid address
        return False
    return True
def is_valid_ip(ip):
    """Validates IP addresses.
    """
    return is_valid_ipv4_address(ip) or is_valid_ipv6_address(ip)


print(is_valid_ip("192.168.0.0"))
print(is_valid_ip("292.168.0.0"))
print(is_valid_ip("4"))
print(is_valid_ipv4_address("0.6959"))