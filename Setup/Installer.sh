#!/bin/bash

cd ~
sudo apt-get update
sudo apt-get install python-serial -y
sudo apt-get install libpng12-dev -y
sudo apt-get install python-gpiozero -y
sudo apt-get install python-pkg-resources python3-pkg-resources -y
cd ~
sudo chmod 755 /home/pi/GBA-SPi/BatteryMonitor/Pngview/pngview
sudo systemctl disable hciuart

cd
curl -O https://raw.githubusercontent.com/adafruit/Raspberry-Pi-Installer-Scripts/master/retrogame.sh
echo '3' | sudo bash retrogame.sh

#install SPI screen
mv SPi_modules /etc/modules
mv SPi_fbtft.conf /etc/modprobe.d/fbtft.conf
sudo apt-get install cmake
git clone https://github.com/tasanakorn/rpi-fbcp
cd rpi-fbcp/
mkdir build
cd build/
cmake ..
make
sudo install fbcp /usr/local/bin/fbcp

cd /home/pi/GBA-SPi/Setup
#move the proper config file for button setups
cp SPi_retrogame.cfg /boot/retrogame.cfg  
#move config.txt
cp SPi_config.txt /boot/config.txt
#move rc.local
cp SPi_rc.local /etc/rc.local
#move modules
cp SPi_modules /etc/modules
#move fbtft.conf
cp SPi_fbtft.conf /etc/modprobe.d/fbtft.conf


#Install I2S
curl -O https://raw.githubusercontent.com/adafruit/Raspberry-Pi-Installer-Scripts/master/i2samp.sh
sudo bash i2samp.sh -y
