import requests

# Set the URL of the Duolingo sign-up page
url = "https://www.duolingo.com/welcome?isLoggingIn=true"

# Get the number of iterations to send the request from the user
num_iterations = int(input("Enter the number of sign-up requests to send: "))

# Define the base data for the request
base_data = {
    "age": "55",
    "email": "gmail@gmail.com",
    "fromLanguage": "en",
    "identifier": "",
    "initialReferrer": "https://www.duolingo.com/",
    "landingUrl": "https://www.duolingo.com/welcome",
    "name": "",
    "password": "",
    "signal": None,
    "timezone": "Asia/Jerusalem",
    "username": None,
}

# Initialize the counter with the last iteration number stored in a file
try:
    with open("counter.txt", "r") as f:
        counter = int(f.read())
except FileNotFoundError:
    counter = 0

# Send the request in a loop
for i in range(num_iterations):
    # Split the base username into parts around the "@" character
    username_parts = base_data['email'].split("@")

    # Insert the iteration number into the middle of the username
    modified_username = f"{username_parts[0]}+{counter+1}@{username_parts[1]}"

    # Modify the data for this iteration by replacing the username with the modified version
    data = {
        **base_data,
        "email": modified_username
    }

    response = requests.post(url, data=data)
    print(f"Response status code: {response.status_code}")

    # Increment the counter
    counter += 1

# Save the counter to a file for the next time the script is run
with open("counter.txt", "w") as f:
    f.write(str(counter))

# Print the last modified username used
print(f"Last modified username: {modified_username}")
