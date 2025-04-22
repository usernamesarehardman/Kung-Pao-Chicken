from scapy.all import sniff, wrpcap, rdpcap
from scapy.layers.inet import IP, TCP, UDP

def capture_packets(count=20, iface=None, filter_expr=None):
    packets = sniff(count=count, iface=iface, filter=filter_expr)
    wrpcap("capture.pcap", packets)
    return packets

def load_packets(file_path="capture.pcap"):
    return rdpcap(file_path)

def summarize_packets(packets, protocol_filter=None):
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