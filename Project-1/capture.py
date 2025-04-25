#!/usr/bin/env python3
# coding=utf-8
"""Basic network capture, loader, and summarizer"""

# Using sniff, wrpcap, rdpcap for packet analysis
from scapy.all import sniff, wrpcap, rdpcap
from scapy.layers.inet import IP, TCP, UDP

def capture_packets(count=20, iface=None, filter_expr=None):
    """
    Handles the capturing of packets and returning of info.

    Args:
        count: The number of packets captured before ending. Defaults to 20
        iface: The interface which the network capture is on. Default is None (chosen by scapy)
        filter_expr: Packet filter on criteria. Default is None (All packets)
    """
    # Utilizes sniff library to capture packets and returns with wrpcap
    packets = sniff(count=count, iface=iface, filter=filter_expr)
    wrpcap("capture.pcap", packets)
    return packets

def load_packets(file_path="capture.pcap"):
    """
    Purpose is to load packets in a pcap file.

    Args:
        file_path: Determines where the pcap file is. Default is capture.pcap
    """
    return rdpcap(file_path)

def summarize_packets(packets, protocol_filter=None):
    """
    Handles the Scapy packet objects and generates a summary for each packet.

    Args:
        packets: Packet list that it reads from.
        protocol_filter: Filters the summary to show only specific protocols. Default is None (All packets)
    """

    # Loops within the packet list and summarizes the info
    summary = []
    for pkt in packets:
        if IP in pkt:
            proto = pkt.getlayer(IP).proto
            proto_name = {6: "TCP", 17: "UDP"}.get(proto, "OTHER")
            if protocol_filter and proto_name != protocol_filter:
                continue
            summary.append({
                "src": pkt[IP].src,
                "dst": pkt[IP].dst,
                "proto": proto_name,
                "summary": pkt.summary()
            })
    return summary