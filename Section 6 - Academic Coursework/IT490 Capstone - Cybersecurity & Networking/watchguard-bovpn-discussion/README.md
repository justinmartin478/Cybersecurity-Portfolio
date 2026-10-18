# Company ABC Seattle to Denver BOVPN

*Site-to-site IPsec VPN with WatchGuard Firebox T45*

**Course:** IT490 Capstone - Cybersecurity & Networking &nbsp;·&nbsp; **Week:** 4 &nbsp;·&nbsp; **Type:** Discussion post

> The full assignment is rendered below. The original and a formal copy are available for download: [**Discussion post (HTML)**](./watchguard_bovpn_discussion_post.html) · [**PDF**](./IT490_WatchGuard_BOVPN_Discussion_Justin_Martin.pdf)

| Seattle | IKEv2 tunnel | Denver |
| --- | --- | --- |
| 203.0.113.10 \| 192.168.10.0/24 | AES-GCM 256 \| DH 19 | 198.51.100.20 \| 192.168.20.0/24 |

---

For company ABC, I would install a WatchGuard Firebox T45 at both the Seattle and Denver offices and configure an IPsec Branch Office VPN, or BOVPN. Since the scenario does not provide office sizes, I am assuming each location has no more than 20 users. WatchGuard identifies the T45 as suitable for small offices and branch locations of this size. I would use local management through Fireware Web UI for this configuration.

## Addressing plan

I would use the following addressing scheme to keep the two office networks separate.

| Setting | Seattle | Denver |
| --- | --- | --- |
| Firebox model | T45 | T45 |
| External interface | Interface 0 | Interface 0 |
| Example public IP | 203.0.113.10/24 | 198.51.100.20/24 |
| Example ISP gateway | 203.0.113.1 | 198.51.100.1 |
| Private LAN | 192.168.10.0/24 | 192.168.20.0/24 |
| Trusted interface | 192.168.10.1 | 192.168.20.1 |
| Test workstation | 192.168.10.100 | 192.168.20.100 |
| Example internal HTTPS server | 192.168.10.50 | 192.168.20.50 |

The public addresses are documentation placeholders for this exercise. They would be replaced with actual ISP assigned addresses during deployment. The private subnets do not overlap, which allows each Firebox to identify traffic intended for the other office.

## Configuration steps

### 1. Activate and connect both Fireboxes

I would register each appliance through WatchGuard's activation page using its serial number. At each office, I would connect interface 0 to the Internet connection and interface 1 to a setup computer configured to obtain an address through DHCP. After powering on the Firebox, the setup computer should receive an address on the default 10.0.1.0/24 network.

### 2. Complete the initial setup

From the setup computer, I would open https://10.0.1.1:8080 and sign in using the factory username admin and passphrase readwrite. I would complete the Web Setup Wizard, select local management, and replace the default administrative credentials with strong passwords. I would then configure each external interface, subnet mask, ISP gateway, and DNS settings. The trusted interface would use the private address listed in the table. After changing that address, I would reconnect the computer to the appropriate LAN and access the Firebox through its new trusted address.

Before configuring the VPN, I would confirm that both offices have Internet connectivity and that their workstations use the local Firebox as their default gateway.

### 3. Create the Seattle VPN gateway

On the Seattle Firebox, I would select **VPN > Branch Office VPN**, click **Add** under Gateways, and name the gateway SeattleToDenver. I would select IPv4 addresses and shared key authentication. I would generate a random 32 character ASCII secret and securely enter the same value on both Fireboxes. The actual secret would be stored securely rather than included in the discussion or configuration documentation.

### 4. Define the Seattle gateway endpoints

In the Gateway Endpoint section, I would click **Add**. For the local gateway, I would select external interface 0, use its primary IPv4 address, and set the gateway ID by IP address to 203.0.113.10.

For the remote gateway, I would select a static IP address of 198.51.100.20 and use that same address as the remote gateway ID. This identifies the Denver Firebox as Seattle's VPN peer.

### 5. Configure Phase 1

On the **Phase 1 Settings** tab, I would select IKEv2 and configure AES GCM with 256 bit encryption and Diffie Hellman Group 19. I would retain the recommended Dead Peer Detection settings and use matching Phase 1 settings on the Denver Firebox. In WatchGuard's IKEv2 implementation, NAT Traversal and Dead Peer Detection are always enabled. I would then save the gateway.

### 6. Create the Seattle tunnel and route

Under **VPN > Branch Office VPN**, I would click **Add** in the Tunnels section, name the tunnel SeattleDenverTunnel, and select the SeattleToDenver gateway.

On the Addresses tab, I would add a tunnel route with local network 192.168.10.0/24 and remote network 192.168.20.0/24. I would select bidirectional traffic and leave tunnel NAT disabled because these networks do not overlap. I would clear the option that adds the tunnel to the default BOVPN allow policies so that I could explicitly control which services cross the connection.

### 7. Configure Phase 2

On the tunnel's **Phase 2 Settings** tab, I would select ESP with AES 256 bit encryption and SHA2-256 authentication. I would enable Perfect Forward Secrecy with Diffie Hellman Group 14 and use the same proposal and security association lifetime on both appliances. Phase 2 defines how the actual traffic between the offices is protected. I would save the tunnel after confirming these settings.

### 8. Configure the Denver Firebox

I would repeat the gateway and tunnel configuration in Denver, using the same shared secret and matching Phase 1 and Phase 2 settings. The local and remote addresses must be reversed.

| VPN setting | Seattle Firebox | Denver Firebox |
| --- | --- | --- |
| Local gateway address and ID | 203.0.113.10 | 198.51.100.20 |
| Remote gateway address and ID | 198.51.100.20 | 203.0.113.10 |
| Local tunnel network | 192.168.10.0/24 | 192.168.20.0/24 |
| Remote tunnel network | 192.168.20.0/24 | 192.168.10.0/24 |

### 9. Add access policies

I would add HTTPS policies on both Fireboxes that allow Seattle's LAN to reach Denver's server at 192.168.20.50 and Denver's LAN to reach Seattle's server at 192.168.10.50 on TCP port 443.

I would remove broad default source and destination entries from these new policies and replace them with the specified networks and hosts. I would also add temporary Ping policies between the two test workstations and enable logging for the new policies. These policies are necessary because I excluded the tunnel from the default BOVPN allow policies.

### 10. Test and troubleshoot

From Seattle's workstation at 192.168.10.100, I would ping Denver's workstation at 192.168.20.100, then repeat the test in the opposite direction. I would also test each approved HTTPS application.

In Fireware Web UI, I would check **System Status > VPN Statistics** to confirm that the tunnel is established and traffic counters increase during testing. If the tunnel fails, I would run the VPN Diagnostic Report and compare the shared secret, gateway IDs, encryption proposals, and tunnel networks on both devices. If negotiation succeeds but application traffic fails, I would check firewall policies, workstation gateways, and host firewalls.

### 11. Document and maintain the connection

After successful testing, I would remove the temporary Ping policies unless they are needed for ongoing monitoring. I would save configuration backups and document the addressing plan, VPN settings, approved services, and test results.

My main takeaway is that creating an encrypted tunnel is only part of the setup. The two Fireboxes must agree on their VPN settings, and the access policies must allow the services company ABC actually needs.

## References

WatchGuard Technologies. (n.d.). *Firebox T45 hardware guide*.

WatchGuard Technologies. (2022). *Firebox T45 quick start guide*.

WatchGuard Technologies. (n.d.). *Configure manual BOVPN gateways*.

WatchGuard Technologies. (n.d.). *Define gateway endpoints for a BOVPN gateway*.

WatchGuard Technologies. (n.d.). *Configure IPsec VPN Phase 1 settings*.

WatchGuard Technologies. (n.d.). *Add routes for a tunnel*.

WatchGuard Technologies. (n.d.). *Configure Phase 2 settings*.

WatchGuard Technologies. (n.d.). *Add policies to your configuration*.

WatchGuard Technologies. (n.d.). *Use the VPN Diagnostic Report*.

## Outcome

I planned a WatchGuard Firebox T45 branch office VPN between Company ABC's Seattle and Denver offices, starting with a non-overlapping addressing plan. I walked through the IKEv2 Phase 1 and Phase 2 settings on both appliances and showed how the local and remote values mirror each other. I replaced the default BOVPN allow policies with explicit HTTPS and test rules and laid out how I would verify and troubleshoot the tunnel.
