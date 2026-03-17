import re

import os
import requests
from bs4 import BeautifulSoup

import shutil
from glob import glob


def mail_extraction(txt_file:str):
    from email_validator import validate_email, EmailNotValidError

    with open(txt_file, 'r') as file:
        content = file.read()
        content = content.split(' ')

        # Determining if the string is an email address
        # we can use regex
        # apparently, email addresses allow special characters
        email_pattern = r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$'
        addresses:list = []
        for x in content:
            x = re.findall(email_pattern, x)
            if x:
                addresses.append(x[0])

    # Write all content from the previous file to the current file
    with open('email_file.txt', 'a+') as email_file:
        for x in addresses:
            try:
                validate_email(x, check_deliverability=True)
                email_file.write(x + '  ' + 'Valid\n')
            except EmailNotValidError:
                email_file.write(x + '  ' + 'Not valid\n')

def scraper(address:str):
    try:
        data = requests.get(address)
        html = data.content # scrapes content of the retrieved web page

        # this is where the magic happens
        soup = BeautifulSoup(html, 'html.parser')
        return soup.title.string # soup.title prints it out with the html tags
    except requests.ConnectTimeout as e:
        print("Website may be down.")
        return e.errno
    except requests.exceptions.ConnectionError as e:
        print("Please check your internet connection.")

def file_transfer(folder_a, folder_b):
    files_moved:int = 0
    while True:
        if os.path.exists(folder_a): break
        folder_a = input(f"{folder_a} is not a valid location, please, enter a valid location")

    if not os.path.exists(folder_b):
        os.mkdir(folder_b)
        print(f"File created at location {folder_b}")
    # glob library is used to retrieve the files within a folder in python
    files = glob(os.path.join(folder_a, "*.jpg")) + glob(os.path.join(folder_a, "*.jpeg"))
    req_files = len(files)
    for file in files:
        try:
            shutil.move(file, folder_b)
            files_moved += 1
        except shutil.SpecialFileError:
            print("Operation not allowed: Special file cannot be moved.")

    if files_moved == req_files:
        print(f"{files_moved}/{req_files} moved. Operation successful.")
    else:
        print(f"{files_moved}/{req_files} moved. Operation unsuccessful.")

if __name__ == "__main__":
    print(scraper("https://www.google.com/"))
    file_transfer(r"C:\Users\user\PycharmProjects\Apexcify tasks\Task 1", r"C:\Users\user\PycharmProjects\Apexcify tasks\Task 5")