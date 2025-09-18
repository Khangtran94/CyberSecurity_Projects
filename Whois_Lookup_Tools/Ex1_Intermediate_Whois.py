import sys
import whois
import time

### Load domains from file if no CLI args
def load_domains_from_file(path="domains.txt"):
    try:
        with open(path, "r") as file:
            return [line.strip() for line in file if line.strip() and not line.startswith("#")]
    except FileNotFoundError:
        return []

### Get WHOIS Registrar Information for a domain
def get_whois_registrar(domain):
    try:
        w = whois.whois(domain)

        registrar = w.registrar
        if isinstance(registrar, list):  # Sometimes python-whois returns a list
            registrar = ", ".join(registrar)

        if not registrar:
            return f"Domain: {domain} | Registrar: Not found"
        return f"Domain: {domain} | Registrar: {registrar}"
    except Exception as e:
        return f"Domain: {domain} | Error: {e}"

### Main function
def main():
    if len(sys.argv) > 1:
        domains = sys.argv[1:]  # CLI input
    else:
        domains = load_domains_from_file()
        if not domains:
            print("Or provide a domains.txt file")
            sys.exit(1)

    for domain in domains:
        result = get_whois_registrar(domain)
        print(result)
        time.sleep(1)  # Simple rate limiting to avoid being blocked

if __name__ == "__main__":
    main()
