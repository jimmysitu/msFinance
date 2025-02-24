#!/usr/bin/python3 -u

import msfinance as msf

proxy = 'socks5://127.0.0.1:1088'

stock = msf.Stock(
    debug=True,
    database='xshg.db3',
    proxy=proxy,
)

tickers_list = {
    '603288',   # Fosha Haitian
    '600519',   # Kweichow Moutai
    '688041',   # Hygon
    '688047',   # Loongson

}

for ticker in sorted(tickers_list):
    key_metrics = stock.get_key_metrics(ticker, 'xshg')
    financials = stock.get_financials(ticker, 'xshg')

    print(f"Ticker: {ticker}")
    for key_metric in key_metrics:
        print(key_metric)
    for financial in financials:
        print(financial)
