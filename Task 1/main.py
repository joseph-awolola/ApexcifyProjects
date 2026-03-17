import smtplib
# mail send to 20 emails

email_address = input("Enter in the email address you'll be sending from")
email_password = input("Enter in the password you'll be seding from")
s = smtplib.SMTP("smtp.gmail.com", 587)
s.starttls()
s.login(email_address, email_password)