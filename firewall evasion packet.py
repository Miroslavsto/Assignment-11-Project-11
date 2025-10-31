from scapy.all import IP, TCP, send

# Define the IP layer with the target IP
ip_layer = IP(dst="52.234.30.228")

# Define the TCP layer with spoofed source port and SYN flag
tcp_layer = TCP(dport=80, sport=12345, flags="S")

# Define a custom HTTP GET payload with a suspicious header
http_payload = (
    "GET /index.html HTTP/1.1\r\n"
    "Host: 52.234.30.228\r\n"
    "User-Agent: ScapyTest/1.0\r\n"
    "Accept: */*\r\n"
    "Custom-Payload: This is a payload that may contain malicious code\r\n"
    "\r\n"
)

# Combine layers and send the packet
packet = ip_layer / tcp_layer / http_payload
send(packet)

print("Malicious packet sent.")
