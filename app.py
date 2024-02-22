import tkinter as tk
from tkinter import filedialog
import requests
from msal import ConfidentialClientApplication
import markdown
import csv

# To add:
# 1. Add a input url for logo for the header and footer of the email (should be saveable)
# 2. Add that you can do {} in the markdown and it will be replaced by the data in the csv file
# 3. Add an input for the sender's email and password
# 4. Add an input for what's the header in the csv file for the email addresses
# 5. Add a radio button to mark if the email is important or not (if important, mark as important)
# 6. Add a dropdown for the schedule of the email if need to be address in calendar

def send_email():
    # Convert Markdown to HTML
    html = markdown.markdown(text_area.get("1.0", "end-1c"))

    # Set up the Azure AD app registration information
    client_id = "7b7ed06b-66bf-4fb3-abfe-488e7e7fa286"
    client_secret = "NeF8Q~nTGZS.ns7SdpkjeDtzQ8CvXWjXkEVt7aE6"
    tenant_id = "ea5d6927-676e-457e-9c72-59d895002fed"

    # Set up the API endpoint
    authority = f'https://login.microsoftonline.com/{tenant_id}'
    endpoint = 'https://graph.microsoft.com/v1.0/me/sendMail'

    # Set up the scope
    scope = ['https://graph.microsoft.com/.default']

    # Set up the client
    app = ConfidentialClientApplication(client_id, authority=authority, client_credential=client_secret)

    # Get the access token
    result = app.acquire_token_for_client(scopes=scope)

    # Read the email addresses from the CSV file
    with open(file_path.get(), 'r') as f:
        reader = csv.reader(f)
        email_addresses = [row[0] for row in reader]

    # Set up the email details
    for email_address in email_addresses:
        email = {
            'message': {
                'subject': subject_entry.get(),
                'body': {
                    'contentType': 'HTML',
                    'content': html
                },
                'toRecipients': [
                    {
                        'emailAddress': {
                            'address': email_address
                        }
                    }
                ]
            },
            'saveToSentItems': 'true'
        }

        # Send the email
        if 'access_token' in result:
            headers = {
                'Authorization': 'Bearer ' + result['access_token'],
                'Content-Type': 'application/json'
            }
            r = requests.post(endpoint, headers=headers, json=email)
            print(r.text)
            r.raise_for_status()
        else:
            print(result.get('error'))
            print(result.get('error_description'))
            print(result.get('correlation_id'))

def browse_file():
    filename = filedialog.askopenfilename(filetypes=[("CSV files", "*.csv")])
    file_path.set(filename)

root = tk.Tk()
root.title("Microsoft Markdown Email Sender")

subject_label = tk.Label(root, text="Subject:")
subject_label.grid(row=0, column=0, sticky='e')

subject_entry = tk.Entry(root)
subject_entry.grid(row=0, column=1)

file_label = tk.Label(root, text="CSV File:")
file_label.grid(row=1, column=0, sticky='e')

file_path = tk.StringVar()
file_entry = tk.Entry(root, textvariable=file_path)
file_entry.grid(row=1, column=1)

browse_button = tk.Button(root, text="Browse", command=browse_file)
browse_button.grid(row=1, column=2)

text_area = tk.Text(root, height=10, width=50)
text_area.grid(row=2, column=0, columnspan=3)

submit_button = tk.Button(root, text="Send Email", command=send_email)
submit_button.grid(row=3, column=0, columnspan=3)

root.mainloop()