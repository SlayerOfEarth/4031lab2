#!/usr/bin/env python3
# fileprocessor1.py

# Open the file
with open('fileprocessor.input', 'r') as file:
    # Read each line into a list
    lines = file.readlines()

# Initialize an empty list to store user data and skipped users
user_data = []
skipped_users = []

# Iterate through each line
for line in lines:
    # Check if the line starts with a hashtag
    if line.startswith('#'):
        # Extract the username to be skipped and remove the hashtag
        skipped_user = line.split(':')[0].strip()[1:]
        skipped_users.append(skipped_user)
        continue

    # Split each line into a list using colon as a delimiter
    user_info = line.strip().split(':')

    # Append the user info to the user_data list
    user_data.append(user_info)

# Print the user data
print("Printing out User Data:")
for user_info in user_data:
    username, password, userid, groupid = user_info
    print(f"The user {username} has a password of {password} and has userid {userid} and groupid {groupid}")

# Print the skipped users
if skipped_users:
    print("\nSkipped Users:")
    for skipped_user in skipped_users:
        print(f"{skipped_user} is skipped because it starts with a hashtag (commented out)")

print("\nEnd of User Data")

