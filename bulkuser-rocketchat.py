import requests

# Configuration
api_url = "https://your-rocketchat-url/api/v1/users.create"
headers = {
    "X-User-Id": "USER-ID",
    "X-Auth-Token": "Auth-Token",
    "Content-Type": "application/json"
}
password = "DefaultPassword"  # Replace with a secure default password


# Read the usernames and names from files
with open('username.txt', 'r') as username_file, open('names.txt', 'r') as names_file:
    # Strip spaces from usernames and split lines
    usernames = [line.strip() for line in username_file.read().splitlines()]
    names = names_file.read().splitlines()

# Check if the number of usernames and names match
if len(usernames) != len(names):
    print("The number of usernames and names do not match.")
    exit()

# Create users
for username, name in zip(usernames, names):
    email = f"{username}@yourdomain.com"
    payload = {
        "name": name,
        "email": email,
        "password": password,
        "username": username,
        "active": True,
        "roles": ["user"],
        "requirePasswordChange": True,
        "setRandomPassword": False,
        "sendWelcomeEmail": False,
        "verified": False
    }

    response = requests.post(api_url, headers=headers, json=payload)

    if response.status_code == 200:
        print(f"Successfully created user: {username}")
    else:
        print(f"Failed to create user: {username} - {response.text}")

print("User creation process completed.")
