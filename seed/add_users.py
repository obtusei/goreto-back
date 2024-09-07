import requests
from faker import Faker
import json

# Initialize the Faker instance
fake = Faker()

# Function to generate fake user data


def generate_fake_users(num_users=10):
    users = []
    for _ in range(num_users):
        password = '123#goreto'
        user = {
            "username": fake.user_name(),
            "password1": password,
            "password2": password,
            "first_name": fake.first_name(),
            "last_name": fake.last_name(),
            "email": fake.email()
        }
        users.append(user)
    return users


# URL of the registration endpoint
url = "http://localhost:8000/api/register/"

# Generate data for 10 fake users
users = generate_fake_users(10)

# Register each user
for user in users:
    response = requests.post(url, data=json.dumps(user), headers={
                             'Content-Type': 'application/json'})

    if response.status_code == 201:  # HTTP 201 Created
        print(f"User {user['username']} created successfully.")
    else:
        print(
            f"Failed to create user {user['username']}. Status code: {response.status_code}. Response: {response.text}")

print("User registration process completed.")
