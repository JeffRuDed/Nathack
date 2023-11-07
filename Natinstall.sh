#!/data/data/com.termux/files/usr/bin/bash
cd $HOME
echo
echo -e "\e[93mThis script will install Nathack in Termux."
echo
echo -e "\e[32m[*] \e[34mDownloading..."
termux-setup-storage -y
apt install python3 -y
apt install megacmd -y
if [ ! -d "Nathack" ]; then
  apt install git -y
fi
pip install pystyle
pip install requests
git clone "https://github.com/JeffRuDed/Nathack"
clear
echo -e "\e[32m[*] \e[34mKeep downloading.."
cd Nathack
echo -e "\e[32m[*] \e[34mSetting Permissions..."
cd $HOME/Nathack
chmod +x main.py
echo -e "\e[32m[*] \e[34m Finishing up..."
# SCRIPT BY @OSLEP FOR NATNONI
if [ ! -f "instagram.txt" ]; then
  mega-get "https://mega.nz/file/mOwQTBAD#8jbpPYRbHDhJx8n5z1gR4ovf5JFtZrzqsPhROLD_L_A"
fi
echo -e "\e[32mNathack was successfully installed!\e[39m"
echo
clear
python3 main.py