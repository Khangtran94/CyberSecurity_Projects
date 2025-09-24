import psycopg2
import os 
import json 

class APIKeyStorageDB:
    def __init__(self, dbname, user, password, host="localhost", port=5432):
        self.conn = psycopg2.connect(
            dbname=dbname,
            user=user,
            password=password,
            host=host,
            port=port
        )
        self.cursor = self.conn.cursor()
        self._create_table()

    def _create_table(self):
        self.cursor.execute("""
            CREATE TABLE IF NOT EXISTS api_keys (
                service_name VARCHAR(255) PRIMARY KEY,
                api_key TEXT NOT NULL
            );
        """)
        self.conn.commit()

    #### Store an API key ####
    def store(self, service_name, api_key):
        service_lower = service_name.lower()
        if self.retrieve(service_name) != 'No API key found for this service.':
            return False  # Already exists
        self.cursor.execute(
            "INSERT INTO api_keys (service_name, api_key) VALUES (%s, %s)",
            (service_lower, api_key)
        )
        self.conn.commit()
        return True

    #### Retrieve an API key ####
    def retrieve(self, service_name):
        service_lower = service_name.lower()
        self.cursor.execute(
            "SELECT api_key FROM api_keys WHERE service_name = %s",
            (service_lower,)
        )
        result = self.cursor.fetchone()
        if result:
            return result[0]
        return 'No API key found for this service.'

    #### Close connection ####
    def close(self):
        self.cursor.close()
        self.conn.close()

def main():
    print("API Key Storage System (PostgreSQL)")
    
    # PostgreSQL connection info
    storage = APIKeyStorageDB(
        dbname="API_Keys_DB",
        user="Khang_Cyber",
        password="Cyber_is_FUN",
        host="localhost",
        port=5432
    )

    while True:
        print("\nOptions:")
        print("1. Store API Key")
        print("2. Retrieve API Key")
        print("3. Exit")

        option = input("Enter choice: ").strip()

        if option == "1":
            service = input("Enter Service Name: ").strip()
            if storage.retrieve(service) != 'No API key found for this service.':
                print(f"{service.capitalize()} is already registered API key.")
            else:
                key = input("Enter API Key: ").strip()
                storage.store(service, key)
                print("API Key stored successfully.")
        elif option == "2":
            service = input("Enter Service Name: ").strip()
            api_key = storage.retrieve(service)
            if api_key == 'No API key found for this service.':
                print(f"{service.capitalize()}: {api_key}")
            else:
                print(f"=> API Key of {service.capitalize()} Service Name: {api_key}")
        elif option == "3":
            print("Exiting...")
            storage.close()
            break
        else:
            print("Invalid choice. Try again.")

if __name__ == "__main__":
    main()
