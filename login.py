import os, sys

print ("\033[1;34mSilahkan Masukkan ID & Password Tool SFGamink")

print ("\033[1;35matau silahkan Hubungi 085659032860 ")
print ("\033[1;32mJgn Ngasal Cok ntr salah ")
ID = 'surya'      

password = 'fadhil'



def restart():

	ngulang = sys.executable

	os.execl(ngulang, ngulang, *sys.argv)



def main():

	uname = raw_input("ID : ")

	if uname == ID:

		pwd = raw_input("password : ")



		if pwd == password:

			print "\034[1;32mSuksess Login To Tool SFGamink..", 

			sys.exit()



		else:

			print "\033[1;32mMaaf Password Anda Salah Silahkeun Coba Lagi... [?]\033[00m"

			print "Silahkan log-in kembali untuk Masuk ke Tool SFGamink...!!\n"

			restart()



	else:

		print "\033[1;32mMaaf  ID Anda salah Silahkeun Check Kembali Untuk Masuk... [?]\033[00m"

		print "Silahkan log-in kembali untuk Login ke Tool SFGamink...!!\n"

		restart()



try:

	main()

except KeyboardInterrupt:

	os.system('clear')

	restart()
