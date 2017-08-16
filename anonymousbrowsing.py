#Quick script I made to browse 'anonymously' on Linux
#This uses the service Proxychains and obviously Tor.
#I made this script, but obviously didn't make Proxychains or Tor.
#To use this type "cd Desktop, then type python anonymousbrowsing.py in your terminal"

import os, time
text = "DNS: When nano pops up, type in nameserver 78.46.223.24 on one line, press enter, and on the other line type in nameserver 162.242.211.137 ctrl + o to save press enter, ctrl + x to quit. Proxychains: Uncomment dynamic_chain by removing the #. Comment out strict_chain by adding a #. Go down till you see socks4 [tab] 127.0.0.1 [space] 9050 under that put in socks5 [tab] 127.0.0.1 [space] 9050. Then do ctrl + o to save, press enter, and ctrl + x to exit."
saveFile = open('instructions.txt', 'w')
saveFile.write(text)
saveFile.close()
print("Changing DNS servers.... Read first part of instructions.txt which is on your desktop. it will tell you what to do")
time.sleep(5)
os.system("sudo rm -r /etc/resolv.conf")
os.system("sudo nano /etc/resolv.conf")

print("Run this script on your desktop.")
print("Enter password when promted")
os.system("sudo apt-get install tor")
os.system("service tor start")
os.system("sudo apt-get install proxychains")
print("Open instructions.txt which should be on your desktop.")
time.sleep(10)
os.system("sudo nano /etc/proxychains.conf")
os.system("proxychains firefox")

