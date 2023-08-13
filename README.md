# DNS Spoofing Tool

The DNS Spoofing Tool is a Python script that uses Scapy and NetfilterQueue to intercept and spoof DNS responses, redirecting a target website to a specified IP address. This tool can be used for educational purposes to demonstrate DNS spoofing and its implications.

## Requirements

- Python 3.x
- Scapy
- NetfilterQueue

## Installation

1. Clone or download the repository to your local machine.

2. Install the required dependencies using pip:

```sh
pip install scapy netfilterqueue
```

## Usage

1. Open a terminal and navigate to the directory containing the `dns_spoof.py` script.

2. Run the script as root (administrator) using the following command:

```sh
sudo python3 dns_spoof.py target new_ip
```

Replace `target` with the website you want to spoof (e.g., www.bing.com) and `new_ip` with the IP address you want to redirect the target website to.

3. The script will intercept DNS responses and spoof the target website, redirecting it to the specified IP address.

4. To stop the DNS spoofing, press `Ctrl+C` in the terminal.

## Example

To spoof the website "www.example.com" and redirect it to the IP address "10.0.2.15", run the following command:

```sh
sudo python3 dns_spoof.py www.example.com 10.0.2.15
```

## Important Notes

- This tool is for educational and research purposes only. Do not use it for malicious activities.
- DNS spoofing can disrupt network communication and potentially lead to security vulnerabilities.
- Ensure you have proper authorization before using this tool on any network.

## Disclaimer

This tool is provided for educational and research purposes only. The author shall not be held responsible for any misuse or illegal activities conducted using this tool.
