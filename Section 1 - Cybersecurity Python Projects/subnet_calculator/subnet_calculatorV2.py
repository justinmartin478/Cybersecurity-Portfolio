# subnet_calculator.py
from fancytools.fancy import fancy_print, colors
from rich.console import Console
from rich.text import Text
import random
import ipaddress

def ip_to_bin(ip):
    return '.'.join(f'{int(octet):08b}' for octet in ip.split('.'))

def ip_to_hex(ip):
    return '.'.join(f'{int(octet):02X}' for octet in ip.split('.'))

def main():
    ip_input = input("Enter IP address (e.g., 192.168.1.10): ").strip()
    mask_input = input("Enter subnet mask (CIDR, e.g., 24 or dotted, e.g., 255.255.255.0): ").strip()

    # Handle CIDR or dotted mask
    if '/' in ip_input:
        network = ipaddress.IPv4Network(ip_input, strict=False)
    else:
        if mask_input.isdigit():
            mask = int(mask_input)
            network = ipaddress.IPv4Network(f"{ip_input}/{mask}", strict=False)
        else:
            network = ipaddress.IPv4Network(f"{ip_input}/{mask_input}", strict=False)

    ip = str(network.network_address)
    mask = str(network.netmask)
    broadcast = str(network.broadcast_address)
    first_host = str(list(network.hosts())[0]) if network.num_addresses > 2 else ip
    last_host = str(list(network.hosts())[-1]) if network.num_addresses > 2 else broadcast
    num_hosts = network.num_addresses - 2 if network.num_addresses > 2 else network.num_addresses

    fancy_print("\n--- Subnetting Breakdown ---", label_rainbow=True)
    fancy_print(f"IP Address:        {ip}", random_color=True, random_style=True)
    fancy_print(f"  Binary:          {ip_to_bin(ip)}", random_color=True, random_style=True)
    fancy_print(f"  Hexadecimal:     {ip_to_hex(ip)}", random_color=True, random_style=True)
    fancy_print(f"Subnet Mask:       {mask}", random_color=True, random_style=True)
    fancy_print(f"  Binary:          {ip_to_bin(mask)}", random_color=True, random_style=True)
    fancy_print(f"  Hexadecimal:     {ip_to_hex(mask)}", random_color=True, random_style=True)
    fancy_print(f"Network Address:   {network.network_address}", random_color=True, random_style=True)
    fancy_print(f"  Binary:          {ip_to_bin(str(network.network_address))}", random_color=True, random_style=True)
    fancy_print(f"  Hexadecimal:     {ip_to_hex(str(network.network_address))}", random_color=True, random_style=True)
    fancy_print(f"Broadcast Address: {broadcast}", random_color=True, random_style=True)
    fancy_print(f"  Binary:          {ip_to_bin(broadcast)}", random_color=True, random_style=True)
    fancy_print(f"  Hexadecimal:     {ip_to_hex(broadcast)}", random_color=True, random_style=True)
    fancy_print(f"First Host:        {first_host}", random_color=True, random_style=True)
    fancy_print(f"Last Host:         {last_host}", random_color=True, random_style=True)
    fancy_print(f"Number of Hosts:   {num_hosts}", random_color=True, random_style=True)
    fancy_print(f"Subnet Range:      {first_host} - {last_host}", random_color=True, random_style=True)

if __name__ == "__main__":
    main()
