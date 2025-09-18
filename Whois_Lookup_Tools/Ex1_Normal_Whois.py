import sys
import whois

### Get WHOIS Registrar Information for Multiple Domains
def get_whois_registrar(domain):
    try:
        w = whois.whois(domain)
        return "Domain name: " + str(domain) + " | Registrar: " + str(w.registrar)
    except Exception as e:
        return f"Error retrieving WHOIS data: {e}"

### Main function to handle command-line arguments    
def main():
    if len(sys.argv) < 2:
        sys.exit(1)
    
    domains = sys.argv[1:]
    for domain in domains:
        result = get_whois_registrar(domain)
        print(result)
        
if __name__ == "__main__":
    main()
    
    