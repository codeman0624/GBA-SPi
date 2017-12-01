#!/bin/bash

cd ~
sudo apt-get update
sudo apt-get install python-serial -y
sudo apt-get install libpng12-dev -y
sudo apt-get install python-gpiozero -y
sudo apt-get install python-pkg-resources python3-pkg-resources -y
cd ~
sudo chmod 755 /home/pi/BatteryMonitor/Pngview/pngview
sudo sed -i '/\"exit 0\"/!s_exit 0_python /home/pi/BatteryMonitor/BatteryMonitor.py \&\nexit 0_g' /etc/rc.local
sudo sed -i '/\"exit 0\"/!s_exit 0_python /home/pi/BatteryMonitor/shutdown_pi.py \&\nexit 0_g' /etc/rc.local
sudo systemctl disable hciuart

config_txt=/boot/config.txt
echo "Enabling hardware UART..."
if ! grep '^dtoverlay=pi3-disable-bt' $config_txt; then
  echo 'dtoverlay=pi3-disable-bt' >> $config_txt
else
  echo "Hardware UART already enabled"
fi
