# Academic Coursework

Selected assignments from my bachelor's degree in cybersecurity at Green River College. Each assignment folder holds the final submitted file, a PDF copy, and a README with the full text of the assignment. The scenarios are fictional (Company ABC, Gatorware Software), and all IP addresses are documentation or private ranges.

Word (.docx) and PowerPoint (.pptx) files open in Microsoft Office. Discussion posts are saved as .html files and open in any browser. Every assignment also has a PDF.

## IT490 Capstone - Cybersecurity & Networking

[Class overview](IT490%20Capstone%20-%20Cybersecurity%20%26%20Networking/)

| Week | Assignment | What it covers | File |
| --- | --- | --- | --- |
| 1 | [Company ABC Network Design](IT490%20Capstone%20-%20Cybersecurity%20%26%20Networking/week1-network-design-wan-security/) | Hub-and-spoke IKEv2/IPsec WAN, /23 subnet correction, VLAN segmentation, default-deny firewall policy | Report |
| 2 | [Basic Cisco Router Setup](IT490%20Capstone%20-%20Cybersecurity%20%26%20Networking/week2-cisco-router-setup/) | SEA-R01 build from scratch in Packet Tracer: /23 LAN sizing, IPv6 WAN, SSH-only access, EIGRP, static route overlap analysis | Report |
| 3 | [Host-to-Host Email Encryption](IT490%20Capstone%20-%20Cybersecurity%20%26%20Networking/week3-email-encryption-purview/) | Microsoft Purview Message Encryption, mail flow rules, forced-TLS partner connector, HIPAA considerations | Report |
| 4 | [NIST IR 8228 (IoT)](IT490%20Capstone%20-%20Cybersecurity%20%26%20Networking/week4-nist-ir-8228-iot/) | Managing IoT cybersecurity and privacy risks, applied to Company ABC cameras and badge readers | Presentation |
| 4 | [Palo Alto Firewall Setup](IT490%20Capstone%20-%20Cybersecurity%20%26%20Networking/week4-palo-alto-firewall/) | PA-440 baseline: blocking a probe source, port lockdown, DNS restricted to domain controllers, validation plan | Report |
| 4 | [SonicWall Site-to-Site VPN](IT490%20Capstone%20-%20Cybersecurity%20%26%20Networking/week4-sonicwall-vpn-discussion/) | TZ370 IKEv2 VPN between Seattle and Denver, explicit access rules | Discussion post |
| 4 | [WatchGuard BOVPN](IT490%20Capstone%20-%20Cybersecurity%20%26%20Networking/watchguard-bovpn-discussion/) | Firebox T45 branch office VPN with Phase 1 and Phase 2 settings and access policies | Discussion post |
| 5 | [Cisco Config Checker](IT490%20Capstone%20-%20Cybersecurity%20%26%20Networking/week5-cisco-config-checker-python/) | Python and Netmiko script that audits SSH and VTY settings on routers and Layer 3 switches | Script and discussion post |
| 5 | [ISO/IEC 27002](IT490%20Capstone%20-%20Cybersecurity%20%26%20Networking/week5-iso-27002/) | The 2013 control set and how Company ABC can apply it | Presentation |
| 5 | [Ports, Services and Five Tuples](IT490%20Capstone%20-%20Cybersecurity%20%26%20Networking/week5-ports-services-five-tuples/) | Service ports and request/response five tuples for LAN, DMZ and VPN remote desktop traffic | Report |
| – | [certutil.exe LOLBin Detection](IT490%20Capstone%20-%20Cybersecurity%20%26%20Networking/certutil-lolbin-detection/) | Living-off-the-land abuse of certutil and how I would detect it with Event ID 4688 | Discussion post |

## IT295 CompTIA Project+ Cert Prep

[Class overview](IT295%20CompTIA%20Project%2B%20Cert%20Prep/)

| Module | Assignment | What it covers | File |
| --- | --- | --- | --- |
| 1 | [Research Project](IT295%20CompTIA%20Project%2B%20Cert%20Prep/module1-research-docker-kubernetes-github-slack/) | Docker, Kubernetes, GitHub and Slack: purpose, producer, deployment and SaaS role | Report |
| 3 | [Gatorware Business Case](IT295%20CompTIA%20Project%2B%20Cert%20Prep/module3-business-case-gatorware/) | Business case for a cloud and SaaS modernization, with security, adoption and skills risk analysis | Report |
| 4 | [Key Deliverables and Methodologies](IT295%20CompTIA%20Project%2B%20Cert%20Prep/module4-deliverables-and-methodologies/) | Deliverables for the Gatorware upgrade, plus Waterfall, Agile and hybrid selections | Report |
| 5 | [WBS Lab](IT295%20CompTIA%20Project%2B%20Cert%20Prep/module5-wbs-critical-path-lab/) | Critical path analysis, what-if scenarios and a Gantt chart | Lab |

## Running the config checker

The script in [`IT490 Capstone - Cybersecurity & Networking/week5-cisco-config-checker-python/`](IT490%20Capstone%20-%20Cybersecurity%20%26%20Networking/week5-cisco-config-checker-python/) needs Python 3 and Netmiko (`python3 -m pip install netmiko`). Replace the example inventory with real device addresses, and test it in a lab first. It only reads configurations and makes no changes.
