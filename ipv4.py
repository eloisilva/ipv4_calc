#! /usr/bin/env python3
#################################################################################
#     File Name           :     ipv4.py
#     Version             :     V3
#     Created By          :     Eloi Silva (etch.linux@gmail.com)
#     Creation Date       :     [2018-05-21 19:36]
#     Last Modified       :     [2018-06-13 19:28]
#     Description         :      
#################################################################################

import sys

IPs = ["192.168.19.128/24", "192.168.225.64/26", "172.16.33.213/27", "10.128.63.229"]

def ip_calc(ip):
    ip, mask = ip_mask_check(ip)
    ip = ip_bin(ip)
    mask = convert_int_to_bits(mask)
    network = network_calc(ip, mask)
    broadcast = broadcast_calc(mask, network)
    return (ip, mask, network, broadcast)

def ip_mask_check(ip):
    '''Check if it is a valid IPv4 address
    Return:
      A list of IPv4 octet
      CIDR Mask integer
    '''
    try:
        # Check IPv4 blocks and mask and return ip octet blocks and CIDR mask
        ip_blocks = [block for block in map(ip_oct_check, ip.rstrip().lstrip().split('/')[0].split('.')) if block]
        mask = int(ip.split('/')[1]) if len(ip.split('/')) == 2 else 32
        if len(ip_blocks) == 4:
            return ip_blocks, mask
        else:
            raise ValueError("Value is not a IPv4")
    except Exception:
        sys.stderr.write('Invalid IPv4: %s' % ip)
        return None

def ip_oct_check(octeto):
    octeto = int(octeto)
    if octeto < 256 and octeto >= 0:
        return octeto
    else:
        return False

def convert_int_to_bits(bits, bits_total=32):
    bits = bits * '1'
    if len(bits) < bits_total:
        bits0 = bits_total - len(bits)
        bits += bits0 * '0'
    return bits

def convert_decimal_to_bits(decimal, bits_total=8):
    decimal = bin(decimal)[2:]
    if len(decimal) < bits_total:
        bits0 = bits_total - len(decimal)
        decimal = (bits0 * '0') + decimal
    return decimal

def ip_bin(ip):
    return ''.join([b for b in map(convert_decimal_to_bits, ip)])

def bits32_to_ip(bits):
    def base10(bits):
        if not bits:
            return ''
        else:
            return str(int(bits[0:8], base=2)) + '.' + bits32_to_ip(bits[8:])
    return base10(bits).rstrip('.')

def network_calc(ip, mask):
    return convert_decimal_to_bits(int(ip, base=2) & int(mask, base=2), bits_total=32)

def broadcast_calc(mask, network):
    bits = mask.count('0')
    if bits > 0:
        broadcast = int(network, base=2) + int(bits * '1', base=2)
        return convert_decimal_to_bits(broadcast, bits_total=32)
    else:
        return network

def ip_hosts(network, broadcast):
    hosts = set([network, broadcast])
    first, last = int(network, base=2), int(broadcast, base=2)
    for host in range(first, last):
        hosts.add(bin(host)[2:])
    return hosts

def show_hosts(hosts):
    for host in sorted(hosts):
        print(bits32_to_ip(host) + '/32')

# Exec main test
def main(ips):
    for ip in ips:
        ip, mask, network, broadcast = ip_calc(ip)
        hosts = ip_hosts(network, broadcast)
        show_hosts(hosts)
        input('\n----Press Enter----')

if __name__ == '__main__':
    main(IPs)
