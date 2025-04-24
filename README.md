# Pseudo-Wireshark

A simplified network packet analyzer built with Python, Scapy, and Flask, intended for educational purposes in network forensics. It captures live packets, allows filtering (e.g., TCP/UDP), and displays basic packet metadata through a web interface styled with Bootstrap.

## Features

- Capture live network traffic
- Save to and load from .pcap files
- Filter by TCP or UDP
- Web interface built with Flask and Bootstrap
- Simple and lightweight

## Getting Started

### Prerequisites

- Python 3.7+
- Admin/root privileges (for packet capture)

### Installation

    git clone https://github.com/yourusername/pseudo-wireshark.git
    cd pseudo-wireshark
    pip install -r requirements.txt

### Run the App

    # On Unix/Linux/macOS (requires sudo for packet capture)
    sudo python app.py

    # On Windows (run with admin privileges)
    python app.py

Then visit http://localhost:5000 in your browser.

## File Structure

    pseudo-wireshark/
    ├── app.py                 # Flask app
    ├── capture.py             # Scapy logic
    ├── requirements.txt       # Python dependencies
    ├── .gitignore             # Common ignored files
    ├── templates/
    │   └── index.html         # Main web page (Bootstrap)
    └── static/
        └── (Optional assets)

## Notes

- Only the first 20 packets are captured by default (modifiable in capture_packets()).
- Scapy may trigger antivirus or firewall warnings.
- For demo purposes, this app does not include HTTPS or authentication.

## License

MIT License
