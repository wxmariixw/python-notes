import ipaddress

def int32_to_ip(int32):
    ipv4 = ipaddress.IPv4Address(int32)
    return str(ipv4)