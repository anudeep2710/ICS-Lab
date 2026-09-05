# ICS Security Lab

## Contents
- [Overview](#overview)
- [Architecture](#architecture)
- [Features](#features)
- [Tech Stack](#tech-stack)
- [Key Findings](#key-findings)
- [Screenshots](#screenshots)
- [How to Run](#how-to-run)
- [Future Improvements](#future-improvements)

---

## Overview

ICS Security Lab is a simulated Industrial Control System (ICS) cybersecurity environment designed to model Operational Technology (OT) networks using a simplified Purdue Model architecture.

The lab uses pfSense to segment Level 1–3 assets into separate security zones and enforces controlled communication paths between the HMI and PLC networks. Industrial traffic is generated using Modbus/TCP and analyzed with Wireshark, Zeek, and Suricata to demonstrate how common OT protocols can be monitored and secured.

This project highlights key OT security concepts including network segmentation, protocol visibility, intrusion detection, and compensating controls for inherently insecure industrial protocols.

---

## Architecture

### Purdue Model Zones

- **Level 3:** Operations / Management Workstation
- **Level 2:** SCADA / HMI Workstation
- **Level 1:** PLC / Controller Simulation
- **Level 0:** Simulated Process Values
- **Monitoring Zone:** Security Monitoring and IDS

### Network Layout

- **Level 3:** `10.10.3.0/24`
- **Level 2 (HMI):** `10.10.2.0/24`
- **Level 1 (PLC):** `10.10.1.0/24`

### Security Controls

- Default deny between zones
- Allow HMI → PLC on Modbus/TCP
- Allow administrative SSH access only where required
- Block unauthorized inter-zone traffic
- Suricata rules to detect Modbus write operations

---

## Features

- Simulated ICS environment based on the Purdue Model
- pfSense firewall segmentation between Level 1–3 networks
- Modbus/TCP server and client for industrial traffic generation
- Wireshark packet inspection
- Zeek network metadata collection
- Suricata intrusion detection with custom Modbus rules
- Security assessment of Modbus/TCP and OPC UA
- Validation of allowed and blocked communication paths

---

## Tech Stack

- VirtualBox
- pfSense
- Ubuntu Server
- Python
- Wireshark
- Zeek
- Suricata
- Modbus/TCP
- OPC UA

---

## Key Findings

- Modbus/TCP communications were transmitted in plaintext and could be fully inspected in packet captures.
- Firewall segmentation prevented unauthorized direct communication between OT zones.
- Suricata detected Modbus Function Code 6 (Write Single Register) using a custom protocol-aware rule.
- Zeek `conn.log` provided visibility into allowed and denied connections across segmented networks.
- OT protocols require compensating controls such as segmentation and monitoring because many lack native security.

---

## Screenshots

### Architecture
- Purdue Model network diagram
- VirtualBox network configuration

### Segmentation
- pfSense interface assignments
- Firewall rules allowing HMI → PLC communication
- Blocked connection attempts

### Monitoring
- Wireshark Modbus packet capture
- Zeek `conn.log`
- Suricata alert for Modbus write activity

---

## How to Run

1. Create four virtual machines:
   - pfSense firewall/router
   - HMI workstation
   - PLC simulation server
   - Monitoring server

2. Configure internal networks:
   - `10.10.3.0/24` (Level 3)
   - `10.10.2.0/24` (HMI)
   - `10.10.1.0/24` (PLC)

3. Configure pfSense interfaces and firewall rules.

4. Deploy a Modbus/TCP server on the PLC VM.

5. Run a Python-based Modbus client from the HMI VM.

6. Capture traffic with Wireshark.

7. Monitor connections with Zeek.

8. Detect suspicious activity with Suricata.

---

## Future Improvements

- Deploy a real OPC UA server and client
- Integrate logs into Splunk or the ELK Stack
- Map findings to ISA/IEC 62443 controls
- Simulate ransomware or unauthorized engineering workstation access
- Add historian and engineering workstation components
