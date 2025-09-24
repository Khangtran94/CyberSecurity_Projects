import os
import json

#### Class to manage API keys securely, default is in-memory storage ####
class APIKeyStorage:
    def __init__(self, storage_type="memory", filename="apikeys.json"):
        self.storage_type = storage_type
        self.filename = filename
        self.memory_store = {}

        if self.storage_type == "file":
            if os.path.exists(self.filename):
                with open(self.filename, "r") as f:
                    try:
                        self.memory_store = json.load(f)
                    except json.JSONDecodeError:
                        self.memory_store = {}
            else:
                self._save_to_file()
                
    def _save_to_file(self):
        with open(self.filename, "w") as f:
            json.dump(self.memory_store, f)
            
    #### Store an API key ####
    def store(self, service_name, api_key):
        key = service_name.lower()
        if key in self.memory_store:
            return False  # Service already exists
        self.memory_store[key] = api_key
        if self.storage_type == "file":
            self._save_to_file()
        return True  # Successfully stored

    #### Retrieve an API key ####
    def retrieve(self, service_name):
        return self.memory_store.get(service_name.lower(), 'No API key found for this service.')
    
def main():
    print("API Key Storage System")
    print("Choose storage type:")
    print("1. In-Memory (temporary)")
    print("2. File (persistent)")
    
    choice = input("Enter choice (1/2): ").strip()
    storage_type = "memory" if choice == "1" else "file"

    storage = APIKeyStorage(storage_type=storage_type)

    while True:
        print("\nOptions:")
        print("1. Store API Key")
        print("2. Retrieve API Key")
        print("3. Exit")

        option = input("Enter choice: ").strip()

        if option == "1":
            service = input("Enter Service Name: ").strip()
            # Check if service already exists
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
            break
        else:
            print("Invalid choice. Try again.")

if __name__ == "__main__":
    main()
