import yfinance as yf

msft = yf.Ticker("GOOGL")

# get all stock info
print(msft.info)


tickers = ['ABEV3.SA']
for ticker in tickers:
    ticker_yahoo = yf.Ticker(ticker)
    data = ticker_yahoo.history()
    last_quote = data['Close'].iloc[-1]
    print(ticker, last_quote)