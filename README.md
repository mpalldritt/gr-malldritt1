# gr-malldritt1 — Acoustic SDR Flow Graphs (FSK / PSK)

This repository contains GNU Radio software-defined radio (SDR) flow graphs,
supporting scripts, and example outputs used in the experimental evaluation
of acoustic digital communication systems described in the associated journal
publication.

The materials provided here enable replication and verification of the
modulation, transmission, and reception techniques reported in the paper.

---

## Overview

The repository includes packet-based **BFSK** and **BPSK** modulation flow graphs
implemented using GNU Radio Companion (GRC). These flow graphs were developed
and tested for acoustic communication experiments in challenging propagation
environments, including highly reflective and multipath media.

The experiments focus on:
- Packet-based transmission and reception
- Baseband and passband signal analysis
- Constellation, spectrum, and correlation visualisation
- Operation around a 40 kHz acoustic carrier

---

## Software Environment

- GNU Radio: **3.10.10**
- Operating System: **Windows 11**
- Audio interface: Sound-card based (192 kHz sample rate)

---

## Repository Structure
```
gr-malldritt1/
├── flowgraphs/
│ ├── fsk/
│ │ ├── tx/ # BFSK transmitter flow graphs
│ │ ├── rx/ # BFSK receiver flow graphs
│ │ └── figures/ # Example TX/RX display outputs
│ └── psk/
│ ├── versions/ # Versioned BPSK flow graphs (dated)
│ └── figures/ # Constellation and spectrum plots
├── docs/
│ └── experiment_notes.md
└── images/
```
