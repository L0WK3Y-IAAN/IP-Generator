import subprocess
import time
import sys
import random

def ipGenerator():
    def generationAnimation():
        subprocess.call(['cls'],shell=True)
        print("[+] Generating IP addresses.")
        animation = "|/-\\"

        for i in range(10):
            time.sleep(0.1)
            sys.stdout.write("\r" + animation[i % len(animation)])
            sys.stdout.flush()
    time.sleep(.5)
    generationAnimation()

    subprocess.call(['cls'],shell=True)
    ipGenNum = int(input("Enter number of IP's to be generated: "))

    def ipList():
        ipArray = [1,'.', 2,'.',3,'.',4]
        ipArray[0] = random.randint(0, 255)
        ipArray[2] = random.randint(0, 255)
        ipArray[4] = random.randint(0, 255)
        ipArray[6] = random.randint(0, 255)
        ipString = ''.join(str(e) for e in ipArray)
        print(ipString)
        
    for i in range(ipGenNum):
        ipList()
        time.sleep(.5)
    print('\n' + "[+] IP generation complete.")
ipGenerator()
