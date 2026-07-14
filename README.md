# BGP & OSPF Peering Builder

## Overview

The **BGP & OSPF Peering Builder** is a beginner-friendly Python automation tool that generates Cisco IOS routing configurations. It simplifies the process of creating BGP neighbor relationships and OSPF network advertisements by prompting the user for a few inputs and automatically generating the required configuration.

This project is intended for students, network engineers, and cloud networking professionals who want to learn routing concepts or quickly build lab configurations.

## Features

* Generate Cisco BGP configurations
* Generate Cisco OSPF configurations
* Automatically create multiple BGP neighbor statements
* Automatically generate sequential neighbor IP addresses
* Support for eBGP and iBGP deployments
* Create multiple OSPF network statements
* Save generated configurations to a text file
* Beginner-friendly command-line interface

## Technologies

* Python 3
* Cisco IOS Routing
* BGP
* OSPF

## Example Output

### BGP

```text
router bgp 65001
 bgp log-neighbor-changes
 neighbor 10.0.0.2 remote-as 65002
 neighbor 10.0.0.3 remote-as 65003
 neighbor 10.0.0.4 remote-as 65004
```

### OSPF

```text
router ospf 1
 router-id 1.1.1.1
 network 10.0.12.0 0.0.0.3 area 0
 network 10.0.13.0 0.0.0.3 area 0
 network 10.0.14.0 0.0.0.3 area 0
```

## How to Run

1. Clone the repository.
2. Open the project in Visual Studio Code.
3. Run the script:

```bash
python3 bgp_ospf_peering_builder.py
```

4. Choose either **BGP** or **OSPF**.
5. Enter the requested values.
6. Review or save the generated configuration.

## Project Purpose

This project demonstrates Python automation for network engineering by reducing manual configuration tasks and generating consistent routing configurations. It serves as a practical portfolio project showcasing Python programming, Cisco networking fundamentals, and infrastructure automation.
