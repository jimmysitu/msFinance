# msfinance
msfinance offers Pythonic way to download stocks financial data from [morningstar.com/stocks](https://www.morningstar.com/stocks)

![PyPI - Python Version](https://img.shields.io/pypi/pyversions/msfinance)
![PyPI - Version](https://img.shields.io/pypi/v/msfinance)
![PyPI - Downloads](https://img.shields.io/pypi/dm/msfinance)
![GitHub Workflow Status (with event)](https://img.shields.io/github/actions/workflow/status/jimmysitu/msfinance/python-package.yml)


## Install
```bash
pip install msfinance
```

## Quick Start
```python
#!/usr/bin/python3 -u
import msfinance as msf

stock = msf.Stock(
    session='msf_database.sql3',
)


print(stock.get_income_statement('aapl', 'xnas'))
print(stock.get_balance_sheet_statement('aapl', 'xnas'))
print(stock.get_cash_flow_statement('aapl', 'xnas'))

print(stock.get_growth('aapl', 'xnas'))
print(stock.get_operating_and_efficiency('aapl', 'xnas'))
print(stock.get_financial_health('aapl', 'xnas'))
print(stock.get_cash_flow('aapl', 'xnas'))
```
- More example is placed in [example](https://github.com/jimmysitu/msfinance/tree/main/example) directory. Add msfinance path to environment variable: PYTHONPATH


## US Tickers and Exchanges
- Get all tickers symbol of each exchange [here](https://www.nasdaq.com/market-activity/stocks/screener)


## HK Tickers and Exchanges
- Get all tickers numbers of Heng Seng Index [here](https://en.wikipedia.org/wiki/Hang_Seng_Index#Components)


## TODO
- [x] Add 'Last Updated' to database record
- [x] Add support for pip package
- [ ] Add tickers from HK exchanges
- [ ] Add docs in docs directory for readthedoc.io
- [ ] Add multiprocessing for speed up
- [ ] More robust error handling
- [ ] Add more statistics valuations
