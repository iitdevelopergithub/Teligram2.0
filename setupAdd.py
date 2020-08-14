import os, sys
import configparser
re="\033[1;31m"
gr="\033[1;32m"
cy="\033[1;36m"
def banner():
	os.system('clear')
	print(f"""
      	{re}╦ ╦ ╔╦╗{cy}╔═╗ ┌─┐ ┬ ┬ ╔═╗ ║  ╔═╗ ┌─┐┌─┐┬─┐
        {re}║ ║  ║ {cy}║ ║ ├┤  │ │ ├┤  ║  ║ ║ ├─┘├┤ ├┬┘
        {re}╩ ╩  ╩ {cy}╚═╝ └─┘  ─  ╚═╝ ╚═ ╚═╝ ┴  └─┘┴└─
 
            version : 2.0
     {re} IIT {cy} DEVELOPER 
	{re}╔═╗{cy}┌─┐┌┬┐┬ ┬┌─┐
	{re}╚═╗{cy}├┤  │ │ │├─┘
	{re}╚═╝{cy}└─┘ ┴ └─┘┴
	""")
banner()
#img = Image.open('TelegramBanner.jpg')    
#img.show() 
print(gr+"[+] Installing requierments ...")
banner()
os.system("touch configAdd.data")
cpass = configparser.RawConfigParser()
cpass.add_section('cred')
xid = input(gr+"[+] enter api ID : "+re)
cpass.set('cred', 'id', xid)
xhash = input(gr+"[+] enter hash ID : "+re)
cpass.set('cred', 'hash', xhash)
xphone = input(gr+"[+] enter phone number : "+re)
cpass.set('cred', 'phone', xphone)
setup = open('configAdd.data', 'w')
cpass.write(setup)
setup.close()
print(gr+"[+] setup for Add Member  complete !")
print(gr+"[+] now you can run any tool !")
print(gr+"[+] make sure to read docs 4 installation & api setup")
print(gr+"[+] https://github.com/iitdevelopergithub/Telegram-hack/edit/master/README.md")
