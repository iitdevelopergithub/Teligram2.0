from telethon.sync import TelegramClient
from telethon.tl.functions.messages import GetDialogsRequest
from telethon.tl.types import InputPeerEmpty, InputPeerChannel, InputPeerUser
from telethon.errors.rpcerrorlist import PeerFloodError, UserPrivacyRestrictedError
from telethon.tl.functions.channels import InviteToChannelRequest
import sys
import csv
import traceback
import time
import random
import os, sys
import configparser
import msvcrt #Here the key used to exit the loop was <ESC>, chr(27).
re="\033[1;31m"
gr="\033[1;32m"
cy="\033[1;36m"
def banner():
	os.system('clear')
	print(f"""
       	{re}╦ ╦ ╔╦╗{cy}╔═╗ ┌─┐ ┬ ┬ ╔═╗ ║  ╔═╗ ┌─┐┌─┐┬─┐
        {re}║ ║  ║ {cy}║ ║ ├┤  │ │ ├┤  ║  ║ ║ ├─┘├┤ ├┬┘
        {re}╩ ╩  ╩ {cy}╚═╝ └─┘  ─  ╚═╝ ╚═ ╚═╝ ┴  └─┘┴└─
            version : 1.0
     {re} welcome to  IIT {cy} DEVELOPER 
	""")
banner()
print(gr+"[+] Welcome to IIT DEVELOPER This is created by IIT DEVELOPER Team")


api_id = input(gr+"[+] Enter Your Id:"+re)#1599918  #Enter Your 7 Digit Telegram API ID.
api_hash = input(gr+"[+] Enter Your Hash Key: "+re)#'741c483b128c763e5e26a54579329ebb'   #Enter Yor 32 Character API Hash
phone = input(gr+"[+] Enter Your Number: "+re)#'+919005552324'   #Enter Your Mobilr Number With Country Code.
client = TelegramClient(phone, api_id, api_hash)
async def main():
    # Now you can use all client methods listed below, like for example...
    await client.send_message('me', 'WELCOME TO IIT DEVELOPER TELEGRAM SOFTWARE ANY QUEARY CALL US 9005552324 ')


SLEEP_TIME_1 = 100
SLEEP_TIME_2 = 100
with client:
    client.loop.run_until_complete(main())
client.connect()
if not client.is_user_authorized():
    client.send_code_request(phone)
    client.sign_in(phone, input('40779'))

users = []
with open(r"members.csv", encoding='UTF-8') as f:  #Enter your file name 
    if msvcrt.kbhit():
	if ord(msvcrt.getch()) == 27:
	   break
    rows = csv.reader(f,delimiter=",",lineterminator="\n")	
    next(rows, None)
    for row in rows:
        user = {}
        user['username'] = row[0]
        user['id'] = int(row[1])
        user['access_hash'] = int(row[2])
        user['name'] = row[3]
        users.append(user)

chats = []
last_date = None
chunk_size = 200
groups = []

result = client(GetDialogsRequest(
    offset_date=last_date,
    offset_id=0,
    offset_peer=InputPeerEmpty(),
    limit=chunk_size,
    hash=0
))
chats.extend(result.chats)

for chat in chats:
    try:
        if chat.megagroup == True:
            groups.append(chat)
    except:
        continue

print('Choose a group to add members:')
i = 0
for group in groups:
    print(str(i) + '- ' + group.title)
    i += 1

g_index = input("Enter a Number: ")
target_group = groups[int(g_index)]

target_group_entity = InputPeerChannel(target_group.id, target_group.access_hash)
mode = int(input("Enter 1 to add by username \nEnter  2 to add by ID: "))
n = 0
for user in users:
    n += 1
    if n % 80 == 0:
        time.sleep(60)
    try:
        print("Adding {}".format(user['id']))
        if mode == 1:
            if user['username'] == "":
                continue
            user_to_add = client.get_input_entity(user['username'])
        elif mode == 2:
            user_to_add = InputPeerUser(user['id'], user['access_hash'])
        else:
            sys.exit("Invalid Mode Selected. Please Try Again.")
        client(InviteToChannelRequest(target_group_entity, [user_to_add]))
        print("Waiting for 60-180 Seconds...")
        time.sleep(random.randrange(0, 5))
    except PeerFloodError:
        print("Getting Flood Error from telegram. Script is stopping now. Please try again after some time.")
        print("Waiting {} seconds".format(SLEEP_TIME_2))
        time.sleep(SLEEP_TIME_2)
    except UserPrivacyRestrictedError:
        print("The user's privacy settings do not allow you to do this. Skipping.")
        print("Waiting for 5 Seconds...")
        time.sleep(random.randrange(0, 5))
    except:
        traceback.print_exc()
        print("Unexpected Error")
        continue
