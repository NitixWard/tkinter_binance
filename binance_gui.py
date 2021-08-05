from tkinter import *
from tkinter import messagebox
from PIL import ImageTk
import requests
from csv import *
import os
import datetime
import tkinter as tk
from tkinter import ttk
from tkinter.messagebox import showinfo


class binance:
    def __init__(self, window):
        self.window = window
        self.window.title('Binance Live Status')
        self.window.geometry('1199x900+50+0')
        self.window.resizable(False, False)

        # ====BG Image====
        self.bg = ImageTk.PhotoImage(file='bg5.jpg')
        self.bg_image = Label(self.window, image=self.bg).place(
            x=0, y=0, relwidth=1, relheight=1)

        # ====Enter Cryptocoin Frame====
        Frame_Cryptocoin = Frame(self.window, bg='#edafb8')
        Frame_Cryptocoin.place(x=660, y=100, height=640, width=500)

        title = Label(Frame_Cryptocoin, text='Binance Coin Status',
                      font=('Impact', 35, 'bold'), fg='#d77337', bg='#edafb8').place(x=48, y=30)
        desc = Label(Frame_Cryptocoin, text='Live Update',
                     font=('Goudy old style', 15, 'bold'), fg='#d77337', bg='#edafb8').place(x=50, y=85)

        coinname_label = Label(Frame_Cryptocoin, text='Crypto Currency',
                               font=('Goudy old style', 25, 'bold'), fg='gray', bg='#edafb8').place(x=50, y=125)
        self.coin_name_var = tk.StringVar()
        self.txt_coinname = Entry(
            Frame_Cryptocoin, font=('times new roman', 20), bg='lightgray', textvariable=self.coin_name_var)
        self.txt_coinname.place(x=55, y=175, height=35)

        basename_label = Label(Frame_Cryptocoin, text='Base Currency',
                               font=('Goudy old style', 25, 'bold'), fg='gray', bg='#edafb8').place(x=50, y=215)
        self.base_name_var = tk.StringVar()
        self.txt_basename = Entry(
            Frame_Cryptocoin, font=('times new roman', 20), bg='lightgray', textvariable=self.base_name_var)
        self.txt_basename.place(x=55, y=265, height=35)

        self.output_frame = Frame(Frame_Cryptocoin, bg='#f2d8db')
        self.output_frame.place(x=55, y=375, width=288, height=200)
        self.output_label = Label(Frame_Cryptocoin, text='Price', font=(
            'times new roman', 15, 'bold'), background='#f2d8db', foreground='red').place(x=55, y=385)

        self.fetchbtn = Button(Frame_Cryptocoin, text='Fetch', bg='#d77337', fg='white', font=(
            'times new roman', 15, 'bold'), command=self.fetch_function).place(x=72, y=315, width=250)

    def fetch_function(self):
        coinname = self.coin_name_var.get()
        coinbase = self.base_name_var.get()
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
        # if checkbtn_var.get() == 0:
        #     subscribed = 'No'
        # else:
        #     subscribed = 'Yes'
        self.current_price = str(coin) + " " + str(price) + " " + \
            str(current_date_time)

# Write to txt file
        with open('file.txt', 'a') as fp:
            fp.write(self.current_price + "\n")


# Write to csv file
        with open('file.csv', 'a') as f:
            dict_writer = DictWriter(f, fieldnames=['BINCURRVAL'])
            if os.stat('file.csv').st_size == 0:
                dict_writer.writeheader()
            dict_writer.writerow({
                'BINCURRVAL': self.current_price
            })

            self.output_label.config(text='self.current_price')


window = Tk()
obj = binance(window)
window.mainloop()
