import json
import datetime
import os

# get the current directory of the script
dir_path = os.path.dirname(os.path.realpath(__file__))
template_file = os.path.join(dir_path, "template.txt")
data_file = os.path.join(dir_path, "data.json")

# Create the directory to save the invitations
try:
    os.mkdir(os.path.join(dir_path, "generated_emails"))
except FileExistsError:
    pass
gen_emails_dir = os.path.join(dir_path, "generated_emails")

# Read the template file
with open(template_file, 'r') as f:
    template = f.read()

# Read the JSON file
with open(data_file, 'r') as f:
    data = json.load(f)

# Loop through the data and replace the placeholders
for record in data:
    name = record['name']
    email = record['email']
    date = datetime.datetime.now().strftime('%d/%m/%Y')
    # Replace the placeholders in the template with the actual values
    invitation = template.replace('<name>', name)\
                         .replace('<email>', email)\
                         .replace('<date>', date)
    # Save the invitation as a new text file
    filename = f"{gen_emails_dir}/{name}.txt"
    with open(filename, 'w') as f:
        f.write(invitation)
