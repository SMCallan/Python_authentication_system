	
import getpass
import hashlib
import os

# This works. It checks for a working file, and if no file exists it creates one. We have a file to save user authentication information into. 
def the_programs_file_system(new_file_name):
	# Check if file exists 
		if os.path.exists(new_file_name):
		# File exists, continue
			print("the file exists")
			return new_file_name
		else:
			# If file doesn't exist we create new one'
			print("the file doesnt exist. It has now been created.")
			# Create new file
			with open(new_file_name, "w") as f:
				return new_file_name

new_file_name = (input("What is the name of the file you want to use? "))
filename = the_programs_file_system(new_file_name)
	
print (filename)				
# It checks the file name, or creates a new file in the name of the searched file.
#-------------------------------------------------------
# This is broken. It needs to be fixed. 
# Create a new user and password. 
def create_a_user():
	username = input("Enter a username : ")
	hashed_password = input("Enter a password: ")
	
# Write the username and hashed password to the text file
	with open(filename, "a") as f:
		f.write(username + ":" + hashed_password + "\n")
	return

#The create_a_user function works, and creates a new user_name and password, adding it to our 'filename' destination.

#create_a_user() comment this is to test the function. 

# Code above is complete, code below requires adaptations. 
# -------------------------------------------------------
#Finally we need to check the file, rather than check the username dictionary, we want to extract the information from 'filename'.

# This is our basic frontdoor access, and requiures a username and password. We can apply hash encryption to secure our users password. 
def authentication(): 
# Create a dictionary of usernames and hashed passwords
	usernames = {}
	# Read authentication details from text file.
	with open(filename, "r") as file:
		for line in file:
			username, hashed_password = line.spkit(":")
			usernames[username] = hashed_password
	#Get authentication details from user. 		
	while True:
		username = input("Enter username : ")
		password = getpass.getpass("Enter password : ")
		#Check is details are valid.
		hashed_password = hashlib.sha256(password.encode()).hexdigest()
		if username in usernames and usernames[username] == hashed_password:
			print("login successful!")
			break
		else:
			print("invalid username or password")
			continue
			#Need to add a break option to create a new user account
#---------------------------------------------

''' The create user and authentication need to be better intergrated. and the details need to be #'ed in the first instance? 

'''



