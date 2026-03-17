import smtplib
from datetime import datetime
import os
from dotenv import load_dotenv

load_dotenv()

def get_mails(file):
    with open(file, "r") as email_file:
        emails = email_file.read()
        emails = emails.split('\n')
        start_time = datetime.now()




        send_mail(emails)

        end_time = datetime.now()
        duration = end_time - start_time
        print("Sent successfully")
        print(f"Mail sent to {len(emails)} clients in {duration.seconds} seconds")

def send_mail(emails):
    failed = 0
    success = 0

    with smtplib.SMTP_SSL("smtp.gmail.com", 465) as s:
        print("Authenticating...")
        s.login(email_address, email_password)
        print("Sending...")

        for x in emails:
            try:

                s.sendmail(email_address, x, msg)
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


if __name__ == "__main__":
    email_address = os.getenv("EMAIL_NAME")
    email_password = os.getenv("EMAIL_PASSWORD")


    msg:str
    while True:
        email_opt = input("""What do you want to send
            1. Type message here
            2. Send file containing message
            """)

        if email_opt == "1":
            subject = input("Type header here: ")
            body = input("Type body here: ")
            msg = f"Subject: {subject}\n\n{body}"
            get_mails("emails.txt")
            break
        if email_opt == "2":
            msg = "lorem ipsum"
            get_mails("emails.txt")
            break
        else:
            print("Invalid option")

