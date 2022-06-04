import argparse
import requests, json
import pyfiglet
import sys
from sys import argv
import os

BLACK = '\033[30m'
red = '\033[31m'
bold = '\033[01m'
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
print(GREEN+"Escribe el numero de telefono junto\ncon el prefijo, ejemplo: +523313002435\n")
# Información

number = input(GREEN+"Numero de telefono: "+RESET)

api_url = 'http://apilayer.net/api/validate?access_key=71c9a91b73291f84764eda1c5ccba175%s&number=%s&country_code&format=1'

data = requests.get(api_url+number)
sys.stdout.flush()
a = LGREEN+bold+"[$]"
b = CYAN+bold+"[$]"
print("")
print (b, "[Número]:", data["number"])
print(red+"<--------------->"+red)
print (a, "[Local]:", data["local_format"])
print(red+"<--------------->"+red)
print (b, "[Internacional]:", data["international_format"])
print(red+"<--------------->"+red)
print (a, "[Prefijo]:", data["country_prefix"])
print(red+"<--------------->"+red)
print (b, "[Codigo de país]:", data["country_code"])
print(red+"<--------------->"+red)
print (a, "[País]:", data["country_name"])
print(red+"<--------------->"+red)
print (b, "[Ubicación]:", data["location"])
print(red+"<--------------->"+red)
print (a, "[Transportador]:", data["carrier"])
print(red+"<--------------->"+red)
print (b, "[Tipo de línea]:", data["line_type"])
print(red+"<--------------->"+red)

for key, value in data.json().items():

    print("%s: %s" % (key, value))
