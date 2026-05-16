from scapy.all import sniff
from scapy.layers.inet import IP

# Function to process packets
def process_packet(packet):

    # Check if packet has IP layer
    if packet.haslayer(IP):

        print("\n===== Packet Captured =====")

        print("Source IP:", packet[IP].src)

        print("Destination IP:", packet[IP].dst)

        print("Protocol:", packet[IP].proto)

# Main function
def main():

    print("Starting Basic Network Sniffer...")
    print("Press CTRL + C to stop.\n")

    sniff(prn=process_packet, store=False)

# Run program
if __name__ == "__main__":
    main()
    