from flask import Flask, render_template, request, redirect
from capture import capture_packets, load_packets, summarize_packets

app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def index():
    packet_data = []
    if request.method == "POST":
        action = request.form.get("action")
        if action == "capture":
            protocol = request.form.get("protocol")
            filter_expr = None
            if protocol == "tcp":
                filter_expr = "tcp"
            elif protocol == "udp":
                filter_expr = "udp"
            packets = capture_packets(count=20, filter_expr=filter_expr)
            packet_data = summarize_packets(packets, protocol_filter=protocol.upper() if protocol else None)
        elif action == "load":
            packets = load_packets()
            packet_data = summarize_packets(packets)
    return render_template("index.html", packets=packet_data)

if __name__ == "__main__":
    app.run(debug=True)