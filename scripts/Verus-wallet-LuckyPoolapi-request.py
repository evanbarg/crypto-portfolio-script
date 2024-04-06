import requests
from decimal import Decimal

Verusurl = 'https://luckpool.net/verus/miner/RMGMD7ErBNGFXJmy7hKWgpXAmEfdxh8Yhu'
response = requests.get(Verusurl)
Verusdata = response.json()

Verusbalance = Verusdata['paid']

print ('Verus Balance:', Verusbalance)