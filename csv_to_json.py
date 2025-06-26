import csv
import json

def csv_to_json(csv_file, json_file):
    """Convert a CSV file to JSON."""
    data = []
    with open(csv_file, 'r') as f:
        csv_reader = csv.DictReader(f)
        for row in csv_reader:
            data.append(row)
    
    with open(json_file, 'w') as f:
        json.dump(data, f, indent=4)

if __name__ == "__main__":
    csv_file = input("Enter CSV file path: ").strip()
    json_file = input("Enter output JSON file path: ").strip()
    csv_to_json(csv_file, json_file)
    print(f"Converted {csv_file} to {json_file}")
