import requests
import pyfiglet
import os

BLACK = '\033[30m'
RED = '\033[31m'
BOLD = '\033[01m'
GREEN = '\033[32m'
YELLOW = '\033[33m'
BLUE = '\033[34m'
MAGENTA = '\033[35m'
CYAN = '\033[36m'
WHITE = '\033[37m'
RESET = '\033[39m'
LGREEN = '\033[92m'

os.system("clear")
print(YELLOW+

"""
██████╗░░█████╗░██╗░░██╗
██╔══██╗██╔══██╗╚██╗██╔╝
██║░░██║██║░░██║░╚███╔╝░
██║░░██║██║░░██║░██╔██╗░
██████╔╝╚█████╔╝██╔╝╚██╗
╚═════╝░░╚════╝░╚═╝░░╚═╝

██████╗░██╗░░██╗░█████╗░███╗░░██╗███████╗
██╔══██╗██║░░██║██╔══██╗████╗░██║██╔════╝
██████╔╝███████║██║░░██║██╔██╗██║█████╗░░
██╔═══╝░██╔══██║██║░░██║██║╚████║██╔══╝░░
██║░░░░░██║░░██║╚█████╔╝██║░╚███║███████╗
╚═╝░░░░░╚═╝░░╚═╝░╚════╝░╚═╝░░╚══╝╚══════╝

""")

print(MAGENTA+"╚» Sʜᴀᴅᴏᴡ Cᴀᴘᴛᴀɪɴ ☬ «╝")
print("")
print(GREEN+"Escribe el numero de telefono junto\ncon el prefijo, ejemplo: +0123456789\n")
# Información

number = int(input(GREEN+"Numero de telefono: "+RESET))
print("")
data = requests.get("http://apilayer.net/api/validate?access_key=71c9a91b73291f84764eda1c5ccba175&number=%s&country_code&format=1" % (number))

for key, value in data.json().items():

    print("%s: %s" % (key, value))
