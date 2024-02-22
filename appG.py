import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
import markdown
import csv
import tkinter as tk
from tkinter import filedialog
from tkinter import messagebox

def send_email(isTrue):
    if not isTrue:
        return
    # Read the CSV file
    with open(file_path.get(), 'r') as f:
        reader = csv.DictReader(f)
        rows = list(reader)  # Store the rows in a list
    for row in rows:  # Iterate over the list of rows
        # Get a fresh copy of the markdown text for each email
        markdown_text = markdown.markdown(text_area.get("1.0", "end-1c"))
        for key, value in row.items():
            markdown_text = markdown_text.replace("{" + key + "}", value)
            
        html = f"""
        <!DOCTYPE html>
        <html lang="en">
        <head>
            <meta charset="UTF-8">
            <meta name="viewport" content="width=device-width, initial-scale=1.0">
            <title>BSCS 1-2 WebApp</title>
            <link href="https://fonts.googleapis.com/css2?family=Rubik&display=swap" rel="stylesheet">
        
            <style>
                body {{
                    font-family: 'Rubik', sans-serif;
                    line-height: 1.5;
                    background-color: #f9ede8;
                    color: #232F3E;
                }}
        
                table {{
                    width: 100%;
                    margin: 0 auto;
                }}

                img {{
                    max-width: 100%;
                    border-radius: 10px;
                }}
        
                .blue {{
                    color: #006BC2;
                }}
                .yellow {{
                    color: #F8BF67;
                }}
        
                .blue , .yellow {{
                    font-weight: 600;
                }}
                .wrapper {{
                    max-width: 50rem;
                    padding-bottom: 0.3rem;
                }}
        
                .header-logo {{
                    display: block;
                    max-width: 100%;
                }}
                .container {{
                    padding: 2rem 1.5rem;
                }}
                .main {{
                    padding: 3rem 2rem 1rem 2rem;
                    text-align: justify;
                    background-color: #FFFFFF;
                    border-radius: 0.5rem;
                }}
        
                hr.solid {{
                    margin: 1.5rem 0 0.8rem 0;
                }}
                .grey {{
                    color: #666666;
                }}
                .footer-logo {{
                    display: block;
                    max-width: 100%;
                }}
                .pad-top-s {{
                    padding-top: 1.5rem;
                }}
                .social img {{
                    width: 2rem;
                    margin-top: -0.5rem;
                    margin-right: 1rem;
                }}
                .social a {{
                    text-decoration: none;
                }}
                .button {{
                    display: block;
                    width: 200px;
                    height: 50px;
                    margin: 20px auto;
                    background-color: #0c70c2;
                    color: white;
                    text-align: center;
                    line-height: 50px;
                    text-decoration: none;
                    border-radius: 10px;
                    transition-duration: 0.4s;
                }}
                .button:hover {{
                    background-color: #045c8c;
                }}
            </style>
        </head>
        
        <body>
            <table class="wrapper">
                <tr>
                    <td style="background-color: #fff; border-radius: 10px;">
                        <!-- Logo Header -->
                        <table>
                            <tr>
                                <td>
                                    <img src="{header_logo_url.get()}" class="header-logo">
                                </td>
                            </tr>
                        </table>
        
                        <!-- Main Content -->
                        <div class="container">
                            <table class="main">
                                <tr>
                                    <td>
                                        <p>
                                            {markdown_text}
                                        </p>
                                    </td>
                                </tr>
                        </table>
                    </div>

                    
                    <!-- Footer -->
                    <table>
                        <tr>
                            <td class="footer">
                                <img src="{footer_logo_url.get()}" alt="" class="footer-logo">
                            </td>
                        </tr>
                    </table>
                </td>
            </tr>
        </table>
        </body>
        </html>
        """
        msg = MIMEMultipart('related')
        msg['Subject'] = subject_entry.get()
        msg['From'] = sender_email.get()
        msg['To'] = row[email_header.get()]

        if is_important.get() == "Yes":
            msg['Importance'] = 'High'

        html_part = MIMEText(html, 'html')
        msg.attach(html_part)

        s = smtplib.SMTP_SSL(host='smtp.gmail.com', port=465)
        s.login(sender_email.get(), sender_password.get())
        s.sendmail(sender_email.get(), msg['To'], msg.as_string())
        s.quit()

def browse_file():
    filename = filedialog.askopenfilename(filetypes=[("CSV files", "*.csv")])
    file_path.set(filename)

def validate():
    if not (header_logo_url.get() and footer_logo_url.get() and email_header.get() and sender_email.get() and sender_password.get() and is_important.get()):
        messagebox.showerror("Error", "All fields are required.")
        return False
    return True

root = tk.Tk()
root.title("Markdown Email Sender")

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

header_logo_url = tk.StringVar()
tk.Label(root, text="Header Logo URL").grid(row=3, column=0)
header_logo_entry = tk.Entry(root, textvariable=header_logo_url)
header_logo_entry.grid(row=3, column=1)

footer_logo_url = tk.StringVar()
tk.Label(root, text="Footer Logo URL").grid(row=4, column=0)
footer_logo_entry = tk.Entry(root, textvariable=footer_logo_url)
footer_logo_entry.grid(row=4, column=1)

email_header = tk.StringVar()
tk.Label(root, text="Email Header").grid(row=5, column=0)
email_header_entry = tk.Entry(root, textvariable=email_header)
email_header_entry.grid(row=5, column=1)

sender_email = tk.StringVar()
tk.Label(root, text="Sender Email").grid(row=6, column=0)
sender_email_entry = tk.Entry(root, textvariable=sender_email)
sender_email_entry.grid(row=6, column=1)

sender_password = tk.StringVar()
tk.Label(root, text="Sender Password").grid(row=7, column=0)
sender_password_entry = tk.Entry(root, textvariable=sender_password, show="*")
sender_password_entry.grid(row=7, column=1)

is_important = tk.StringVar(value="off")
tk.Label(root, text="Important").grid(row=8, column=0)
tk.Radiobutton(root, text="Yes", variable=is_important, value="Yes").grid(row=8, column=1)
tk.Radiobutton(root, text="No", variable=is_important, value="No").grid(row=8, column=2)

submit_button = tk.Button(root, text="Submit", command=lambda: send_email(validate()))
submit_button.grid(row=9, column=0, columnspan=2)

root.mainloop()