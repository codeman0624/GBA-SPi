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
sudo bash retrogame.sh -2

#move the proper config file for button setups
mv SPi_retrogame.cfg /boot/retrogame.cfg  
#move config.txt?
    
#move rc.local
mv SPi_rc.local /etc/rc.local
