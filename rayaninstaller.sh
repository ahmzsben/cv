#!/bin/bash

echo "  _____             __     __      _   _ "
echo " |  __ \     /\     \ \   / //\   | \ | |"
echo " | |__) |   /  \     \ \_/ //  \  |  \| |"
echo " |  _  /   / /\ \     \   // /\ \ | .   |"
echo " | | \ \  / ____ \     | |/ ____ \| |\  |"
echo " |_|  \_\/_/    \_\    |_/_/    \_\_| \_|"
echo ""


echo "   Happy Scanning Script by: RA YAN "
echo "            @RAYANDIAG               "
echo "      https://t.me/RAYANDIAG     "


echo "This is a the script installer"

pkg remove game-repo -y
pkg remove science-repo -y

pkg install grep -y
pkg install golang -y
pkg install openssl -y
pkg install python -y && pip install requests

echo 'PATH="$PATH:$HOME/go/bin"' >> $HOME/.bashrc && source $HOME/.bashrc

go install -v github.com/projectdiscovery/subfinder/v2/cmd/subfinder@latest


go install -v github.com/aztecrabbit/bugscanner-go@latest

echo "##################"

echo "the installation was successful"


