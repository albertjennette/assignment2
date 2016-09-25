import os,sys
import crypt

def identifyCrypt(crypType):
	if crypType == '6':
		print "Hash type SHA-512 detected..."
	elif crypType == '5':
		print "Hash type SHA-256 detected..."
	elif crypType == '2':
		print "Hash type Blowfish detected..."
	elif crypType == '1': 
		print "Hash type MD5 detected..."
	else:
		print "Hash type too old or not recognized..."
		exit

def dictAttack(cryptPass):
	hash = cryptPass.split("$")
	crypType = hash[1]
	salt = "$"+crypType+"$"+hash[2]+"$"
	identifyCrypt(crypType)
	dict = open ('american-english',"r")
	for word in dict.readlines():
		word=word.strip('\n')
		cryptWord = crypt.crypt(word, salt)
		if (cryptWord == cryptPass):
			print "Found password: "+word
			return
	print "Password not in dictionary"
	exit
	
def main():
	filePath = sys.argv[1]
	user = sys.argv[2]
	if filePath ==  None:
		print "No file path given ..."
		exit 
	else:
		passFile = open (filePath,'r')
		for line in passFile.readlines():
			line = line.replace("\n","").split(":")
			if user in line:
				cryptPass = line[1]
		dictAttack(cryptPass)
main()

	

