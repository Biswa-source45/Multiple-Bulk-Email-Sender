from tkinter import *
from tkinter import messagebox, filedialog, StringVar
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.application import MIMEApplication
import csv
import os

SMTP_SERVER = "smtp.gmail.com"
SMTP_PORT = 587
EMAIL_ADDRESS = "litcamsystem01@gmail.com"
EMAIL_PASSWORD = "gxlz dvgc gayy sprl"

def get_html_template(user_name, body_text):
    return f"""
    <!DOCTYPE html>
    <html>
    <head>
      <meta charset='UTF-8'>
      <title>Welcome to Lakshya Institute of Technology</title>
    </head>
    <body style='font-family: Arial, sans-serif; background-color: #f9f9f9; padding: 0; margin: 0;'>
      <table width='100%' cellpadding='0' cellspacing='0' style='max-width: 600px; margin: auto; background-color: #ffffff; border-radius: 8px; box-shadow: 0 0 10px rgba(0,0,0,0.05);'>
        <tr>
          <td style='text-align: center; padding: 30px 20px 10px 20px;'>
            <img src='https://i.postimg.cc/zBQ1nzhG/1620793172logoload.png' alt='LIT Logo' width='120'>
            <h1 style='color: #D35400; margin-bottom: 5px;'>Welcome to Lakshya Institute of Technology</h1>
            <p style='color: #555;'>Your journey to excellence begins here!</p>
          </td>
        </tr>

        <tr>
          <td style='padding: 20px;'>
            <p>Dear <strong>{user_name}</strong>,</p>
            <p>{body_text}</p>
            <div style='text-align:center; margin: 20px 0;'>
              <img src='https://media.giphy.com/media/3ohs4BSacFKI7A717y/giphy.gif' alt='Welcome Gif' style='width: 80%; max-width: 400px; border-radius: 10px;'>
            </div>
            <p>If you have any questions, feel free to contact us at <a href='mailto:support@litodisha.ac.in'>support@litodisha.ac.in</a>.</p>
            <p style='margin-top: 30px;'>Warm regards,<br><strong>Team LIT</strong><br>Odisha, India</p>
          </td>
        </tr>

        <tr>
          <td style='background-color: #F4F6F6; text-align: center; padding: 20px; border-top: 1px solid #ddd; font-size: 12px; color: #999;'>
            © 2025 Lakshya Institute of Technology. All rights reserved.
          </td>
        </tr>
      </table>
    </body>
    </html>
    """

def send_mail():
    names = [name.strip() for name in name_entry.get().strip().split(',')]
    emails = [email.strip() for email in mail_entry.get().strip().split(',')]

    filtered = [(n, e) for n, e in zip(names, emails) if e.endswith("@gmail.com")]

    subject = subject_entry.get().strip()
    body = body_entry.get("1.0", END).strip()

    if not filtered or not subject or not body:
        messagebox.showerror("Error", "Please fill in all required fields correctly.")
        return

    success_list = []
    failed_list = []

    for user_name, to_email in filtered:
        msg = MIMEMultipart()
        msg['From'] = EMAIL_ADDRESS
        msg['To'] = to_email
        msg['Subject'] = subject

        html_content = get_html_template(user_name, body)
        msg.attach(MIMEText(html_content, "html"))

        if file_path.get():
            try:
                with open(file_path.get(), "rb") as attachment:
                    filename = file_path.get().split('/')[-1]
                    part = MIMEApplication(attachment.read(), Name=filename)
                    part['Content-Disposition'] = f'attachment; filename="{filename}"'
                    msg.attach(part)
            except Exception as e:
                failed_list.append(to_email)
                continue

        try:
            server = smtplib.SMTP(SMTP_SERVER, SMTP_PORT)
            server.starttls()
            server.login(EMAIL_ADDRESS, EMAIL_PASSWORD)
            server.sendmail(EMAIL_ADDRESS, to_email, msg.as_string())
            success_list.append(to_email)
        except:
            failed_list.append(to_email)
        finally:
            server.quit()

    # Append success/failure results to CSV
    csv_path = "mail_data.csv"
    try:
        with open(csv_path, "a", newline="") as csvfile:
            writer = csv.writer(csvfile)
            max_len = max(len(success_list), len(failed_list))
            for i in range(max_len):
                row = [
                    success_list[i] if i < len(success_list) else '',
                    failed_list[i] if i < len(failed_list) else ''
                ]
                writer.writerow(row)
    except Exception as e:
        messagebox.showwarning("CSV Error", f"Couldn't write to CSV: {e}")

    messagebox.showinfo("Mail Status", f"✔ Sent: {len(success_list)} | ❌ Failed: {len(failed_list)}")

def browse_file():
    filename = filedialog.askopenfilename(filetypes=[("PDF Files", "*.pdf")])
    file_path.set(filename)

# GUI Setup
win = Tk()
win.title("Multi-Email-sender")
win.configure(bg="#9DC08B")
win.minsize(900, 800)
win.state('zoomed')

Label(win, text="Email Sender", font=("Helvetica", 60, "bold"), bg="#9DC08B").place(x=500, y=50, height=100)

Label(win, text="Enter Student's Name:", font=("Helvetica", 20), bg="#9DC08B").place(x=300, y=150, height=40)
name_entry = Entry(win, font=("Helvetica", 18), width=35, bd=0, bg="#F2F2F2", fg="#000000")
name_entry.place(x=700, y=150, height=40)

Label(win, text="Enter the mail address to send:", font=("Helvetica", 20), bg="#9DC08B").place(x=300, y=220, height=50)
mail_entry = Entry(win, font=("Helvetica", 18), width=35, bd=0, bg="#F2F2F2", fg="#000000")
mail_entry.place(x=700, y=220, height=50)

Label(win, text="Enter the subject of the mail:", font=("Helvetica", 20), bg="#9DC08B").place(x=300, y=300, height=50)
subject_entry = Entry(win, font=("Helvetica", 18), width=35, bd=0, bg="#F2F2F2", fg="#000000")
subject_entry.place(x=700, y=300, height=50)

Label(win, text="Enter the body of the mail:", font=("Helvetica", 20), bg="#9DC08B").place(x=300, y=380, height=50)
body_entry = Text(win, font=("Helvetica", 18), width=35, bd=0, bg="#F2F2F2", fg="#000000")
body_entry.place(x=700, y=380, height=150)

Label(win, text="Attach Notice (PDF):", font=("Helvetica", 14), bg="#9DC08B").place(x=300, y=560, height=50)
attach_button = Button(win, text="Attach", font=("Helvetica", 14), bg="#66D2CE", fg="#000000", command=browse_file)
attach_button.place(x=700, y=560, height=50, width=150)

file_path = StringVar()
file_label = Label(win, textvariable=file_path, font=("Helvetica", 12), bg="#9DC08B")
file_label.place(x=860, y=560, height=50)

button = Button(win, text="Send Mail", font=("Helvetica", 20), bg="#66D2CE", fg="#000000", command=send_mail)
button.place(x=700, y=660, height=50, width=200)

win.mainloop()
