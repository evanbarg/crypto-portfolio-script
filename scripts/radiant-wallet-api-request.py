import requests
from decimal import Decimal

urlRadiant = 'https://radiantexplorer.com/ext/getbalance/12ZnbELhFgmFCKygB5PW3yYkigNGZ2da72'
response = requests.get(urlRadiant)
Radiantdata = response.json()

Radiantbalance = response.text

print('Radiant Balance:', Radiantbalance)