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



`BPSK and BFSK Flow graph modulation updated on 18/12/2025

GRC BFSK and BPSK software, tested on Windows 11 laptop with radiocanda and GNU Radio 3.10.10


gr-malldritt1 PSK
PSK Baseband, Constellation and IO Correlation Graphs.jpg	          PSK Display Graphs using this GRC software
PSK Passband RX Spectrum and Output bandwidth centered at 40khz.jpg	PSK Display Graphs using this GRC software
PSK Passband TX Spectrum and Transmit Data.jpg	                    PSK Display Graphs using this GRC software
pkt_xmt_rcv_ma_16122025.grc	                                        PSK modulation protocol
pkt_xmt_rcv_ma_16122025.pdf	                                        PSK modulation protocol
pkt_xmt_rcv_ma_16122025.py	                                        PSK modulation protocol
pkt_xmt_rcv_ma_18122025.grc	                                        PSK modulation protocol updated flowgraph
pkt_xmt_rcv_ma_18122025.pdf	                                        PSK modulation protocol updated flowgraph
pkt_xmt_rcv_ma_18122025.py	                                        PSK modulation protocol updated flowgraph
pkt_xmt_rcv_ma_19122025.grc	                                        PSK modulation protocol updated flowgraph final
pkt_xmt_rcv_ma_19122025.pdf	                                        PSK modulation protocol updated flowgraph final
pkt_xmt_rcv_ma_19122025.py	                                        PSK modulation protocol updated flowgraph final
Baseband graph and Constellation 19122025.jpg		                    PSK modulation protocol updated flowgraph final
		
 
gr-malldritt1 FSK
RX display graph.jpg	    FSK Display Graphs using this GRC software
TX display graph.jpg	    FSK Display Graphs using this GRC software
pkt_fsk_rcv.grc	          FSK modulation protocol
pkt_fsk_rcv.pdf	          FSK modulation protocol
pkt_fsk_rcv.py	          FSK modulation protocol
pkt_fsk_rcv_26112025.jpg	FSK Display Graphs using this GRC software
pkt_fsk_xmt.grc	          FSK modulation protocol
pkt_fsk_xmt.pdf	          FSK modulation protocol
pkt_fsk_xmt.py	          FSK modulation protocol
pkt_fsk_xmt_26112025.jpg	FSK Display Graphs using this GRC software

gr-malldritt/
├── README.md
├── flowgraphs/
│   ├── fsk/
│   │   ├── tx/
│   │   │   ├── pkt_fsk_xmt.grc
│   │   │   ├── pkt_fsk_xmt.py
│   │   │   └── pkt_fsk_xmt.pdf
│   │   ├── rx/
│   │   │   ├── pkt_fsk_rcv.grc
│   │   │   ├── pkt_fsk_rcv.py
│   │   │   └── pkt_fsk_rcv.pdf
│   │   └── figures/
│   │       ├── TX_display_graph.jpg
│   │       └── RX_display_graph.jpg
│   ├── psk/
│   │   ├── versions/
│   │   │   ├── 16122025/
│   │   │   ├── 18122025/
│   │   │   └── 19122025_final/
│   │   └── figures/
│   │       ├── constellation.jpg
│   │       └── spectrum.jpg
├── images/
│   └── README_figures/
├── docs/
│   └── experiment_notes.md
`
