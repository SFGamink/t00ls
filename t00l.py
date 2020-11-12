#Coded By SFGamink

import os,sys,time


def main():
    time.sleep(1)
    os.system ('clear')
    print '[96m'
    os.system ('figlet TOOLS')
    print'[92m================================='
    print'[97m Tools   :[96mSFGamink '
    print'[97m Author  :[96mSurya Gumawang '
    print'[92m================================='
    print'[92m++++++++++++ [97mTOOLS [92m++++++++++++'
    print'[92m[[97m1[92m] [97mCAMERA CCTV '
    print'[92m[[97m2][92m [97mFB TANPA LOGIN '
    print'[92m[[97m3[92m] [97mC4LL '
    print'[92m[[91m0[92m] [91mExit '
    gans = raw_input ('[97m=SFGAMINK=>[93m ')
    if gans in ['1']:
        time.sleep(1)
        os.system ('git clone https://github.com/SFGamink/sia')
        os.system ('pkg install python3')
        os.system ('pip3 install requests')
        os.system ('pip3 install colorama')
        os.system ('cd sia')
        os.system ('python3 cctv.py')
    if gans in ['2']:
        time.sleep(1)
        os.system ('git clone https://github.com/SFGamink/surya')
        os.system ('cd surya')
        os.system ('python2 uya.py')
    if gans in ['3']:
        time.sleep(1)
        os.system ('git clone https://github.com/SFGamink/C4LL')
        os.system ('pkg install python')
        os.system ('pip install requests')
        os.system ('gem install ruby')
        os.system ('pkg install php')
        os.system ('pip install bash')
        os.system ('cd C4LL')
        os.system ('python c4ll.py')
    else:
        time.sleep(1)
        print '[97m Pilih CING Bener [92mNJIRR . . .'
        time.sleep(1)
        main()

main()
 
