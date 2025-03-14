# Hash Reverser

A Python project for reversing SHA-256 hashed numbers to their original values using a precomputed dictionary of hashes.

## Project Overview 📖 

This project demonstrates how to reverse hashed data using Python's `hashlib` module. It takes a CSV file containing names and SHA-256 hashes, attempts to match the hashes to their original numbers, and produces a human-readable output.

### Example Input CSV (`hashed_data.csv`):
```csv
Ali,df91d97b8518e7a95c11b21218d4be8306c42ff83eee9e879a2a81a8518f6424
Hossein,6affdae3b3c1aa6aa7689e9b6a7b3225a636aa1ac0025f490cca1285ceaf1487
```

### Example Output (reversed_data.json):

```json
{
    "Ali": 1234,
    "Hossein": 5678,
}
```
## Features ⚙️ 
- Generates SHA-256 hashes for numbers in the range 0-9999.
- Matches provided hashes to their corresponding original numbers.
- Outputs the result in a clean, human-readable JSON format.
- Handles unmatched hashes gracefully by marking them as "Hash not found".



## How to Run 🚀 

1. Clone the repository:

```bash
git clone https://github.com/heydari-dev/hash-reverser.git
cd hash-reverser
```

2. Place your CSV file (hashed_data.csv) in the same directory.

3. Run the Python script:

```bash
python main.py
```
4. Check the output file reversed_data.json for the results.

## File Structure 📂 

```
hash-reverser/
├── main.py               # Main script
├── hashed_data.csv    # Example input CSV file
├── reversed_data.json    # Output JSON file (generated after running the script)
├── README.md             # Project documentation
└── .gitignore            # Ignore unnecessary files
```

## How It Works 🔍 
1. **Hash Generation**:

- The script generates SHA-256 hashes for numbers between 0 and 9999.
- These hashes are stored in a dictionary for quick lookups.

2. **Input Processing**:

- Reads a CSV file containing names and SHA-256 hashes.

3. **Hash Matching**:

- Compares hashes in the input file with precomputed hashes.
- If a match is found, the hash is replaced with its original number.
- If no match is found, the script marks it as Hash not found.

4. **Output**:

- Saves the results in reversed_data.json.

## Requirements 🛠️ 
- Python 3.x
- No additional dependencies (uses Python's standard library).

## License 📄 
This project is licensed under the [MIT License](LICENSE).

