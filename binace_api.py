import requests
import xlwt
from xlwt import Workbook


def binace_srapper(value):
    url = "https://api.binance.com/api/v3/ticker/price?symbol="+str(value)
    resp = requests.get(url).json()
    price = resp['price']
    return str(price)
    wb = Workbook()
    sheet1 = wb.add_sheet('Binance')
    sheet1.write(1, 0, current_date_time)
    sheet1.write(1, 0, price)
    wb.save('example.xls')


value = input("Enter cryptocurrency: ")
print(binace_srapper(value))
