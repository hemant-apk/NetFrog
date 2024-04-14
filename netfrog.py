import subprocess
import speedtest
import os


print("""\
  _   _      _   ______               
 | \ | |    | | |  ____|              
 |  \| | ___| |_| |__ _ __ ___   __ _ 
 | . ` |/ _ \ __|  __| '__/ _ \ / _` |
 | |\  |  __/ |_| |  | | | (_) | (_| |
 |_| \_|\___|\__|_|  |_|  \___/ \__, |
                                 __/ |
                                |___/ 

Get your Network Information , Connection speed and Connected Devices in your Network.
""")

# get internet speed using speedtest module

def speed():
    speed_test = speedtest.Speedtest()
    download = speed_test.download() / 1000000 
    upload = speed_test.upload() / 1000000 
    return download,upload;

# GET CONNECTED DEVICES ON YOUR NETWORK

def connected_device():    
    cmd = "arp -a"
    output = subprocess.check_output(cmd)
    return output.decode("utf-8")

# GET NETWORK DETAILS 

def wifi_ssid():
    wifissid = subprocess.check_output(['netsh', 'WLAN', 'show', 'interfaces'])
    wifiname = wifissid.decode('utf-8')
    return wifiname


# My Network Details

print("My Network Details :")
wifi_name = wifi_ssid()
print(wifi_name)


# Network Connected Device Ip & Mac address

print("Connected Devices in Network:")
device = connected_device()
print(device)
 
# Download and upload speed

download,upload = speed()
print("Download Speed : ", download , "Mbps")
print("Upload Speed : ", upload , "Mbps")


# Saving report in txt file

f = open("network-stats.txt", "w+")
f.write("NetFrog Network Report")
f.write("\n")
f.write("\n")
f.write("My Network Details :")
f.write("\n")
f.write(wifi_name)
f.write("\n")
f.write("Connected Device in Network :")
f.write("\n")
f.write(device)
f.write("\n")
f.write("Download Speed : ")
f.write(str(download))
f.write(" Mbps")
f.write("\n")
f.write("Upload Speed : ")
f.write(str(upload))
f.write(" Mbps")        
f.close()

# opening the generated file

os.startfile('network-stats.txt')

print("Thanks for using NetFrog ^_^ ")
