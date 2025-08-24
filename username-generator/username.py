# username-generator/username.py

# Ask user details
nick = input("Enter your nickname: ").strip()
real = input("Enter your real name (first name only): ").strip().lower()

# Generate a few possible usernames
username1 = nick.lower() + "_" + real
username2 = real[:3] + nick.lower()
username3 = nick.lower() + str(len(real))

# Show suggestions
print("\nHere are some cool username ideas for you:")
print("1.", username1)
print("2.", username2)
print("3.", username3)
