import json
import os

# get the current directory of the script
dir_path = os.path.dirname(os.path.realpath(__file__))
template_file = os.path.join(dir_path, "template.txt")
data_file = os.path.join(dir_path, "data.json")

# Create the invitation template
template = f"""
Dear <name> (<email>),

You are cordially invited to a dinner party on <date>.
Please let us know if you can make it.

Sincerely,
The Host
"""

with open(template_file, "w") as f:
    f.write(template)

# Generate the data file
data = [
    {"name": "Alice", "email": "alice@example.com"},
    {"name": "Bob", "email": "bob@example.com"},
    {"name": "Charlie", "email": "charlie@example.com"}
]

with open(data_file, "w") as f:
    json.dump(data, f)
