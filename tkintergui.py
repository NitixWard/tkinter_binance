import requests
#import tkinter as tk
import datetime
#import pandas as pd


def binace_srapper(value):
    url = "https://api.binance.com/api/v3/ticker/price?symbol="+str(coin)
    resp = requests.get(url).json()
    price = resp['price']
    current_date_time = datetime.datetime.now()

    # window = tk.Tk()
    # #window.title(" My Favorite Sports Player ")
    # window.geometry("400x400")

    # # Current price
    # binancelabel = tk.Label(text=price)
    # binancelabel.grid(column=10, row=10)

    # # Current time
    # binanceDateTimeCurr = tk.Label(text=current_date_time)
    # binanceDateTimeCurr.grid(column=20, row=20)

    # # Text input window
    # # inputText = tk.Text(window, height=5, width=20)
    # # inputText.grid()

    # # Button
    # # fetchButton = tk.Button(text='Fetch', command=binace_srapper)
    # # fetchButton.grid()

    # window.mainloop()
    return (str(price), str(current_date_time))


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

print(binace_srapper(coin))
