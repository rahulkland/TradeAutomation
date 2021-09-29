#!/usr/bin/env python3

from os import environ

# environ is used to get API information from environment variables
# You could also use a config file, pass them as arguments,
# or even hardcode them (not recommended)
from telethon import TelegramClient, events, utils
import re
import sys

api_id = 8289565
api_hash = '7e958c4c4ea8f0cea7485196733ca4ad'

phone = '+919003199379'
username = '1273828837'

BANK_NIFTY = 'BankNifty'
NIFTY = 'Nifty'
Put = 'PE'
Call = 'CE'
Buy = 'Buy'
Sell = 'Sell'

stockName = ''
optionType = ''
transactionType = ''
entryPrice = 0

#sourceGroupName = 'Support Signals (Platinum Batch 5)'
sourceGroupName = 'Trade Pops'
destinationGroupName = 'DharamikTradeMessages'

messageFilter = ['Buy', 'Target']
stockFilter = ['BankNifty', 'Nifty', '#BankNifty', '#Nifty']

weeklyExpiryMonth = {"Jan": "1", "Feb": "2", "Mar": "3", "Apr": "4", "May": "5", "Jun": "6", "Jul": "7", "Aug": "8", "Sep": "9", "Oct": "O", "Nov": "N", "Dec": "D"}

def main():
    # session_name = environ.get('TG_SESSION', 'session')
    client = TelegramClient(username, api_id, api_hash)
    
    @client.on(events.NewMessage)
    async def my_handler(event):
        newMessage = event.message.message

        chat_from = event.chat if event.chat else (await event.get_chat()) # telegram MAY not send the chat enity
        chat_title = chat_from.title

        if(chat_from.title == sourceGroupName):
            await sendMessage(destinationGroupName, newMessage)

    # --------------------- This is to filter only the trade signal messages --------------------------
    async def sendMessage(destinationGroupName, message):
        
        destinationGroupEntity = await client.get_entity(destinationGroupName)

        print(destinationGroupEntity)

        print(message)

        await client.send_message(entity=destinationGroupEntity,message=message)
        

    client.start(phone)

    # client.add_event_handler(update_handler)

    print('(Press Ctrl+C to stop this)')

    client.run_until_disconnected()


# def update_handler(update):
#     print(update)


if __name__ == '__main__':
    userDetails = sys.argv[1]
    if userDetails:
        if(userDetails.lower() == 'rahul'):
            api_id = 8289565
            api_hash = '7e958c4c4ea8f0cea7485196733ca4ad'
            phone = '+919003199379'
            username = '1273828837'
        elif(userDetails.lower() == 'srikanth'):
            api_id = 8648499
            api_hash = 'b635f9d93e1d51a1119029e7a392a483'
            phone = '+919790913870'
            username = '1568072049'
    main()