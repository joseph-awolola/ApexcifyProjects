import smtplib
import time
from datetime import datetime
import os
from dotenv import load_dotenv

load_dotenv()

def get_mails(file):
    with open(file, "r") as email_file:
        emails = email_file.read()
        emails = emails.split('\n')
        start_time = datetime.now()
        failed = 0
        success = 0
        print("Sending...")
        for x in emails:
            try:
                send_mail(x)
                success += 1
            except smtplib.SMTPConnectError:
                # If a connection could not be established
                print(f"Connection could not be established for email {x}")
                failed += 1
                print(f"{failed} failed operations")
            except smtplib.SMTPAuthenticationError:
                print(f"There was a problem authenticating the user {x}")
                failed += 1
                print(f"{failed} failed operations")
            except smtplib.SMTPServerDisconnected:
                print(f"The server got disconnected")
                failed += 1
                print(f"{success} successful operations")
            finally:
                print(f"Mail sent to {x}")

        end_time = datetime.now()
        duration = end_time - start_time
        print("Sent successfully")
        print(f"Mail sent to {len(emails)} in {duration.seconds} seconds")

def send_mail(email:str):
    email_address = os.getenv("EMAIL_NAME")
    email_password = os.getenv("EMAIL_PASSWORD")

    with smtplib.SMTP_SSL("smtp.gmail.com", 465) as s:

        s.login(email_address, email_password)
        subject = "Automated Python Email"
        body = "This is a test message sent via Python."
        msg = f"Subject: {subject}\n\n{body}"
        s.sendmail(email_address, email, msg)



if __name__ == "__main__":
    get_mails("emails.txt")
