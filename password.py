import os, sys

print ("\033[1;33mAbuskeun ID&PW :)")

print ("\033[1;33mTools Ini Ga Gratis ;)")
print ("\033[1;33mPM No 085659032860")
ID = 'UYA'      
PW = 'FADHIL'

def restart():
	ngulang = sys.executable
	os.execl(ngulang, ngulang, *sys.argv)

def main():
	uname = raw_input("ID : ")
	if uname == ID:
		pwd = raw_input("PW : ")

		if pwd == PW:
			print "\n\033[1;34mWILUJENG SUMPING", 
			sys.exit()

		else:
			print "\n\033[1;36mPASSWORD SALAH!!!\033[00m"
			print "Back Login\n"
			restart()

	else:
		print "\n\033[1;36mID SALAH!!!\033[00m"
		print "Back Login\n"
		restart()

try:
	main()
except KeyboardInterrupt:
	os.system('clear')
	restart()
