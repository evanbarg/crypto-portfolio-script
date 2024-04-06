import requests
from decimal import Decimal

Hypraurl = 'https://explorer.hypra.network/api?module=account&action=balance&address=0xCE63CF9788eF003AFAe7A96f5b27a28c1682B50C'
HypraResponse = requests.get(Hypraurl)
HypraData = HypraResponse.json()

Hyprabalance = HypraData['result']

str_HypraTotal = str(Hyprabalance)
newHypraBalance = Decimal(str_HypraTotal[:-18] + '.' + str_HypraTotal[-18:])

print ('Hypra Balance:', newHypraBalance)