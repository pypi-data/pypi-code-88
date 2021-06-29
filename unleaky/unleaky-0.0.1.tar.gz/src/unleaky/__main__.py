# Importing the Necessary Modules

import sqlite3
from time import strftime
from datetime import datetime
from datetime import date
import pyperclip
import os
import sys
import time

def main():
	global master_password
	master_password = "HelloWorld"

	def time_cal():
	    current_t = datetime.now()
	    current_date = str(date.today())
	    current_t_f = current_t.strftime("%H:%M:%S")
	    timeAnddate = (f'{current_t_f} {current_date}')
	    return timeAnddate

	def pwd_gen():
		import random
		import string
		print("Passsword Genenerator")
		pwdlength = int(input("Specify Password Length: "))
		lower = string.ascii_lowercase
		upper = string.ascii_uppercase
		digits = string.digits
		symbols = string.punctuation
		whole =  lower + upper + digits + symbols
		pwd1 = random.sample(whole,pwdlength)
		password = "".join(pwd1)
		password_final = str(password)
		print(f'The password to be used is: {password}')
		pyperclip.copy(password_final)
		print("Passsword Genenerated and Copied to the clipboard")
		return password_final

	def master_password_verify(e, password):
		if e == 1:
			to_verify = str(input("Enter the current master password: "))
			c.execute("SELECT * FROM master_password WHERE master_password = :Password",{
				'Password': to_verify,
			})
			current_master_password = c.fetchone()
			print(f'Your Current Master Password is {current_master_password[0]}')
			new_master_password = str(input("Enter New Master Password: "))
			c.execute("UPDATE master_password SET master_password = :Username WHERE master_password = :Actual", {
				'Username': new_master_password,
				'Actual': current_master_password[0]
				})
			c.execute("SELECT * FROM master_password")
			choice = str.lower(input("Are yous ure you want to change the master password? y/n: "))
			if choice == "y":
				conn.commit()
				print("Changes Will take place after restart")
				time.sleep(2)
				exit()
			else:
				print("Password Not changed")
		if e == 2:
			to_verify = password
			c.execute("SELECT * FROM master_password WHERE master_password = :Password",{
				'Password': to_verify,
			})
			current_master_password = c.fetchone()
			if to_verify == current_master_password[0]:
				return "verified"

	def add_to_db(username, password_given):
		c.execute("INSERT INTO passwords VALUES (:Username, :Password, :_time)",
			{
				'Username': username,
				'Password': password_given,
				'_time': time_cal(),
			})
		conn.commit()

	# Connecting to the database
	conn = sqlite3.connect('unleaky.db')

	# Creating a cursor for operating in the database. This is will act as a literal cursor
	c = conn.cursor()

	try:
		c.execute("""CREATE TABLE master_password(
		    master_password text
		)""")
	except:
		pass
	try:
		# Creating a table
		c.execute("""CREATE TABLE passwords(
		    Username text,
		    Password text,
		    _time text
		)""")
	except:
		pass

	# try:
	print("Hello, Welcome to Unleaky CLI, a simple CLI password manager")
	given_password = str(input("Input Master Password: "))
	while True:
		if master_password_verify(2, given_password) == "verified":
			action = str.lower(input("Enter action or help for help: "))
			print("\n")
			if action == "new":
				username = str(input("Enter UserName: "))
				password_choice = str.lower(input("Do you want to [E]nter new password or [G]enerate it?: "))
				if password_choice == "e":
					password_given = str(input("Enter the password, preferably a strong passphrase: "))
				elif password_choice == "g":
					password_given = pwd_gen()
				# c.execute("INSERT INTO passwords VALUES (username, password_given, time_cal())")
				add_to_db(username, password_given	)
			if action == "read":
				c.execute('SELECT rowid, * FROM passwords')
				usernames = c.fetchall()
				print("User Entries So far\n\n")
				print("INDEX \t USERNAME \t PASSWORD \t\t TIME\n")
				for username in usernames:
					print(f'{username[0]} | {username[1]} | {username[2]} | {username[3]}\n')
			if action == "generate":
				pwd_gen()
			if action == "update":
				username_to_update = str(input("Enter the Username that you want to change: "))
				try:
					c.execute("SELECT * FROM passwords WHERE Username = :Username",{
						'Username': username_to_update,
						})
					actual_username_list = c.fetchone()
					actual_username = actual_username_list[0]
					if username_to_update == actual_username:
						choice_to_update = str.lower(input("What Parameter do you want to update? [U]sername or [P]assword or [B]oth? "))
						if choice_to_update == "u":
							new_username_to_update = str(input(f'Enter the new username for {actual_username}: '))
							c.execute("UPDATE passwords SET Username = :Username WHERE Username = :Actual", {
								'Username': new_username_to_update,
								'Actual': actual_username,
								})
							conn.commit()
							print("Executed Commnad to Update Usernames")
						if choice_to_update == "p":
							password_to_update = str(input("Enter the previous password: "))
							try:
								c.execute("SELECT * FROM passwords WHERE Password = :Password",{
									'Password': password_to_update,
									})
								actual_password_list = c.fetchone()
								actual_password = actual_password_list[1]
								if password_to_update == actual_password:
									new_password_to_update = str(input(f'Enter new password to update for {username_to_update}: '))
									c.execute("UPDATE passwords SET Password = :Password WHERE Password = :Actual", {
										'Password': new_password_to_update,
										'Actual': actual_password,
										})
									conn.commit()
									print("Executed Command to Update Password")
							except:
								print("Failed to execute command, wrong previous password input.")
						if choice_to_update == "b":
							new_username_to_update = str(input(f'Enter the new username for {actual_username}: '))
							c.execute("UPDATE passwords SET Username = :Username WHERE Username = :Actual", {
								'Username': new_username_to_update,
								'Actual': actual_username,
								})
							# conn.commit()
							# print("Executed Commnad to Update Usernames")
							password_to_update = str(input("Enter the previous password: "))
							try:
								c.execute("SELECT * FROM passwords WHERE Password = :Password",{
									'Password': password_to_update,
									})
								actual_password_list = c.fetchone()
								actual_password = actual_password_list[1]
								if password_to_update == actual_password:
									new_password_to_update = str(input(f'Enter new password to update for {username_to_update}: '))
									c.execute("UPDATE passwords SET Password = :Password WHERE Password = :Actual", {
										'Password': new_password_to_update,
										'Actual': actual_password,
										})
								conn.commit()
								print("Executed Commnad to Update Usernames and Passwords")
							except:
								conn.commit()
								print("Executed Commnad to Update Usernames but failed to update password due to wrong previous password input")
				except:
					print(f'No Username {username_to_update} found!, try again by making sure with the read command')
			if action == "copy":
				info_to_copy = str(input("UserName you want to copy: "))
				try:
					c.execute("SELECT * FROM passwords WHERE Username = :Username",{
						'Username': info_to_copy,
						})
					actual_username_list = c.fetchone()
					actual_username = actual_username_list[0]
					if info_to_copy == actual_username:
						username_to_copy = actual_username_list[0]
						password_to_copy = actual_username_list[1]
						pyperclip.copy(username_to_copy)
						# print("Username copied!")
						pyperclip.copy(password_to_copy)
						# print("Password Copied!")
						print("Copy Command Execution Done")
					# print(actual_username_list)
				except:
					print(f'No Username {info_to_copy} found! try again by checking with the read command')
			if action == "admin":
				x = "HelloWorld"
				master_password_verify(1, x)
			if action == "clear":
				try:
					os.system("clear")
				except:
					os.system("cls")
				print("UNLEAKY\nBy NoobScience")
			if action == "quit":
				print("Securely quitting the application...")
				time.sleep(2)
				try:
					os.system("clear")
				except:
					os.system("cls")
				print("Command Line Cleared and Flushed, Feel Free to Close the application or wait for it to close it self,\n")
				print("\nTHANKS FOR USING UNLEAKY\n")
				print("By NoobScience\n")
				time.sleep(5)
				try:
					os.system("clear")
				except:
					os.system("cls")
				exit()
	# except:
	# 	print("Something went wrong, try again or report this issue at https://github.com/newtoallofthis123/unleaky")

	# Commit the command
	conn.commit()

	# Close the connection, just to be safe
	conn.close()

if __name__ == '__main__':
	main()