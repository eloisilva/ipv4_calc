#! /usr/bin/env python3
#################################################################################
#     File Name           :     ipv4.py
#     Version             :     V4
#     Created By          :     Eloi Silva (etch.linux@gmail.com)
#     Creation Date       :     [2018-05-21 19:36]
#     Last Modified       :     [2018-06-18 19:09]
#     Description         :      
#################################################################################

import sys

def ip_calc(ip):
    '''
    ip: receive a ipv4/cidr as argument
    Return: ip, mask, network and broadcast in binary format
    '''
    ip, mask = ip_check(ip)
    network = network_calc(ip, mask)
    broadcast = broadcast_calc(mask, network)
    return (ip, mask, network, broadcast)

def ip_check(ip):
    '''
    Check if it is a valid IPv4 address
    Return:
      A list of IPv4 octet
      CIDR Mask integer
    '''
    try:
        # Check IPv4 blocks and mask and return ip octet blocks and CIDR mask
        ip_blocks = [block for block in map(ip_oct_check, ip.rstrip().lstrip().split('/')[0].split('.')) if block]
        mask = int(ip.split('/')[1]) if len(ip.split('/')) == 2 else 32
        if len(ip_blocks) == 4:
            return ip_bin(ip_blocks), convert_int_to_bits(mask)
        else:
            raise ValueError("Value is not a IPv4")
    except Exception:
        sys.stderr.write('Invalid IPv4: %s' % ip)
        return None

def ip_bin(ip):
    return ''.join([b for b in map(convert_decimal_to_bits, ip)])

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

def convert_bits_to_ip(bits):
    def base10(bits):
        if not bits:
            return ''
        else:
            return str(int(bits[0:8], base=2)) + '.' + convert_bits_to_ip(bits[8:])
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

def hosts_calc(network, broadcast):
    hosts = set([network, broadcast])
    first, last = int(network, base=2), int(broadcast, base=2)
    for host in range(first, last):
        hosts.add(bin(host)[2:])
    return hosts

def print_ip_calc(ip):
    ip, mask, network, broadcast = map(convert_bits_to_ip, ip_calc(ip))
    print('%-15s %-15s %-15s %-15s' % (ip, mask, network, broadcast))

def show_hosts(hosts):
    for host in sorted(hosts):
        print(convert_bits_to_ip(host) + '/32')

# Exec main test
def main(ips):
    for ip in ips:
        ip, mask, network, broadcast = ip_calc(ip)
        hosts = hosts_calc(network, broadcast)
        show_hosts(hosts)
        input('\n----Press Enter----')

if __name__ == '__main__':
    main(IPs)
