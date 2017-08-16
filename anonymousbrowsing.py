#Drag this file to your desktop
#Quick script I made to browse 'anonymously' on Linux
#This uses the service Proxychains and obviously Tor.
#I made this script, but obviously didn't make Proxychains or Tor.
#To use this type "cd Desktop, then type python anonymousbrowsing.py in your terminal"
#AFTER RUNNING THIS SCRIPT ONCE, OPEN TERMINAL, TYPE IN 'service tor start' THEN TYPE IN 'proxychains firefox' THAT IS ALL YOU NEED TO DO AFTER USING IT ONCE. DO NOT RUN THE SCRIPT AGAIN
#If you run the script again, you will need to redo everything, so make sure after running the script once, delete it. 
#When you want to browse anonymously again, all you need to do is type 'service tor start' in terminal, then type in 'proxychains firefox' 
#And you will be browsing anonymously!
import os, time
text = "DNS: When nano pops up, type in nameserver 78.46.223.24 on one line, press enter, and on the other line type in nameserver 162.242.211.137 ctrl + o to save press enter, ctrl + x to quit. Proxychains: Uncomment dynamic_chain by removing the #. Comment out strict_chain by adding a #. Go down till you see socks4 [tab] 127.0.0.1 [space] 9050 under that put in socks5 [tab] 127.0.0.1 [space] 9050. Then do ctrl + o to save, press enter, and ctrl + x to exit."
saveFile = open('instructions.txt', 'w')
saveFile.write(text)
saveFile.close()
print("Changing DNS servers.... Read first part of instructions.txt which is on your desktop. it will tell you what to do")
time.sleep(5)
os.system("sudo rm -r /etc/resolv.conf")
os.system("sudo nano /etc/resolv.conf")
print("Enter password when promted")
os.system("sudo apt-get install tor")
os.system("service tor start")
os.system("sudo apt-get install proxychains")
print("Open instructions.txt which should be on your desktop.")
time.sleep(10)
os.system("sudo nano /etc/proxychains.conf")
os.system("proxychains firefox")

