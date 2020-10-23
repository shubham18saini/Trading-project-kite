from kiteconnect import KiteConnect
from kiteconnect import KiteTicker
import sys
# import pdb

kws = ""
kite = ""

with open('config.txt', 'r') as f:
    api_k=f.readline().strip()
    api_s=f.readline().strip()
    Stock_tokn=f.readline().strip()
print(api_k,api_s,Stock_tokn)

def get_login(api_k, api_s):  # log in to zerodha API panel
    global kws, kite
    kite = KiteConnect(api_key=api_k)

    print("[*] Generate access Token : ", kite.login_url())
    request_tkn = input("[*] Enter Your Request Token Here : ")
    data = kite.generate_session(request_tkn, api_secret=api_s)
    print(data)
    kite.set_access_token(data["access_token"])
    kws = KiteTicker(api_k, data["access_token"])
    # kws = KiteTicker(api_k, request_tkn)

    
    print(data['access_token'])

    # kite.set_access_token(access_token)
    # kws = KiteTicker(api_k, access_token)

get_login(api_k, api_s)

print("Average price,","Last price,", "open,", "High,","Low,","Close,","Last trade time")
def on_ticks(ws, ticks):
    t = ticks
    lp = t[0]['last_price']
    ap = t[0]['average_price']
    ohlc = t[0]['ohlc']
    ltt = t[0]['last_trade_time']

    print(f'{ap},{lp},{ohlc["open"]},{ohlc["high"]},{ohlc["low"]},{ohlc["close"]},{ltt}')
    # print(ticks)
    # pdb.set_trace()

inst_token = [int(Stock_tokn)]

def on_connect(ws, response):
    ws.subscribe(inst_token)
    ws.set_mode(ws.MODE_FULL, inst_token)

# print("COMPLETE")
kws.on_ticks = on_ticks
kws.on_connect = on_connect
kws.connect()
