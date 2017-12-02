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
#move the proper config file for button setups
mv SPi_retrogame.cfg /boot/retrogame.cfg  

#Install I2S
curl -O https://raw.githubusercontent.com/adafruit/Raspberry-Pi-Installer-Scripts/master/i2samp.sh
sudo bash i2samp.sh -y <<< $'N\n'


#move config.txt?
mv SPi_config.txt /boot/config.txt
#move rc.local
mv SPi_rc.local /etc/rc.local


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

