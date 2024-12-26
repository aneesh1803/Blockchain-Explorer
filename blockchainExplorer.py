import json

# Example blockchain stored in a JSON file (mock data)
blockchain = [
    {
        "index": 1,
        "timestamp": "2024-12-01T10:00:00",
        "data": "Genesis Block",
        "previous_hash": "0",
        "hash": "abc123"
    },
    {
        "index": 2,
        "timestamp": "2024-12-02T11:00:00",
        "data": "Block 2 data",
        "previous_hash": "abc123",
        "hash": "def456"
    },
    {
        "index": 3,
        "timestamp": "2024-12-03T12:00:00",
        "data": "Block 3 data",
        "previous_hash": "def456",
        "hash": "ghi789"
    }
]

# Function to display the blockchain
def display_blockchain(chain):
    print("Blockchain Explorer\n")
    for block in chain:
        print(f"Block Index: {block['index']}")
        print(f"Timestamp: {block['timestamp']}")
        print(f"Data: {block['data']}")
        print(f"Previous Hash: {block['previous_hash']}")
        print(f"Hash: {block['hash']}")
        print("-" * 40)

# Main explorer loop
def blockchain_explorer():
    while True:
        print("\nOptions:")
        print("1. View entire blockchain")
        print("2. View a specific block")
        print("3. Exit")
        choice = input("Enter your choice: ")
        
        if choice == "1":
            display_blockchain(blockchain)
        elif choice == "2":
            try:
                index = int(input("Enter the block index (1-based): "))
                if 1 <= index <= len(blockchain):
                    block = blockchain[index - 1]
                    print("\nBlock Details:")
                    print(json.dumps(block, indent=4))
                else:
                    print("Invalid index. Try again.")
            except ValueError:
                print("Invalid input. Please enter a number.")
        elif choice == "3":
            print("Exiting blockchain explorer. Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.")

# Run the blockchain explorer
blockchain_explorer()
