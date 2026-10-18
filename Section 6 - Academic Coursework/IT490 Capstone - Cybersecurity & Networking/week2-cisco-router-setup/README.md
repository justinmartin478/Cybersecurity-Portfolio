# Basic Cisco Router Setup and Verification

*Configuration of SEA-R01 from a new router state, with LAN and WAN addressing, SSH access, password protection, static routing, EIGRP, and documented verification*

**Course:** IT490 Capstone - Cybersecurity & Networking &nbsp;·&nbsp; **Week:** 2 &nbsp;·&nbsp; **Type:** Report

> The full assignment is rendered below. The original and a formal copy are available for download: [**Word document**](./IT490_Week2_Basic_Cisco_Router_Setup_Portfolio_Justin_Martin.docx) · [**PDF**](./IT490_Week2_Basic_Cisco_Router_Setup_Portfolio_Justin_Martin.pdf)

| Requirements Mapped | Usable LAN Hosts | Only VTY Transport | Evidence Figures |
| --- | --- | --- | --- |
| 14 | 510 | SSH v2 | 19 |

---

## Summary

Configuration of SEA-R01 from a new router state, with LAN and WAN addressing, SSH access, password protection, static routing, EIGRP, and documented verification. The tested management and routing paths worked. The assignment's static route overlaps the LAN subnet and remains a documented configuration limitation.

## Project Snapshot

| | |
| --- | --- |
| Author | Justin Martin |
| Course | IT490 Capstone, Green River College |
| Date | October 4, 2026 |
| Environment | Cisco Packet Tracer, two Cisco 2911 routers (IOS 15.1), Cisco 2960 switch, one admin PC |
| Skills demonstrated | VLSM subnet sizing, IPv4 and IPv6 interface configuration, SSH hardening, Telnet restriction, password storage types, EIGRP, static routing, route-table analysis, verification testing |

## 01. Executive Results

SEA-R01 was configured in Cisco Packet Tracer using a Cisco 2911 router. The LAN and WAN interfaces reached an up/up state, SSH access succeeded, Telnet access was rejected, and EIGRP exchanged the LAN route with WAN-R02. Both routers returned [OK] when their configurations were saved.

| Area | Result | Evidence |
| --- | --- | --- |
| LAN capacity | 192.168.16.1/23 provides 510 usable addresses | Figures 1.5 and 1.9 |
| WAN interfaces | IPv4 and IPv6 link tests reached 100% success | Figures 1.6, 1.7 and 1.8 |
| Remote access | SSH login and enable succeeded; Telnet was closed | Figures 1.10 and 1.11 |
| EIGRP | Neighbor formed; WAN-R02 learned the LAN /23 | Figures 1.12 through 1.14 |
| Static route | Required /24 installed; overlaps connected /23 | Figure 1.15 |
| Final validation | PC reached LAN gateway and WAN peer with no loss | Figure 1.16 |
| Persistence | Running configurations copied to startup configurations | Figures 1.17 and 1.18 |

## 02. Environment and Addressing

| Device and interface | Address | Purpose |
| --- | --- | --- |
| SEA-R01 Gi0/0 | 192.168.16.1/23 | LAN gateway |
| SEA-R01 Gi0/1 | 10.0.0.2/30<br>2001:db8:a0b:12f0::1/64 | WAN interface |
| WAN-R02 Gi0/0 | 10.0.0.1/30<br>2001:db8:a0b:12f0::2/64 | WAN test peer |
| Admin-PC Fa0 | 192.168.17.10/23 | SSH client and ping source |
| LAN-SW01 | 2960 switch with no management IP assigned | LAN connectivity |

Admin-PC uses gateway 192.168.16.1 and DNS server 8.8.8.8. The PC connects to LAN-SW01 Fa0/1, the switch Gi0/1 connects to SEA-R01 Gi0/0, and SEA-R01 Gi0/1 connects to WAN-R02 Gi0/0.

The /30 WAN IPv4 subnet, /64 IPv6 prefix length, EIGRP autonomous system 100, local SSH account admin, domain abc.example, and supporting test devices are lab choices. The assignment specifies the primary router settings but does not supply these supporting values. The routers report IOS version 15.1.

### LAN Subnet Calculation

A /24 contains 256 total addresses and 254 usable host addresses, which is insufficient for 270 hosts. A /23 leaves 9 host bits: 2^9 − 2 = 510 usable host addresses. The mask is 255.255.254.0, the network is 192.168.16.0, the broadcast is 192.168.17.255, and the usable range is 192.168.16.1 through 192.168.17.254.

| Prefix | Mask | Host bits | Usable hosts | Meets 270? |
| --- | --- | --- | --- | --- |
| /24 | 255.255.255.0 | 8 | 254 | No |
| /23 | 255.255.254.0 | 9 | 510 | Yes |

The test PC address 192.168.17.10 demonstrates use of the second half of the /23. It also falls outside the overlapping /24 static route. A successful ping from this address does not validate routing for the entire LAN.

## 03. Assignment Requirement Mapping

| Item | Implemented setting | Verification |
| --- | --- | --- |
| a | LAN 192.168.16.1 with mask 255.255.254.0; no shutdown | Gi0/0 up/up; 510 usable addresses |
| b | WAN 2001:db8:a0b:12f0::1/64; no shutdown | Gi0/1 up/up; IPv6 peer ping 5/5 |
| c | hostname SEA-R01 | Final running configuration |
| d | ip name-server 8.8.8.8 | Final running configuration |
| e | transport input ssh on VTY 0 through 4 | Telnet connection closed without login |
| f | Local account, domain, RSA keys and SSH version 2 | Successful PC SSH session |
| g | enable secret It490Tmason! | Type 5 hash; enable access succeeded |
| h | service password-encryption; secret credentials | Type 7 line passwords and Type 5 secrets |
| i | no ip domain-lookup | Final running configuration |
| j | Console and VTY password iT490tMason* | Console login; VTY login local |
| k | ip route 192.168.16.0 255.255.255.0 10.0.0.1 | Static /24 installed; overlap discussed below |
| l | EIGRP 100 includes both directly connected IPv4 networks | Neighbor 10.0.0.1; learned LAN /23 |
| m | Interface, SSH, route, neighbor and ping checks | Evidence section |
| n | show running-config | Final configuration appendices |

## 04. Commands in Execution Order

These command sequences document the configuration workflow. Commands are entered at the router CLI unless a different device is named. The credentials are assignment supplied lab values.

### 1 Router Identity and Console Access

**SEA-R01**

```
enable
configure terminal
hostname SEA-R01
no ip domain-lookup
ip name-server 8.8.8.8
enable secret It490Tmason!
service password-encryption
line console 0
password iT490tMason*
login
logging synchronous
exit
end
```

The enable secret protects privileged EXEC access. Console login requires the assigned line password. logging synchronous prevents console status messages from disrupting typed commands.

### 2 SSH Access and Telnet Restriction

**SEA-R01**

```
configure terminal
ip domain-name abc.example
username admin secret iT490tMason*
crypto key generate rsa
! modulus prompt: 2048
ip ssh version 2
line vty 0 4
password iT490tMason*
login local
transport input ssh
exit
end
```

At the RSA modulus prompt, enter 2048. This is an interactive response, not a separate IOS command. The key size was selected during setup; the supplied screenshots do not independently show the modulus.

login local authenticates SSH with the admin account. The assigned VTY line password is present, but local account authentication takes precedence. transport input ssh restricts these VTY lines to SSH (Cisco, 2026).

### 3 SEA-R01 LAN and WAN Interfaces

**SEA-R01**

```
configure terminal
ipv6 unicast-routing
interface GigabitEthernet0/0
description LAN connection to LAN-SW01
ip address 192.168.16.1 255.255.254.0
no shutdown
exit
interface GigabitEthernet0/1
description WAN connection to WAN-R02
ip address 10.0.0.2 255.255.255.252
ipv6 address 2001:db8:a0b:12f0::1/64
no shutdown
exit
end
```

### 4 WAN-R02 Supporting Peer

**WAN-R02**

```
enable
configure terminal
hostname WAN-R02
no ip domain-lookup
ipv6 unicast-routing
interface GigabitEthernet0/0
description WAN connection to SEA-R01
ip address 10.0.0.1 255.255.255.252
ipv6 address 2001:db8:a0b:12f0::2/64
no shutdown
exit
end
```

### 5 Admin PC Addressing

In Desktop → IP Configuration, select Static. Enter IPv4 address 192.168.17.10, subnet mask 255.255.254.0, default gateway 192.168.16.1, and DNS server 8.8.8.8. No global IPv6 address was assigned to the PC.

### 6 EIGRP on SEA-R01

**SEA-R01**

```
configure terminal
router eigrp 100
no auto-summary
network 192.168.16.0 0.0.1.255
network 10.0.0.0 0.0.0.3
passive-interface GigabitEthernet0/0
end
```

The network statements select the LAN and WAN interfaces for IPv4 EIGRP. The LAN is passive to prevent neighbor formation toward the PC while retaining its network advertisement (Cisco, 2011).

### 7 EIGRP on WAN-R02

**WAN-R02**

```
configure terminal
router eigrp 100
no auto-summary
network 10.0.0.0 0.0.0.3
end
```

### 8 Required Static Route on SEA-R01

**SEA-R01**

```
configure terminal
ip route 192.168.16.0 255.255.255.0 10.0.0.1
end
```

IOS static routes specify a destination prefix and next hop. The assignment's phrase "from 192.168.16.0/24 to 10.0.0.1" is implemented as a destination route for 192.168.16.0/24 through 10.0.0.1. This interpretation creates the overlap described in the technical analysis.

### 9 Verification and Saving

| Device | Verification commands |
| --- | --- |
| SEA-R01 | show ip interface brief, show ipv6 interface brief, show ip ssh, show ip eigrp neighbors, show ip protocols, show ip route, ping 10.0.0.1, ping 2001:db8:a0b:12f0::2 |
| WAN-R02 | show ip route, ping 192.168.17.10 |
| Admin-PC | ssh -l admin 192.168.16.1, authenticate with iT490tMason*, enter enable and authenticate with It490Tmason!, then exit. Test telnet 192.168.16.1, ping 192.168.16.1, and ping 10.0.0.1. |

**Both Routers**

```
copy running-config startup-config
show running-config
```

Run the save command on both routers and press Enter at the destination filename prompt. The [OK] outputs confirm successful writes. Save the Packet Tracer project separately to retain the topology.

## 05. Technical Analysis and Reflection

### Static Route Overlap

SEA-R01 contains a connected 192.168.16.0/23 route and a static 192.168.16.0/24 route through WAN-R02. The routing table visibly contains both. The /24 is more specific, so traffic for other 192.168.16.x hosts matches the static route rather than the connected /23. The router's own 192.168.16.1 address retains a local /32 route (Cisco, 2024a).

WAN-R02 learned 192.168.16.0/23 through SEA-R01. Based on these installed routes, traffic to another 192.168.16.x LAN host would be forwarded toward WAN-R02 and then back toward SEA-R01, creating a routing loop. This consequence is inferred from the route tables; no affected host or loop test was added. Tests with 192.168.17.10 succeed because that address does not match the static /24.

The literal assignment route remains in the saved configuration for the exercise. Before using this design operationally, clarify the intended remote destination and remove or replace the overlapping route. A default route through 10.0.0.1 would be appropriate only if WAN-R02 actually provides an upstream path; that role was not established in this lab. Retest hosts in both halves of the /23 after correcting the requirement.

### Password Protection and Management Access

The final SEA-R01 configuration stores the enable secret and admin secret as Type 5 hashes. Console and VTY line passwords appear as Type 7 values after service password-encryption. Type 7 is reversible obfuscation, not strong password protection; Type 5 uses an older MD5 based hash. The assignment's password storage requirement is demonstrated, but these mechanisms should not be presented as modern production security (Cisco, 2024b). Newer IOS releases support Type 8 and Type 9 secrets through the algorithm-type option, which the IOS 15.1 image in this lab does not offer.

SSH version 2 was confirmed, and an actual SSH session reached privileged EXEC mode. The Telnet attempt briefly displayed "Open" and then closed without providing a login. Together with transport input ssh, this supports rejection of Telnet management access. WAN-R02 served only as a test peer; the assignment's management hardening was applied to SEA-R01.

### Validation Limits

The initial IPv4 WAN ping returned 4/5 replies; the repeat returned 5/5. Address resolution could explain the first loss, but no capture confirmed it. IPv6 WAN connectivity returned 5/5. DNS resolution, Internet connectivity, and persistence after reload were not tested.

Items d and i also interact. With no ip domain-lookup in place, the router does not query the configured name server, so 8.8.8.8 is stored in the configuration but not used by SEA-R01 itself. If router-side name resolution were needed later, transport preferred none on the console and VTY lines would still stop typos from being treated as Telnet hostnames while leaving domain lookup enabled.

show ip protocols confirmed disabled automatic summarization. The no auto-summary command does not appear in the running configurations because automatic summarization is already disabled by default in IOS 15, so IOS does not display it. IPv6 was tested only on the directly connected WAN; IPv6 EIGRP was not configured.

### Reflection

This exercise reinforced that entering a command successfully does not guarantee a sound routing design. I had to calculate the LAN mask from the host requirement, verify access with an actual SSH session, and compare the static route with the connected network. The overlap was the most useful lesson because successful pings from one address range could hide a problem elsewhere in the same LAN.

## 06. Evidence

### Evidence of Initial Configuration

**Figure 1.1 — Initial topology with router links still down before interface configuration.**

![Packet Tracer topology of Admin-PC, LAN-SW01, SEA-R01 and WAN-R02 with red link indicators on the router links](./screenshots/figure-1-1-initial-topology.png)

**Figure 1.2 — Early running configuration shows the hostname, enable secret, password service, and DNS settings.**

![SEA-R01 CLI showing an early show running-config with hostname, enable secret, service password-encryption and name server lines](./screenshots/figure-1-2-early-running-config.png)

### Evidence of SSH Configuration

**Figure 1.3 — show ip ssh confirms SSH version 2.0.**

![SEA-R01 CLI output of show ip ssh reporting SSH enabled at version 2.0](./screenshots/figure-1-3-show-ip-ssh.png)

**Figure 1.4 — Console and VTY configuration shows Type 7 passwords, local SSH authentication, and SSH only transport.**

![SEA-R01 running configuration lines for line con 0 and line vty 0 4 with Type 7 passwords, login local and transport input ssh](./screenshots/figure-1-4-console-vty-config.png)

### Evidence of Interface Status

**Figure 1.5 — IPv4 interface summary shows both configured router interfaces up/up.**

![SEA-R01 show ip interface brief output with GigabitEthernet0/0 and 0/1 up and up](./screenshots/figure-1-5-ipv4-interface-brief.png)

**Figure 1.6 — IPv6 interface summary shows the required WAN address on Gi0/1 in an up/up state.**

![SEA-R01 show ipv6 interface brief output listing the 2001:DB8:A0B:12F0::1 address on GigabitEthernet0/1](./screenshots/figure-1-6-ipv6-interface-brief.png)

### Evidence of WAN Connectivity

**Figure 1.7 — Initial WAN tests show IPv4 success of 4/5 and IPv6 success of 5/5.**

![SEA-R01 ping results to 10.0.0.1 at 4 of 5 and to 2001:db8:a0b:12f0::2 at 5 of 5](./screenshots/figure-1-7-initial-wan-pings.png)

**Figure 1.8 — Repeated IPv4 WAN ping succeeds with 5/5 replies.**

![SEA-R01 repeat ping to 10.0.0.1 with a 100 percent success rate](./screenshots/figure-1-8-repeat-ipv4-ping.png)

### Evidence of Admin PC Addressing

**Figure 1.9 — Admin PC uses 192.168.17.10 with the /23 mask, LAN gateway, and assigned DNS server.**

![Admin-PC IP Configuration window with static address 192.168.17.10, mask 255.255.254.0, gateway 192.168.16.1 and DNS 8.8.8.8](./screenshots/figure-1-9-admin-pc-ip-config.png)

### Evidence of Remote Access Tests

**Figure 1.10 — The PC authenticates over SSH and reaches the SEA-R01 privileged EXEC prompt.**

![Admin-PC command prompt showing an SSH login as admin to 192.168.16.1 that reaches the SEA-R01 enable prompt](./screenshots/figure-1-10-ssh-login.png)

**Figure 1.11 — The Telnet attempt is closed by the router without providing a login session.**

![Admin-PC command prompt showing telnet 192.168.16.1 opening and then closing without a login prompt](./screenshots/figure-1-11-telnet-rejected.png)

### Evidence of EIGRP Operation

**Figure 1.12 — EIGRP neighbor 10.0.0.1 is established; both networks are included and the LAN interface is passive.**

![SEA-R01 output of show ip eigrp neighbors and show ip protocols listing neighbor 10.0.0.1, both networks and the passive LAN interface](./screenshots/figure-1-12-eigrp-neighbor-protocols.png)

### Evidence of Learned Route and Return Traffic

**Figure 1.13 — WAN-R02 learns 192.168.16.0/23 through EIGRP via 10.0.0.2.**

![WAN-R02 show ip route output with a D route for 192.168.16.0/23 via 10.0.0.2](./screenshots/figure-1-13-wan-r02-learned-route.png)

**Figure 1.14 — WAN-R02 reaches the LAN PC using the learned route with 5/5 ping replies.**

![WAN-R02 ping to 192.168.17.10 with a 100 percent success rate](./screenshots/figure-1-14-wan-r02-ping-pc.png)

### Evidence of Required Static Route

The installed /24 satisfies the literal command interpretation. Its overlap with the connected /23 is documented in the technical analysis.

**Figure 1.15 — SEA-R01 installs the assignment static /24 alongside the overlapping connected /23.**

![SEA-R01 show ip route output with the connected 192.168.16.0/23 and the static 192.168.16.0/24 via 10.0.0.1](./screenshots/figure-1-15-static-route-overlap.png)

### Evidence of Final PC Connectivity

**Figure 1.16 — Admin PC reaches the LAN gateway and WAN peer with 4/4 replies and 0% loss for each.**

![Admin-PC command prompt with successful pings to 192.168.16.1 and 10.0.0.1](./screenshots/figure-1-16-pc-final-pings.png)

### Evidence of Configuration Saving

**Figure 1.17 — SEA-R01 saves its running configuration to startup configuration with an OK confirmation.**

![SEA-R01 copy running-config startup-config output ending in OK](./screenshots/figure-1-17-sea-r01-save-config.png)

**Figure 1.18 — WAN-R02 saves its running configuration to startup configuration with an OK confirmation.**

![WAN-R02 copy running-config startup-config output ending in OK](./screenshots/figure-1-18-wan-r02-save-config.png)

### Evidence of Final Topology

**Figure 1.19 — Final topology shows green link indicators between all four devices.**

![Packet Tracer topology of Admin-PC, LAN-SW01, SEA-R01 and WAN-R02 with all links green](./screenshots/figure-1-19-final-topology.png)

## Final SEA-R01 Running Configuration

Captured after configuration and save verification. The output below preserves the supplied running configuration, including IOS separator lines.

```
SEA-R01#show running-config
Building configuration...
Current configuration : 1344 bytes
!
version 15.1
no service timestamps log datetime msec
no service timestamps debug datetime msec
service password-encryption
!
hostname SEA-R01
!
!
!
enable secret 5 $1$mERr$vZNpuir0bCjVU7HUaCqW8.
!
!
!
!
!
!
ip cef
ipv6 unicast-routing
!
no ipv6 cef
!
!
!
username admin secret 5 $1$mERr$mFGr.HZHSHlB0ulUXLjNi1
!
!
license udi pid CISCO2911/K9 sn FTX1524YKNP-
!
!
!
!
!
!
!
!
!
!
!
ip ssh version 2
no ip domain-lookup
ip domain-name abc.example
ip name-server 8.8.8.8
!
!
spanning-tree mode pvst
!
!
!
!
!
!
interface GigabitEthernet0/0
description LAN connection to LAN-SW01
ip address 192.168.16.1 255.255.254.0
duplex auto
speed auto
!
interface GigabitEthernet0/1
description WAN connection to WAN-R02
ip address 10.0.0.2 255.255.255.252
duplex auto
speed auto
ipv6 address 2001:DB8:A0B:12F0::1/64
!
interface GigabitEthernet0/2
no ip address
duplex auto
speed auto
shutdown
!
interface Vlan1
no ip address
shutdown
!
router eigrp 100
passive-interface GigabitEthernet0/0
network 192.168.16.0 0.0.1.255
network 10.0.0.0 0.0.0.3
!
ip classless
ip route 192.168.16.0 255.255.255.0 10.0.0.1
!
ip flow-export version 9
!
!
!
!
!
!
!
line con 0
password 7 0828781A5049113A1318030A60
logging synchronous
login
!
line aux 0
!
line vty 0 4
password 7 0828781A5049113A1318030A60
login local
transport input ssh
!
!
!
end
```

## Final WAN-R02 Running Configuration

Captured after configuration and save verification. The output below preserves the supplied running configuration, including IOS separator lines.

```
WAN-R02#show running-config
Building configuration...
Current configuration : 871 bytes
!
version 15.1
no service timestamps log datetime msec
no service timestamps debug datetime msec
no service password-encryption
!
hostname WAN-R02
!
!
!
!
!
!
!
!
ip cef
ipv6 unicast-routing
!
no ipv6 cef
!
!
!
!
license udi pid CISCO2911/K9 sn FTX1524AZIU-
!
!
!
!
!
!
!
!
!
!
!
no ip domain-lookup
!
!
spanning-tree mode pvst
!
!
!
!
!
!
interface GigabitEthernet0/0
description WAN connection to SEA-R01
ip address 10.0.0.1 255.255.255.252
duplex auto
speed auto
ipv6 address 2001:DB8:A0B:12F0::2/64
!
interface GigabitEthernet0/1
no ip address
duplex auto
speed auto
shutdown
!
interface GigabitEthernet0/2
no ip address
duplex auto
speed auto
shutdown
!
interface Vlan1
no ip address
shutdown
!
router eigrp 100
network 10.0.0.0 0.0.0.3
!
ip classless
!
ip flow-export version 9
!
!
!
!
!
!
!
line con 0
!
line aux 0
!
line vty 0 4
login
!
!
!
end
```

## References

Cisco. (2011, April 21). Configuring EIGRP. Cisco IOS 15.0S. https://www.cisco.com/en/US/docs/ios-xml/ios/iproute_eigrp/configuration/15-0s/Configuring_EIGRP.html

Cisco. (2024a, January 17). Configure route selection for routers. https://www.cisco.com/c/en/us/support/docs/ip/enhanced-interior-gateway-routing-protocol-eigrp/8651-21.html

Cisco. (2024b, July 22). Understand Cisco IOS password encryption. https://www.cisco.com/c/en/us/support/docs/security-vpn/remote-authentication-dial-user-service-radius/107614-64.html

Cisco. (2026, July 30). Configure SSH on routers. https://www.cisco.com/c/en/us/support/docs/security-vpn/secure-shell-ssh/4145-ssh.html

Lab evidence consists of the Packet Tracer screenshots and final router configurations captured on October 4, 2026.

## Outcome

I configured SEA-R01 from a new router state with a /23 LAN sized for 270 hosts, an IPv4 and IPv6 WAN link, SSH-only management and EIGRP, then verified each requirement with CLI and PC tests. I documented 19 figures of evidence and saved both router configurations. I also traced how the required static /24 overlaps the connected /23 and explained why it could cause a routing loop for part of the LAN.
