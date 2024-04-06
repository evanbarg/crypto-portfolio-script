import requests
from decimal import Decimal

urlErgo = 'https://api.ergoplatform.com/addresses/9g47GkWEzeTcwFZNWBNgUvxHD7QnjLr5r9g2SnzdNVyCXjS7Aze'

response = requests.get(urlErgo)
Ergodata = response.json()

Ergobalance = Ergodata["transactions"]["totalBalance"]

str_Ergototal = str(Ergobalance)
newErgoBalance = Decimal(str_Ergototal[:-9] + '.' + str_Ergototal[-9:])

print ('Ergo Balance:', newErgoBalance)