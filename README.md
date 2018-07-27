# IPv4 Calc
Python module to calc IP, Mask, Network and Broadcast

The main function is a disaggregate


# Version 4.1.1
This version of ipv4_calc can be installed as a package using pip.


# Install
Use pip to install the package

Installing:

pip setup.py install

-Or-

pip install ipv4_calc.tar.bz2


# Usage not installed
Syntax:

ipv4_calc [-h]

ipv4_calc [-f FILE]

ipv4_calc [IPs ...]

ipv4_calc [IPs ...] [-f FILE]


Example:

python3 ipv4_calc 69.108.111.105/25 207.102.45.2/30 123.10.1.5

python3 ipv4_calc FileWithIPs


# Usage Installed

disaggregate [-h]

disaggregate [-f FILE]

disaggregate [IPs ...]

disaggregate [IPs ...] [-f FILE]

disaggregate 69.108.111.105/25 207.102.45.2/30 123.10.1.5

Example:

python3 ipv4_calc 69.108.111.105/25 207.102.45.2/30 123.10.1.5

python3 ipv4_calc FileWithIPs
