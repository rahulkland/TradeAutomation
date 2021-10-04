# INSTALLATION:
# pip3 install fyers-apiv2

# AUTHORIZATION:
from fyers_api import fyersModel
from fyers_api import accessToken

client_id = 'XR11602'
secret_key = 'LJCTDO2WQY'
redirect_url = 'https://tradepop.com/TradeDhar/api-login'

session=accessToken.SessionModel(client_id=client_id, secret_key=secret_key, redirect_uri=redirect_url, response_type='code', grant_type='authorization_code', state='I hope the money is flowing today!)

response = session.generate_authcode()
print(response)

#scope=”The value in scope must be openid if being passed.
#Though this is an optional field”

#Nonce = “The value in nonce can be any random string value.
#This is also an optional field”

# ------------------------------------  AUTH CODE ---------------------------------- #

# def main()

#   auth_code = input ("Enter some value: ")
#   session.set_token(auth_code)
#   response = session.generate_token()
#   access_token = response["access_token"]
#   # "You will be provided with the access_token which will have the below shown response" 

#   fyers = fyersModel.FyersModel(client_id=123, token=ABC)

#   is_async = True  #(By default the async will be False, Change to True for async API calls.)

#   # log_path = "This will create logs in the local system and that will be stored in the particular local address you have defined"

#   def PlaceOrder(tradeSignal)
#   data = {
#       "symbol":"tradeSignal",
#       "qty":1,
#       "type":1,
#       "side":1,
#       "productType":"INTRADAY",
#       "limitPrice":0,
#       "stopPrice":0,
#       "validity":"DAY",
#       "disclosedQty":0,
#       "offlineOrder":"False",
#       "stopLoss":0,
#       "takeProfit":0
#     }

#     fyers.place_order(data)
