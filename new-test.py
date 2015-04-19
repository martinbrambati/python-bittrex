from bittrex.bittrex import Bittrex

bit = Bittrex(api_key='748fdc31633644849231b13a9f2cafdd', api_secret='25e3129bc6ed4cf3b3d7beaebfc4914e')
print(bit.get_markets())
