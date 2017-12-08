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

#Add necessary lines to the rc.local file
sudo sed -i 's/exit 0/fbcp\&\nexit 0/g' /etc/rc.local
sudo sed -i 's/exit 0/python /home/pi/BatteryMonitor/BatteryMonitor.py\&\nexit 0/g' /etc/rc.local
sudo sed -i 's/exit 0/python /home/pi/BatteryMonitor/shutdown_pi.py\&\nexit 0/g' /etc/rc.local
echo "Modified /etc/rc.local"

#check and modify config.txt
config_txt=/boot/config.txt
echo "Modifying /boot/config.txt..."
if ! grep '^dtparam=spi=on' $config_txt; then
echo 'dtparam=spi=on' >> $config_txt
fi

if ! grep '^disable_overscan=0' $config_txt; then
echo 'disable_overscan=0' >> $config_txt
fi

echo "overscan_scale=1\n" >> $config_txt
echo "enable_uart=1\n" >> $config_txt
echo "dtoverlay=pi3-disable-bt\n" >> $config_txt
echo "dtoverlay=hifiberry-dac\n" >> $config_txt
echo "core_freq=300\n" >> $config_txt
echo "Modified /boot/config.txt

cd /home/pi/GBA-SPi/Setup
#move the proper config file for button setups
cp SPi_retrogame.cfg /boot/retrogame.cfg  
echo "Configured retrogame inputs"


#move modules
cp SPi_modules /etc/modules
echo "Configured /etc/modules"

#move fbtft.conf
cp SPi_fbtft.conf /etc/modprobe.d/fbtft.conf
echo "Configured /etc/modprobe.d/fbtft.conf


#Install I2S
curl -O https://raw.githubusercontent.com/adafruit/Raspberry-Pi-Installer-Scripts/master/i2samp.sh
sudo bash i2samp.sh -y
