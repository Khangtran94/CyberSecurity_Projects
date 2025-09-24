# API Key Storage System

## Overview
This project provides a simple **API Key Storage System** implemented in Python. It allows users to securely store and retrieve API keys either in-memory (temporary) or in a file (persistent). The system is designed to manage API keys for different services, ensuring that keys are stored securely and can be easily retrieved when needed.

## Features
- **Storage Options**: Choose between in-memory storage (temporary) or file-based storage (persistent, using a JSON file).
- **Secure Storage**: Store API keys for various services with a simple interface.
- **Retrieve Keys**: Easily retrieve stored API keys by service name.
- **Duplicate Check**: Prevents overwriting existing service keys.
- **User-Friendly CLI**: Interactive command-line interface for storing and retrieving keys.

## Requirements
- Python 3.x
- Standard libraries: `os`, `json`

No external dependencies are required.

## Installation
1. Clone or download the repository containing the `Ex2_Secrets_Manager.py` script.
2. Ensure Python 3.x is installed on your system.
3. Place the `Ex2_Secrets_Manager.py` file in your desired directory.

## Usage
1. Run the script using Python:
   ```bash
   python Ex2_Secrets_Manager.py
   ```
2. Choose a storage type:
   - **1. In-Memory**: API keys are stored temporarily and cleared when the program exits.
   - **2. File**: API keys are saved to a file (`apikeys.json`) for persistent storage.
3. Follow the interactive menu to:
   - **Store API Key**: Enter a service name and its corresponding API key.
   - **Retrieve API Key**: Enter a service name to retrieve the stored API key.
   - **Exit**: Close the program.

### Example Interaction
```plaintext
API Key Storage System
Choose storage type:
1. In-Memory (temporary)
2. File (persistent)
Enter choice (1/2): 1

Options:
1. Store API Key
2. Retrieve API Key
3. Exit
Enter choice: 1
Enter Service Name: Twitter
Enter API Key: abc123xyz
API Key stored successfully.

Options:
1. Store API Key
2. Retrieve API Key
3. Exit
Enter choice: 2
Enter Service Name: Twitter
=> API Key of Twitter Service Name: abc123xyz
```

## File Structure
- `Ex2_Secrets_Manager.py`: Main script containing the `APIKeyStorage` class and CLI logic.
- `apikeys.json` (optional): Created when using file-based storage to store API keys persistently.

## Code Structure
- **Class `APIKeyStorage`**:
  - `__init__(storage_type, filename)`: Initializes the storage system (in-memory or file-based).
  - `_save_to_file()`: Saves the in-memory store to a JSON file (used for file-based storage).
  - `store(service_name, api_key)`: Stores an API key for a given service.
  - `retrieve(service_name)`: Retrieves the API key for a given service.
- **Function `main()`**: Implements the interactive CLI for user interaction.

## Notes
- **Security**: The current implementation stores API keys in plain text in the `apikeys.json` file when using file-based storage. For production use, consider encrypting the file or using a more secure storage mechanism.
- **Case Insensitivity**: Service names are converted to lowercase to ensure consistent key storage and retrieval.
- **Error Handling**: The script handles cases where the JSON file is invalid or the service name already exists.

## Limitations
- No encryption for file-based storage.
- No support for updating or deleting existing API keys.
- No validation for API key format.

## Future Improvements
- Add encryption for file-based storage.
- Support updating or deleting API keys.
- Add validation for API key formats.
- Include support for environment variable storage.

## License
This project is unlicensed and provided as-is for educational purposes.