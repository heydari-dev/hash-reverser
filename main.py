import hashlib
import csv
import json

# Function to generate a dictionary of hashes for numbers in a given range
def generate_hashes(start=0, end=10000):
    """Generate a dictionary of SHA-256 hashes for numbers in a specified range."""
    hash_dict = {}
    for number in range(start, end):
        hashed_string = hashlib.sha256(str(number).encode('utf-8')).hexdigest()
        hash_dict[hashed_string] = number
    return hash_dict

# Function to read the CSV file and load data into a dictionary
def load_csv_to_dict(file_path):
    """Load data from a CSV file into a dictionary."""
    data = {}
    try:
        with open(file_path, newline='', encoding='utf-8') as f:
            csv_reader = csv.reader(f)
            for row in csv_reader:
                if len(row) == 2:  # Ensure valid row
                    data[row[0]] = row[1]
    except FileNotFoundError:
        print(f"Error: File '{file_path}' not found.")
        exit(1)
    except Exception as e:
        print(f"Error reading the file: {e}")
        exit(1)
    return data

# Function to reverse hashes in the dictionary
def reverse_hashes(data, hash_dict):
    """Reverse the hashes in the data dictionary using the hash_dict."""
    for key, hashed_value in data.items():
        if hashed_value in hash_dict:
            data[key] = hash_dict[hashed_value]
        else:
            data[key] = "Hash not found"  # Handle unmatched hashes
    return data

# Main function
def main():
    # File path for the CSV file
    csv_file_path = 'hashed_data.csv'

    # Step 1: Generate hashes
    hash_dict = generate_hashes()

    # Step 2: Load CSV data
    person_data = load_csv_to_dict(csv_file_path)

    # Step 3: Reverse the hashes
    reversed_data = reverse_hashes(person_data, hash_dict)

    # Step 4: Output the result
    output_file = 'reversed_data.json'
    with open(output_file, 'w', encoding='utf-8') as f:
        json.dump(reversed_data, f, indent=4, ensure_ascii=False)

    print(f"Hash reversing completed. Output saved to '{output_file}'.")

if __name__ == "__main__":
    main()
