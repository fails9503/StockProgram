import yfinance as yf
import sys
import io
import json

sys.stdout = io.TextIOWrapper(sys.stdout.detach(), encoding = 'utf-8')
sys.stderr = io.TextIOWrapper(sys.stderr.detach(), encoding = 'utf-8')

# This class is Stock info.
# Stock info include zip, sector, history and another things
class Stock:

    def __init__(self, stock_code):

        # yf.Ticker(stock_code)
        # find stock code from yahoo-finance databases    
        self.stock_code = yf.Ticker(stock_code)

        # info method looks for information on stocks that match the stock code. 
        stock_data = self.stock_code.info


        # Setting key and values
        self.zip = stock_data['zip']
        self.sector = stock_data['sector']

    # We have many print methods. this methods just print 'stock-code' and 'zip' and 'sector'
    def print_stock_simple(self):
        print(self.stock_code)
        print(self.zip)
        print(self.sector)

try:
    msft = Stock("AAP123")
    msft.print_stock_simple()

except KeyError:
    print("주식 정보를 찾을 수 없습니다.")

except ValueError:
    print("주식 정보를 찾을 수 없습니다.")
    
finally:
    print("프로그램을 종료합니다.")
