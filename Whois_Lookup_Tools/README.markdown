# Domain WHOIS Registrar Lookup

This project provides two Python scripts to retrieve WHOIS registrar information for domain names, using the `python-whois` library. The scripts allow users to query domain registrar details either via command-line arguments or a text file.

## Features
- **Ex1_Normal_Whois.py**: A basic script that accepts domain names as command-line arguments and returns their registrar information.
- **Ex1_Intermediate_Whois.py**: An enhanced version that supports both command-line arguments and reading domains from a `domains.txt` file, with rate limiting to avoid WHOIS server blocks.
- **domains.txt**: A sample file containing a list of domains for testing the intermediate script.

## Requirements
- Python 3.x
- `python-whois` library (`pip install python-whois`)

## Installation
1. Clone this repository:
   ```bash
   git clone https://github.com/<your-username>/domain-whois-lookup.git
   cd domain-whois-lookup
   ```
2. Install the required library:
   ```bash
   pip install python-whois
   ```

## Usage

### Ex1_Normal_Whois.py
Run the script with domain names as command-line arguments:
```bash
python Ex1_Normal_Whois.py google.com yahoo.com
```
**Output**:
```
Domain name: google.com | Registrar: MarkMonitor Inc.
Domain name: yahoo.com | Registrar: MarkMonitor Inc.
```

### Ex1_Intermediate_Whois.py
Run with command-line arguments:
```bash
python Ex1_Intermediate_Whois.py google.com yahoo.com
```
Or, use the `domains.txt` file:
```bash
python Ex1_Intermediate_Whois.py
```
**Output** (using `domains.txt`):
```
Domain: google.com | Registrar: MarkMonitor Inc.
Domain: openai.com | Registrar: NameCheap, Inc.
Domain: yahoo.com | Registrar: MarkMonitor Inc.
Domain: nic.uk | Registrar: Not found
Domain: apple.com | Registrar: CSC Corporate Domains, Inc.
Domain: vietnamairlines.com | Registrar: GoDaddy.com, LLC
```

### domains.txt
The `domains.txt` file contains a list of domains, one per line. Lines starting with `#` or empty lines are ignored. Example:
```
google.com
openai.com
yahoo.com
nic.uk
apple.com
vietnamairlines.com
```

## Notes
- The intermediate script includes a 1-second delay between WHOIS queries to prevent rate-limiting by WHOIS servers.
- Some WHOIS servers may return incomplete data or block excessive queries. Adjust the `time.sleep(1)` value in `Ex1_Intermediate_Whois.py` if needed.
- Ensure a stable internet connection, as the scripts rely on WHOIS server responses.

## License
This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.

## Contributing
Feel free to submit issues or pull requests for improvements, such as adding error handling, supporting additional WHOIS fields, or optimizing performance.