"""   Server / Sender Side   """

import os
import json
import socket
import time

# Defining some Global Variables
CHUNK = 1024

class server:

	def __init__(self):
		########################

		# Defining Hostname and Port
		try:
			self.host = self.__getIP__()
		except:
			self.host = input("\nSpecify host's URL or IP-Address \n(just press enter to use default): ")
			if self.host is None:
				self.host = '127.0.0.1'
		
		# Creating Socket
		self.sockServer = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
		self.sockServer.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
		
		self.host = socket.gethostbyname(self.host)
		self.port = 55555

		# file(s') header
		self.headerDetails = {}
		# list of files that are to be send
		self.filelist = []
		self.caretCompression = False

		#########################

		# Binding socket with the host and port
		self.sockServer.bind((self.host, self.port))
		self.sockServer.listen(5)

		print('Server up at {0}'.format(self.host))
		
		#########################
		
		# Accepting the Connections of the client willing to connect
		self.connection, self.address = self.sockServer.accept()
		print(f"Connection from {self.address} (receiver) has been established!!!")

	# to auto detect the ip-address
	def __getIP__(self):
		os.system("ifconfig | grep broadcast | cat | tail -1 > ip.txt")
		with open('ip.txt', 'r') as f:
			line = f.read()
		addrinfo = ' '.join(line.split())
		ipaddr = addrinfo.split(' ')[1]
		os.system("rm ip.txt")
		return ipaddr

	def __loadFiles__(self):
		# Getting the filenames from the Input to send to the client
		totalFiles = int(input("How many files you want to share: "))
		filenames = []

		for i in range(totalFiles):
			filename = input("Enter the name (including complete path) of file-{}: ".format(i+1))
			filenames.append(filename)
		
		# to compress if user is sending 
		# multiple files in compressed form
		if totalFiles > 1:
			wannaCompress = input("Wanna compress all files, it's even faster! (y/n): ")
			if wannaCompress in ['y','Y']:
				filenames = self.compressAll(filenames) # list of 1 element
		
		return filenames

	def compressAll(self,fileNames):
		## assuming all the files have unique names
		## even if they are from diff. directory

		# making a compression directory
		os.system("mkdir caterCompressed")

		# coplying all files in this dir
		for fileName in fileNames:
			if '/' in fileName:
				newFileName = fileName.split('/')[-1]
			else:
				newFileName = fileName
			os.system("cp {} ./caterCompressed/{}".format(fileName, newFileName))
		
		# compressing the new dirctory
		# this uniquename means that client will have to do auto-extract 
		os.system("tar -cvjf caterCompressed.tar.bz2 ./caterCompressed/ > /dev/null") 
		print("Your files are successfully compressed as 'caterCompressed.tar.bz2'")

		## setting flag for post share removal of folder/file
		self.caretCompression = True
		
		return ['caterCompressed.tar.bz2']

	def definingHeader(self):
		self.filelist = self.__loadFiles__()

		i = 1
		tempHeader = {}
		
		# Defining Data Dictionary Meta Data
		for filename in self.filelist:
			# Checking File Size
			filesize = os.stat(filename).st_size

			# Defining header to send as MetaData
			tempHeader[i] = {
								'filename' : filename,
								'filesize' : filesize,
							}
			i += 1

		return tempHeader
	
	def printHeader(self):
		print("\nSharing:\n") # printing from next line
		print("{")
		for fileHeaderIndex in self.headerDetails:
			if int(fileHeaderIndex) != len(self.headerDetails):
				print("\t{}: {},".format(str(fileHeaderIndex), self.headerDetails[fileHeaderIndex]))
		print("\t{}: {}".format(str(fileHeaderIndex), self.headerDetails[fileHeaderIndex]))
		print("}")


	def server(self):		
		self.headerDetails = self.definingHeader()	# Calling function to defining the Header
		st = time.time()

		# Sending dictionary after converting into json object as byte data
		self.connection.send(bytes(json.dumps(self.headerDetails).encode()))
		self.printHeader()

		# Looping over the list to send all the files in list
		for filename in self.filelist:

			# Opening and Reading the first chunk of file bytes
			with open(filename, 'rb') as f:
				fileData = f.read(CHUNK)

				# No Indentation Error Check
				while fileData:
					if not fileData:
						break
					# Sending Data through the connection to the client
					self.connection.send(fileData)
					# Reading the other chunks of the file bytes
					fileData = f.read(CHUNK)

			f.close()	# Closing the file

		et = time.time()
		timeTaken = et-st
		print("\nFile(s) shared in {0:.5f} seconds!\n".format(timeTaken)+"-"*12)

		## removing generated files if compression was done by cater
		if self.caretCompression:
			os.system("rm -rf caterCompressed")
			os.system("rm caterCompressed.tar.bz2")
		
		self.connection.close()	# Closing the connection


