import requests
import random

old = random.randint(18, 50)

num_emails = int(input("How many emails do you want to send? "))
email_prefix = input("Enter the email prefix (before the @): ")

# Ask the user which server they want to use
server = input("Enter the email server (gmail, yahoo, outlook, custom): ")
if server == "custom":
    server_domain = input("Enter the custom server domain (e.g. example.com): ")
else:
    server_domain = f"{server}.com"

# Read in the last modified number from the file, if it exists
try:
    with open("num.txt", "r") as f:
        last_modified_num = int(f.read())
except FileNotFoundError:
    last_modified_num = 0

# Set the payload
payload = {
    "age": "",
    "distinctId": "",
    "fromLanguage": "en",
    "identifier": "",
    "initialReferrer": "https://www.duolingo.com/",
    "landingUrl": "https://www.duolingo.com/welcome",
    "name": "",
    "password": "Ahmad,12345",
    "signal": None,
    "timezone": "Asia/Jerusalem",
    "username": None
}

# Send the emails
for i in range(num_emails):
    # Update the email and username in the payload
    email = f"{email_prefix}+{i + last_modified_num + 1}@{server_domain}"
    payload["email"] = email
    payload["username"] = email_prefix
    payload["age"] = old

    response = requests.post("https://www.duolingo.com/2017-06-30/users", json=payload)

    print(f"Sent email to {email} Response code: {response.status_code}")

with open("last_modified_num.txt", "w") as f:
    f.write(str(last_modified_num + num_emails))

print(f"Finished sending {num_emails} emails. Last email sent to {email}.")

input("Press Enter to exit...")
