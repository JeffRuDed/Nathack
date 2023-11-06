#!/data/data/com.termux/files/usr/bin/bash

cd $HOME
echo
echo -e "\e[93mThis script will install Nathack in Termux."
echo
echo -e "\e[32m[*] \e[34mDownloading..."
termux-setup-storage -y
apt install python3 -y
apt install megacmd -y
apt install git -y
pip install pystyle
pip install requests
git clone "https://github.com/JeffRuDed/Nathack"
echo -e "\e[32m[*] \e[34mKeep downloading.."
cd Nathack
mega-get "https://mega.nz/file/mOwQTBAD#8jbpPYRbHDhJx8n5z1gR4ovf5JFtZrzqsPhROLD_L_A"
cd $HOME/Nathack
echo -e "\e[32m[*] \e[34mCreating workspace directory..."
cd $HOME
cd Nathack
chmod +x main.py
echo -e "\e[32m[*] \e[34mCleaning up..."
rm -rf NatInstall.sh
echo
echo -e "\e[32mNathack was successfully installed!\e[39m"
echo
python3 main.py
