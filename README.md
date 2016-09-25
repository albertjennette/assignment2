# assignment2

## How to run
	1. To start, open the terminal of your system.
	
	2. To clone the file directory onto your system, please write git clone https://github.com/albertjennette/assignment2.git /albertjennette
	
	3. Because this program accesses the shadow file of your system, it must be run as a super user. Either login through sudo su or simply type sudo in the same line of the executable command.

	4. This program accepts two arguments. In order to execute a python file the command is python <filename.py>, followed by any arguments. The argument order for this program is the file directory and then the specific user, so an example would resemble python <filename.py> <file or directory> <user>.

	5. After following these steps your command line prompt should be python assignment2.py <shadow file or directory location> <user> or sudo python assignment2.py <shadow file or directory location> <user> if you have not already enabled root access. 

	6. Hit enter to execute.

## Purpose of this progam
	The purpose of this program is very straightforward. It implements a dictionary style password cracking attack to break a specific user's password hash retrieved from a given shadow file.

## How does it work?
	The work of this program is divided into three functions. The organizing main function, accepts two system arguments, the shadow file or its directory location and a specific user within the shadow file who's password we would like to gain access to. With this it then reads the shadow file for the specific user and retrieves the relevant password hash, which is passed to the attack function.  The attack function then breaks down the password hash for crypt type, salt, and the encrypted password. The crypt type is passed to an identifying function which returns what hash type was used (note: while the attack function can theoretically work for any hash type supported by the linux crypt library, the identifier will only recongize SHA-512, SHA-256, Blowfish, and MD5 type hashes). The attack function then opens a standard american english dictionary (the exact txt file can be found in usr/share/dict). Each word is encrypted with the same hash type and salt, and then compared to the encrypted password. Since hashing is 1 to 1, if we know the encryption type and salt, we know that the word blue encrypted with these will always result in the same hash. Thus, if the hashed password and hashed dictionary word match, the word is returned as that is the password. If the password is not in the dictionary text file however, the password can not be guessed (such as through a brute force attack) and "password not found in dictionary" is returned. 
