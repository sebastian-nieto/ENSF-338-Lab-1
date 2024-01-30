import json

# Step 1: Load the file
with open('large-file.json', 'r',encoding ="UTF-8") as file:
    data = json.load(file)

# Step 2: Change the "size" field in every record to the value 35
for record in data:
    if "size" in record:
        record["size"] = 35

# Step 3: Write back the result, in reverse order, to a file called output.2.3.json
data.reverse()  # Reverse the list
output_file_path = 'output.2.3.json'

with open(output_file_path, 'w') as output_file:
    json.dump(data, output_file, indent=2)

print(f"Modified data written to {output_file_path}")
