1. put this folder in ~/home/pi/
2. put autostart.sh in ~/home/pi/ and set 
chmod +x /home/pi/autostart.sh
3. edit /home/pi/.config/lxsession/LXDE/autostart and add this line:
lxterminal --command="/home/pi/autostart.sh"
