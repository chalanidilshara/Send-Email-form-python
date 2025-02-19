import smtplib
import getpass
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

# Ask user for email and password (password input is hidden)
sender_email = input("Enter sender email: ")
password = getpass.getpass("Enter sender email password: ")
receiver_email = input("Enter recipient email: ")

# Create the email message
msg = MIMEMultipart()
msg["From"] = sender_email
msg["To"] = receiver_email
msg["Subject"] = "Test Email from Python"

# Email body
body = "Hello, this is a test email sent from Python."
msg.attach(MIMEText(body, "plain"))

# SMTP Server setup (Gmail - Secure SSL Port 465)
smtp_server = "smtp.gmail.com"
smtp_port = 465  

server = None  # Initialize server variable

try:
    # Connect using SSL (secure connection)
    server = smtplib.SMTP_SSL(smtp_server, smtp_port, timeout=10)
    server.login(sender_email, password)
    server.sendmail(sender_email, receiver_email, msg.as_string())
    
    print("✅ Email sent successfully!")

except Exception as e:
    print(f"❌ Error: {e}")

finally:
    # Ensure the SMTP connection is closed
    if server:
        server.quit()
        print("🔒 Connection closed.")
