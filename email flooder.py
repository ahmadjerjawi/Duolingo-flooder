import requests

# Set the URL of the Duolingo sign-up page
url = "https://mega.nz/register"
import requests

# Get the number of iterations to send the request from the user
num_iterations = int(input("Enter the number of sign-up requests to send: "))

# Define the base data for the request
base_data = {
    "identifier": "email@mail.com",
}

# Initialize the counter with the last iteration number stored in a file
try:
    with open("counter.txt", "r") as f:
        counter = int(f.read())
except FileNotFoundError:
    counter = 0

# Read the list of proxies from a file or a URL
proxies = []

# Option 1: Read the proxies from a file
try:
    with open("proxies.txt", "r") as f:
        for line in f:
            proxy = line.strip()
            if proxy:
                proxies.append(proxy)
except FileNotFoundError:
    pass

# Option 2: Get the proxies from a URL
if not proxies:
    try:
        response = requests.get("http://example.com/proxies")
        for line in response.text.split("\n"):
            proxy = line.strip()
            if proxy:
                proxies.append(proxy)
    except Exception as e:
        print(f"Error getting proxies: {e}")

# Send the request in a loop
for i in range(num_iterations):
    # Split the base username into parts around the "@" character
    username_parts = base_data['identifier'].split("@")

    # Insert the iteration number into the middle of the username
    modified_username = f"{username_parts[0]}+{counter + 1}@{username_parts[1]}"

    # Modify the data for this iteration by replacing the username with the modified version
    data = {
        **base_data,
        "identifier": modified_username
    }

    # Select a proxy from the list
    proxy = proxies[i % len(proxies)]

    # Send the request using the selected proxy
    response = requests.post(url, data=data, proxies={"http": proxy, "https": proxy})
    print(f"Response status code: {response.status_code} (proxy: {proxy})")

    # Increment the counter
    counter += 1

# Save the counter to a file for the next time the script is run
with open("counter.txt", "w") as f:
    f.write(str(counter))