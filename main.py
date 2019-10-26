import asyncio
import logging
import re
import time
import os
import sys
import random

logging.basicConfig(level=logging.ERROR)

from telethon import TelegramClient, events
from telethon.tl.functions.channels import JoinChannelRequest
from telethon.tl.functions.messages import GetBotCallbackAnswerRequest
from datetime import datetime
from colorama import Fore, init as color_ama
color_ama(autoreset=True)

os.system('cls' if os.name=='nt' else 'clear')

# Get your own values from my.telegram.org
api_id = 800812
api_hash = 'db55ad67a98df35667ca788b97f771f5'

forecast_channel = '@ETH_Forecast_Group'
forecast_group = '@ETH_Forecast_Group'

def print_msg_time(message):
	print('[' + Fore.CYAN + f'{datetime.now().strftime("%H:%M:%S")}' + Fore.RESET + f'] {message}')

async def main():
	print(Fore.MAGENTA + ' _       _      _           _			')
	print(Fore.MAGENTA + '| |_ ___| | ___| |__   ___ | |_		')
	print(Fore.MAGENTA + '| __/ _ \ |/ _ \  _ \ / _ \| __|		')
	print(Fore.MAGENTA + '| ||  __/ |  __/ |_) | (_) | |_	')
	print(Fore.MAGENTA + ' \__\___|_|\___|_.__/ \___/ \__| ' + 'forecast' + '\n' )
	
	print(Fore.BLUE + ' ========================================  ' + Fore.RESET)
	print(Fore.GREEN + ' ammarabdullahalzahid@gmail.com -   ' + Fore.RESET)
	print(Fore.BLUE + ' ======================================== \n' + Fore.RESET)
	
	# Check if phone number is not specified
	if len(sys.argv) < 2:
		print('Usage: python start.py phone_number')
		print('-> Input number in international format (example: +639162995600)\n')
		e = input('Press any key to exit...')
		exit(1)
		
	phone_number = sys.argv[1]
	choice1 = '/u'
	choice2 = '/u'
	
	if not os.path.exists("session"):
		os.mkdir("session")
   
    # Connect to client
	client = TelegramClient('session/' + phone_number, api_id, api_hash)
	await client.start(phone_number)
	me = await client.get_me()
	
	# FORECAST BOT
	
	print_msg_time(Fore.GREEN + f'Welcome : ({me.first_name}) to ' + forecast_channel + Fore.RESET)
	print_msg_time(Fore.YELLOW + 'Membaca data........200OK' + '\n' + Fore.RESET)
	
	# Start command /balance

	i = 0
	while i <= 99999999999999999999:
		await client.send_message(forecast_group, choice1)
		print_msg_time(Fore.GREEN + 'sending command ' + choice1 + Fore.RESET)
		time.sleep(2)
		await client.send_message(forecast_group, choice2)
		print_msg_time(Fore.RED + 'sending command ' + choice2 + Fore.RESET)
		time.sleep(1)
		i = i +1
	
	await client.run_until_disconnected()
	
asyncio.get_event_loop().run_until_complete(main())

	
   
