# 📧 Multi Email Sender – Bulk Email Send Application

A professional and user-friendly desktop app built in Python to send customized bulk emails (with optional attachments) to  **Multiple Emails**.

---

## ✨ Features

- GUI-based email sender using Tkinter
- Personalized HTML-styled messages
- Multi-recipient support (Gmail-only)
- Optional PDF attachment (e.g., notices)
- Logs sent/failed mails into a CSV file
- Institution-branded email design

---

## 🧠 Modules Used

| Module                 | Purpose                                |
|------------------------|----------------------------------------|
| `tkinter`              | GUI development                        |
| `smtplib`              | Send email using SMTP protocol         |
| `email.mime` modules   | Constructing HTML emails & attachments |
| `csv`                  | Logging results                        |
| `os`                   | File path management                   |

---

## ⚙️ Setup Instructions

### 1. Gmail SMTP Setup

To use your Gmail account to send emails, follow these steps:

1. Go to your **Google Account** → **Security**.
2. Enable **2-Step Verification**.
3. Under **App Passwords**, generate a password for "Mail" and "Windows Computer".
4. Replace the following values in the source code:

```python
EMAIL_ADDRESS = "your-email@gmail.com"
EMAIL_PASSWORD = "your-app-password"
```

---

## 🖥️ How to Use

1. **Run the Python script.**

2. **Enter:**
   - Reciver names (comma-separated, )
   - Their Gmail addresses (comma-separated, same order as names)
   - Mail subject
   - Mail body
   - Attach a PDF notice (optional)

3. **Click Send Mail.**

4. A CSV log (`mail_data.csv`) will be created showing success and failure results.("optional" you can update and create a page for this also)

---

## 📂 Output Log Format

The file `mail_data.csv` will be structured like this:

| Success Emails       | Failed Emails        |
|----------------------|----------------------|
| example1@gmail.com   | example2@gmail.com   |
| example3@gmail.com   |                      |

---


## 📂 Exe file

- The exe file i have built is inside the dist zip file unzip it to check it out

---

## 📌 Note

- This application currently works **only with Gmail** addresses.
- Make sure to enable **App Passwords** in your Google account for security.
- **Do not share** your app password publicly.
- Emails are formatted using a clean HTML template for a professional look.

---

## 🏫 Built For

**My college Lakshya Institute of Technology (LIT), Odisha**  

- Developed as an internal tool to send academic notifications and updates efficiently to students via bulk email.
---

## 📬 Contact

If you have questions or feedback:

🔗 https://www.linkedin.com/in/biswabhusan-sahoo-22b704292/ 

---
