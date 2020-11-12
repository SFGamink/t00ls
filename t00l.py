clear
b="\033[1m"
u="\033[4m"
bl="\033[30m"
r="\033[31m"
g="\033[32m"
bu="\033[34m"
m="\033[35m"
c="\033[36m"
w="\033[37m"
endc="\033[0m"
enda="\033[0m"
blue="\033[1;34m"
cyan="\033[1;36m"
red="\033[1;31m"
figlet "Surya Gumawang"
echo "Selamat datang di tools kami" |lolcat
echo $c " ========================================== ${endc}";
echo $c "  ████████╗░█████╗░░█████╗░██╗░░░░░░██████╗ ${endc}";
echo $c "  ╚══██╔══╝██╔══██╗██╔══██╗██║░░░░░██╔════╝ ${endc}";
echo $c "  ░░░██║░░░██║░░██║██║░░██║██║░░░░░╚█████╗░ ${endc}";
echo $c "  ░░░██║░░░██║░░██║██║░░██║██║░░░░░░╚═══██╗ ${endc}";
echo $c "  ░░░██║░░░╚█████╔╝╚█████╔╝███████╗██████╔╝ ${endc}";
echo $c "  ░░░╚═╝░░░░╚════╝░░╚════╝░╚══════╝╚═════╝░ ${endc}";
echo $c " ========================================== ${endc}";

echo  "[+]===========================================[+]" |lolcat
echo  "[+] Tools     : SFGamink $white               [+] " |lolcat
echo  "[+] Author   : Surya Gumawang $white          [+] " |lolcat
echo  "[+]===========================================[+]" |lolcat

echo $r"•••••••••••••••••••••••••••••••••••••••••••••${endc}";
echo   "##### Kumpulan Tools SFGamink #####" |lolcat
echo $r"•••••••••••••••••••••••••••••••••••••••••••••${endc}";

trap ctrl_c INT
ctrl_c() {
clear
echo  $red"[#]> (Ctrl + C ) Detected,
Trying To Exit ... "
echo  $cyan"[#]> SUNDANESE"
sleep 1
echo ""
echo  $white"[#]> semoga bermanfaat :)"
sleep 1
exit
}
lagi=1
while [ $lagi -lt 6 ];
do
sleep 1
echo ""
echo  "=========================================" |lolcat
echo  $r "1.  CAMERA CCTV                        [÷]${endc}";
echo  $g "2.  FB MASSAL TANPA LOGIN              [÷]${endc}";
echo  $c "3.  C4LL                               [÷]${endc}";
echo  $r "00. Exit                               [÷]${endc}";
echo  "=========================================" |lolcat
echo ""
echo  "╭─SFGamink" |lolcat
read -p "╰─#" pil;

#CAMERA CCTV

1) apt update && apt upgrade
clear
figlet "SFGamink"
pkg install python3
pip3 install requests
pip3 install colorama
git clone https://github.com/SFGamink/sia
cd sia
python3 cctv.py

;;

#FB MASSAL TANPA LOGIN

2) apt update && apt upgrade
clear
figlet "SFGamink"
pkg install python2
git clone https://github.com/SFGamink/surya
cd surya
python2 uya.py

;;

#C4LL

3) apt update && apt upgrade
clear
figlet "SFGamink"
pkg install python
pip install requests
gem install ruby
pkg install php
pip install bash
pkg install git
git clone https://github.com/SFGamink/C4LL
cd C4LL
python2 c4ll.py

;;

00) clear
figlet "SFGamink" |lolcat
echo "Good bye" |lolcat
echo "Jangan Bosen Untuk Memakai Tools Ini" |lolcat
exit

;;

*) echo  $g "SALAH!!!,
EWH PILIHANNA!
TUNGGUAN UPDATENA
esac
done
done
