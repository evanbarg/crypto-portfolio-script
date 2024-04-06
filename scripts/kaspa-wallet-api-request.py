import requests
from decimal import Decimal

url = 'https://api.kaspa.org/addresses/kaspa%3Aqr9rzljkpgm8n3vp445vmua4cy38mkhqzcdx0ge2xqp57jptjmxjcsf2g66c5/balance'
response = requests.get(url)
data = response.json()

Kaspabalance = data['balance']

str_Kaspatotal = str(Kaspabalance)
newKaspaBalance = Decimal(str_Kaspatotal[:-8] + '.' + str_Kaspatotal[-8:])

print ('Kaspa Balance:', newKaspaBalance)