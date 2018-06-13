#! /usr/bin/env python3
#################################################################################
#     File Name           :     ipv4.py
#     Version             :     V1
#     Created By          :     Eloi Silva (etch.linux@gmail.com)
#     Creation Date       :     [2018-05-21 19:36]
#     Last Modified       :     [2018-06-13 18:53]
#     Description         :      
#################################################################################

IPs = ["192.168.19.128/24", "192.168.225.64/26", "172.16.33.213/27", "10.128.63.229"]

def block_ipv4(ip):
    try:
        ip_blocks = list(map(check_oct, ip.rstrip().lstrip().split('/')[0].split('.')))
        mask = int(ip.split('/')[1]) if len(ip.split('/')) == 2 else 32
        if len(ip_blocks) == 4:
            return ip_blocks, mask
        else:
            raise ValueError("Value is not a IPv4")
    except Exception:
        print('Invalid IPv4: %s' % ip)
        return None

def check_oct(octeto):
    octeto = int(octeto)
    if octeto < 255 and octeto >= 0:
        return octeto
    else:
        return False

def mask_bin(mask):
    if mask < 32:
        bits0 = 32 - mask
        mask = (mask * '1') + (bits0 * '0')
    else:
        mask = mask * '1'
    mask = [mask[:8], mask[8:16], mask[16:24], mask[24:]]
    return mask

def ip_bin(ip):
    ip = bin(ip)[2:]
    if len(ip) < 8:
        bits0 = 8 - len(ip)
        ip = (bits0 * '0') + ip
    return ip

def mask_ip(ip, mask):
    network = []
    for o in range(4):
        network.append(int(ip[o], base=2) & int(mask[o], base=2))
    return network

def main(ips):
    for ip in ips:
        ip_b, mask = block_ipv4(ip)
        ip_bits = list(map(ip_bin, ip_b))
        mask_bits = mask_bin(mask)
        #yield (ip_b, ip_bits, mask_bits)
        network = mask_ip(ip_bits, mask_bits)
        print('IP: %s:\nIP Bits: %10s\nMask Bits: %10s\nNetwork: %10s\n' % (ip, ip_bits, mask_bits, network))
        #yield ip_b, ip_bits, mask_bits, network

