# Copy of app.py but google instead of microsoft

import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
import markdown
import csv
import tkinter as tk
from tkinter import filedialog

def send_email():
    # Convert Markdown to HTML
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
                                <img src="https://media.discordapp.net/attachments/1155185540254142475/1170666524965609482/banner.png?ex=65e44ca9&is=65d1d7a9&hm=9de7bbac48e2684aa78f84da852959ca7ebb53ac3225134919088a77dc1c41e9&=&format=webp&quality=lossless" class="header-logo">
                            </td>
                        </tr>
                    </table>
    
                    <!-- Main Content -->
                    <div class="container">
                        <table class="main">
                            <tr>
                                <td>
                                    <p>
                                        {markdown.markdown(text_area.get("1.0", "end-1c"))}
                                    </p>
                                </td>
                            </tr>
                    </table>
                </div>
                
                <!-- Footer -->
                <table>
                    <tr>
                        <td class="footer">
                            <img src="https://media.discordapp.net/attachments/1155185540254142475/1170666540971081758/footer.png?ex=65e44cad&is=65d1d7ad&hm=d2b035bf0cfdc5e19f37ecc69d5dda4833c5484a34cb4b1bb1514ceb65a54257&=&format=webp&quality=lossless" alt="" class="footer-logo">
                        </td>
                    </tr>
                </table>
            </td>
        </tr>
    </table>
    </body>
    </html>
    """
    

    # Read the email addresses from the CSV file
    with open(file_path.get(), 'r') as f:
        reader = csv.reader(f)
        email_addresses = [row[0] for row in reader]

    # Set up the email details
    for email_address in email_addresses:
        msg = MIMEMultipart('related')
        msg['Subject'] = subject_entry.get()
        msg['From'] = 'bscs0102@gmail.com'
        msg['To'] = email_address

        html_part = MIMEText(html, 'html')
        msg.attach(html_part)

        s = smtplib.SMTP_SSL(host='smtp.gmail.com', port=465)
        s.login('bscs0102@gmail.com', 'nhvd pczq wrtf qrdu')
        s.sendmail('bscs0102@gmail.com', email_address, msg.as_string())
        s.quit()

def browse_file():
    filename = filedialog.askopenfilename(filetypes=[("CSV files", "*.csv")])
    file_path.set(filename)

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

submit_button = tk.Button(root, text="Send Email", command=send_email)
submit_button.grid(row=3, column=0, columnspan=3)

root.mainloop()
