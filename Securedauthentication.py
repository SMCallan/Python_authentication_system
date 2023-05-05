import getpass
import hashlib

open("passwords.txt", "w")

def create_account():
    # Get the username and password from the user
    username = input("Enter your username: ")
    password = getpass.getpass("Enter your password: ")

    # Hash the password
    hashed_password = hashlib.sha256(password.encode()).hexdigest()

    # Write the username and hashed password to the text file
    with open("passwords.txt", "a") as f:
        f.write(username + ":" + hashed_password + "\n")

    print("Account created successfully!")

def authentication(): 
# Create a dictionary of usernames and hashed passwords
    usernames = {}

    # Read the usernames and hashed passwords from the text file
    with open("passwords.txt", "r") as f:
        for line in f:
            username, hashed_password = line.split(":")
            usernames[username] = hashed_password

    # Get the username and password from the user
    while True:
        username = input("Enter your username: ")
        password = getpass.getpass("Enter your password: ")

        # Check if the username and password are valid
        hashed_password = hashlib.sha256(password.encode()).hexdigest()
        if username in usernames and usernames[username] == hashed_password:
            print("Login successful!")
            break
        else:
            print("Invalid username or password.")
            continue



if __name__ == "__main__":
    # Create an account if the text file does not exist
    if not os.path.exists("passwords.txt"):
        create_account()

    # Run the authentication function

