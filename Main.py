from email import message
from fileinput import filename
from importlib.resources import contents
from tkinter.filedialog import test
from turtle import delay, speed
from typing_extensions import Self
import requests
import ctypes
import string
import os
import time
import sys
import random, string
from discord import Webhook, RequestsWebhookAdapter
from discord_webhook import DiscordEmbed, DiscordWebhook

import subprocess
if os.name == "nt":
    ctypes.windll.kernel32.SetConsoleTitleW(f"GEN AUNGPAO BY xenoz.xyz#8590 X ") #หลัง Xใส่ชื่อตัวเองได้ ห้ามลบชื่อกู
print("")
def HWID():
    cmd = 'wmic csproduct get uuid'
    uuid = str(subprocess.check_output(cmd))
    pos1 = uuid.find("\\n")+2
    uuid = uuid[pos1:-15]
    return uuid
print(f"Your HWID is {HWID()} ")
mess = "CHECKING YOU HWID..."
def typewriter(message):
        for char in mess:
         sys.stdout.write(char)
         sys.stdout.flush()
         
         time.sleep(0.1)
typewriter(mess)

hwid_auth = requests.get("link hwid") #สร้างpastebin สำหรับเช๊คhwid/เพิ่ม-ลบhwid
if HWID() in hwid_auth.text:
    time.sleep(5)
    os.system('cls')
    print("CORRECT")
    time.sleep(2)
    os.system('cls')
    
    print("Welcome")
    print("""            ██╗░░██╗██████╗░███████╗
            ╚██╗██╔╝╚════██╗██╔════╝
            ░╚███╔╝░░░███╔═╝█████╗░░ 
            ░██╔██╗░██╔══╝░░██╔══╝░░ 
            ██╔╝╚██╗███████╗███████╗
            ╚═╝░░╚═╝╚══════╝╚══════╝ """) #แก้เป็นชื่อตัวเองได้
    
    
    dis="MADE BY: xenoz.xyz#8590 X  \n" #หลัง X ใส่ชื่อตัวเองได้ตรงนี้ห้ามลบชื่อกู
    def typewriter(message):
        for char in dis:
         sys.stdout.write(char)
         sys.stdout.flush()
         time.sleep(0.09)
    typewriter(dis)
  

    def config_read():
        filename = "config.config"
        contents = open(filename).read()
        config = eval(contents)
        link = config['link']
        amount = int(input("amount: "))
        
        for i in range(amount):
            code = https://gift.truemoney.com/campaign/?v= + "".join(random.choices(string.digits, k=18))
            print("[Generated] " + code)
            webhook = Webhook.from_url(link, adapter=RequestsWebhookAdapter())
            webhook.send(code)


    if __name__ == "__main__":
        config_read()   

else:
    print("Your HWID was not found ")
    print("Pls contact admin to add hwid")
    print("or join discord and open ticket")
    
    


 
