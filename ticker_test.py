import yfinance as yf
import sys
import signal
import schedule
# import time

# msft = yf.Ticker("GOOGL")
#
# # get all stock info
# print(msft.info)


def signal_handler(signal, frame):
    print("\nClosing")
    sys.exit(0)


tickers = ['GOOGL']


# tickers = load data from saved file
def job():
    for ticker in tickers:
        ticker_yahoo = yf.Ticker(ticker)
        data = ticker_yahoo.history()
        last_quote = data['Close'].iloc[-1]
        print(ticker, last_quote)

#
# def get_current_price(symbol):
#     ticker = yf.Ticker(symbol)
#     todays_data = ticker.history(period='1d')
#     return todays_data['Close'][0]


if __name__ == "__main__":
    signal.signal(signal.SIGINT, signal_handler)
    print("Hello World")
    schedule.every(3).minutes.until("16:30").do(job)