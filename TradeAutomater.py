#!/usr/bin/env python3
# A simple script to print all updates received
#
# NOTE: To run this script you MUST have 'TG_API_ID' and 'TG_API_HASH' in
#       your environment variables. This is a good way to use these private
#       values. See https://superuser.com/q/284342.

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

tradeSignalGroupName = 'TestGroup'
tradeStatusGroupName = 'Trade Pops'

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

        if(chat_from.title == tradeSignalGroupName):
            isTradeMessage = filtermessage(newMessage)
            if isTradeMessage :
                print("Fuck Yeah, this is a trade signal")
                await processMessage(newMessage)
    
    # --------------------- This is to filter only the trade signal messages --------------------------
    def filtermessage(message):
        isTradeMessage = True
        isDesiredStock = False

        for filter in messageFilter:
            if message.lower().find(filter.lower()) == -1:
                isTradeMessage = False
        
        for filter in stockFilter:
            if message.lower().find(filter.lower()) != -1:
                isDesiredStock = True

        return isTradeMessage & isDesiredStock

    # --------------------- Processing the message to extract the key attributes to be sent to the trading broker ---------
    async def processMessage(trademessage):

        if trademessage.find(BANK_NIFTY) != -1:
            stockName = BANK_NIFTY
        elif trademessage.find(NIFTY) != -1:
            stockName = NIFTY

        if trademessage.find(Buy) != -1:
            transactionType = Buy
        else :
            transactionType = Sell

        optionTypeMessage = trademessage.split(' ', 1)[0]
        #print(optionTypeMessage)
        
        splitstrings = trademessage.split()
        #print(splitstrings)
        
        entryPrice = int(re.search(r'\d+', re.search('Buy At (.*) For', trademessage).group(1)).group())

        stockSymbol = ''
        if((len(splitstrings[1]) >= 3) and (len(splitstrings[2]) <= 3)):
            #---- Weekly Expiry
            date = splitstrings[1]
            month = weeklyExpiryMonth.get(splitstrings[2])
            optionStrikePrice = splitstrings[3]
            optionType = splitstrings[4]

            stockSymbol = stockName.upper() + '20' + month + date.rstrip(date[-2:]) + optionStrikePrice + optionType.upper()
            #print(stockSymbol)
        else:
            #---- Monthly Expiry
            month = splitstrings[1]
            optionStrikePrice = splitstrings[2]
            optionType = splitstrings[3]
            stockSymbol = stockName.upper() + '20' + month.upper() + optionStrikePrice + optionType.upper()
            #print(stockSymbol)

        tradeSignal = stockSymbol + ' - ' + transactionType + ' - ' + str(entryPrice)
        # print(stockName, optionType, transactionType, entryPrice)
        print(tradeSignal)

        # await client.send_message('', tradeSignal)

        tradeStatusGroupEntity= await client.get_entity(tradeStatusGroupName)
        
        tradeStatusUpdateMessage = trademessage + '\n \n' + tradeSignal

        await client.send_message(entity=tradeStatusGroupEntity,message=tradeStatusUpdateMessage)

        

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