# python-coinmarketcal
Coinmarketcal.com REST API python implementation

API (1.0.0): https://api.coinmarketcal.com/

## Install
```
pip install https://github.com/mfuellbier/python-coinmarketcal/archive/master.zip
```

## Changelog
24/01/21 : Remove oAuth authentication
24/01/21 : Fix base URL

## Usage
```python
from coinmarketcal import Coinmarketcal
# Get Token
coinmarketcal = Coinmarketcal(client_secret)

# Get coins list
coinmarketcal.get_coins()
# Get categories list
coinmarketcal.get_categories()
# Get default events
coinmarketcal.get_events(page=None, max=None,
                         dateRangeStart=None, dateRangeEnd=None, coins=None,
                         categories=None, sortBy=None, showOnly=None)

```
