#! /usr/bin/env python3
#################################################################################
#     File Name           :     ipv4.py
#     Version             :     V2
#     Created By          :     Eloi Silva (etch.linux@gmail.com)
#     Creation Date       :     [2018-05-21 19:36]
#     Last Modified       :     [2018-06-13 19:10]
#     Description         :      
#################################################################################

import sys

IPs = ["192.168.19.128/24", "192.168.225.64/26", "172.16.33.213/27", "10.128.63.229"]

def ip_calc(ip):
    ip, mask = ip_oct_check(ip)
    if ip and mask:
        bit_mask = convert_int_to_bits(mask)
        bit_ip = ip_bin(ip)
        bit_network = bin(int(bit_mask, base=2) & int(bit_ip, base=2))[2:]
        n_hosts = bit_mask.count('0') * '1'
        bit_broadcast = bin(int(bit_network, base=2) + int(n_hosts, base=2))[2:]
        print('%s\n%s\n%s\n%s' % tuple(map(bin32_to_ip, [bit_ip, bit_mask, bit_network, bit_broadcast])))

def check_ip_mask(ip):
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
    return ''.join([b for b in map(ip_normalize, ip)])

def bin32_to_ip(bits):
    def base10(bits):
        if not bits:
            return ''
        else:
            return str(int(bits[0:8], base=2)) + '.' + bin32_to_ip(bits[8:])
    return base10(bits).rstrip('.')



'''
def mask_ip(ip, mask):
    network = []
    for o in range(4):
        network.append(int(ip[o], base=2) & int(mask[o], base=2))
    return network
'''


# Exec main test
def main(ips):
    for ip in ips:
        ip_calc(ip)
        print()
        '''
        ip_b, mask = block_ipv4(ip)
        ip_bits = list(map(ip_bin, ip_b))
        mask_bits = mask_bin(mask)
        #yield (ip_b, ip_bits, mask_bits)
        network = mask_ip(ip_bits, mask_bits)
        print('IP: %s:\nIP Bits: %10s\nMask Bits: %10s\nNetwork: %10s\n' % (ip, ip_bits, mask_bits, network))
        #yield ip_b, ip_bits, mask_bits, network
        '''
