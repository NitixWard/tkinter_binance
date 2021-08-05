coin = input(
    "Enter coin of which you want the value, ex. MATIC, SHIB, BTC, BNB etc: ")
base = input(
    "Enter the base with respect to which you want the current price, ex. BTC,BNB,BUSD,USDT etc: ")
coin = coin+base
for c in coin:
    if c.islower():

        coin = coin.upper()
    else:
        coin = coin
print(coin)
