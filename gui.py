# importing the tkinter module
from tkinter import Message, font
from tkinter.font import BOLD
import requests
import datetime
import tkinter as tk
from csv import *
import os
from tkinter import Grid, Label, StringVar, ttk
from tkinter.constants import ANCHOR, CENTER, CHECKBUTTON, INSERT
from typing import Collection, ContextManager, Text

# Creating the window
window = tk.Tk()
window.geometry('500x500')
window.title('Live Crypto Status')
window['bg'] = '#E5FD6F'
font_tuple = ('Comic Sans MS', 8, 'bold')
# msg = Message(window, text='Hey')
# msg.grid(row=7, column=0)

# Creating the widgets by creating the labels
l = Label(window, text='Binance Live')
l.config(font=('Comic Sans MS', 20, 'bold'), fg='Blue')
l.grid(row=0, columnspan=10)

cryptocoin_name = ttk.Label(
    window, text='Enter the name of the coin listed on Binance: ')
cryptocoin_name.grid(row=1, column=0, sticky=tk.W)


crypto_base = ttk.Label(
    window, text='Enter the fiat or base coin listed on Binance: ')
crypto_base.grid(row=2, column=0, sticky=tk.W)


# Creating output
display_price = ttk.Label(window)
display_price.grid(row=5, column=0, sticky=tk.W)


# Creating the entrybox
coin_name_var = tk.StringVar()
cryptocoin_name_entrybox = ttk.Entry(
    window, width=16, textvariable=coin_name_var)
cryptocoin_name_entrybox.grid(row=1, column=1)
cryptocoin_name_entrybox.focus()
cryptocoin_name_entrybox.configure(font=font_tuple)

coin_base_var = tk.StringVar()
crypto_base_entrybox = ttk.Entry(window, width=16, textvariable=coin_base_var)
crypto_base_entrybox.grid(row=2, column=1)
crypto_base_entrybox.configure(font=font_tuple)


# Creating a check button
checkbtn_var = tk.IntVar()
checkbtn = ttk.Checkbutton(
    window, text='Please selelct the tick if you want to access the newsletter ', variable=checkbtn_var)
checkbtn.grid(row=3, column=0, sticky=tk.W)


# Writing a function that handles the API call from Binance
# and return the value with current time

def action():
    coinname = coin_name_var.get()
    coinbase = coin_base_var.get()
    coin = coinname+coinbase
    for c in coin:
        if c.islower():
            coin = coin.upper()
        else:
            coin = coin

    url = "https://api.binance.com/api/v3/ticker/price?symbol="+str(coin)
    resp = requests.get(url).json()
    price = resp['price']
    current_date_time = datetime.datetime.now()
    if checkbtn_var.get() == 0:
        subscribed = 'No'
    else:
        subscribed = 'Yes'
    current_price = str(coin) + " " + str(price) + " " + \
        str(current_date_time) + " " + subscribed


# Write to txt file
    with open('file.txt', 'a') as fp:
        fp.write(current_price + "\n")


# Write to csv file
    with open('file.csv', 'a') as f:
        dict_writer = DictWriter(f, fieldnames=['BINCURRVAL'])
        if os.stat('file.csv').st_size == 0:
            dict_writer.writeheader()
        dict_writer.writerow({
            'BINCURRVAL': current_price
        })

    display_price.config(text=current_price)


# Creating a button
fetchbtn = ttk.Button(window, text='Fetch', command=action)
fetchbtn.grid(row=4, columnspan=3)


window.mainloop()
