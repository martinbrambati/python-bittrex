from bittrex.bittrex import Bittrex

bit = Bittrex(api_key='748fdc31633644849231b13a9f2cafdd', api_secret='25e3129bc6ed4cf3b3d7beaebfc4914e')

# Only one instance is ok

# Function get_markets

#market_list = bit.get_markets()
# Uncomment next line to print
# print(market_list)

# Ticker list example

#firs_market = market_list['result'][0]['MarketName']
#ticker_for_the_first_market = bit.get_ticker('BTC-CRAVE')

#print (ticker_for_the_first_market)

# Buy limit example
limit = bit.buy_limit('BTC-CRAVE', float(0.1) , float(2.1))
print(limit)