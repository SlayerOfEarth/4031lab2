#!/usr/bin/env python3
import sys

print("Printing out User Data:\n")

for line in sys.stdin:
    # Strip whitespace and skip empty lines or lines starting with '#'
    line = line.strip()
    
    if not line or line.startswith('#'):
        continue

    # tuple unpacking to assign variables to parts
    try:
        username, password, userid, groupid = map(str.strip, line.split(':'))
        print(f"The user {username} has a password of {password} and has userid {userid} and groupid {groupid}")
    except ValueError:
        print(f"Skipping invalid line: {line}")

print("\nEnd of User Data")

