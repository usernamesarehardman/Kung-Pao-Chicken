#!/usr/bin/env python3
# coding=utf-8
"""Simple web applicationto capture and load network packet files into web browser"""

# Importing Flask for web app and capture.py for network packet access
from flask import Flask, render_template, request, redirect
from capture import capture_packets, load_packets, summarize_packets

# Initialize Flask App
app = Flask(__name__)

# Define Route for GET to see page and POST to send info (load packets)
@app.route("/", methods=["GET", "POST"])


def index():
    """
    This is the standard page for where the user is navigated
    """

    # Creates array of packet data to save
    packet_data = []

    # Actions that user can do, such as input a packet to summarize or to capture packets
    if request.method == "POST":
        action = request.form.get("action")

        # Packet capture option
        if action == "capture":
            protocol = request.form.get("protocol")
            filter_expr = None

            # Filter options
            if protocol == "tcp":
                filter_expr = "tcp"
            elif protocol == "udp":
                filter_expr = "udp"

            # Runs Packet capture
            packets = capture_packets(count=20, filter_expr=filter_expr)
            packet_data = summarize_packets(packets, protocol_filter=protocol.upper() if protocol else None)
        
        # Loading packet option
        elif action == "load":
            packets = load_packets()
            packet_data = summarize_packets(packets)
    return render_template("index.html", packets=packet_data)

if __name__ == "__main__":
    app.run(debug=True)