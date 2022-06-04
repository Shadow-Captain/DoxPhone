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
print("valid: ")
print("number: ")
print("local_format: ")
print("international_format: ")
print("country_prefix: ")
print("country_code: ")
print("country_name: ")
print("location: ")
print("carrier: ")
print("line_type: ")

print (" "+YELLOW)

for key, value in data.json().items():

    print("%s: %s" % (key, value))
