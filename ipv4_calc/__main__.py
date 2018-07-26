#! /usr/bin/env python3
#################################################################################
#     File Name           :     ipv4_calc/__main__.py
#     Created By          :     Eloi Silva (etch.linux@gmail.com)
#     Creation Date       :     [2018-06-20 14:18]
#     Last Modified       :     [2018-07-26 17:43]
#     Description         :      
#################################################################################

import sys
import argparse
import ipv4_calc
import ipv4_calc.ipv4 as ipv4

USAGE='''ipv4_calc [-h]
ipv4_calc [-f FILE]
ipv4_calc [IPs ...]
ipv4_calc [IPs ...] [-f FILE]
'''

# Creating a parser arguments
parser = argparse.ArgumentParser(usage=USAGE, description="Calculate IP, Mask, Network, Broadcast and print all hosts inside a network")

# Pass a file to read IPv4
parser.add_argument("-f", "--file", help="File with ip address. One ipv4 per line", type=argparse.FileType('r'), required=False)

# Positional arguments
parser.add_argument("IPs", help="Pass all ipv4/cidr as argument", nargs='*')

# Parsing arguments
args = parser.parse_args()

# Main function
def main():
    IPs = []
    if args.file:
        IPs += [ip.strip() for ip in args.file.readlines()]
    if args.IPs:
        IPs += args.IPs
    for ip in IPs:
        hosts = ipv4.network_to_hosts(ip)
        if hosts:
            ipv4.show_hosts(hosts)
        else:
            print('[Error] - There is no IPv4 to calculate')

if __name__ == '__main__':
    main()
