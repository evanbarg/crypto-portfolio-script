import requests
from decimal import Decimal

AIPGurl = 'https://explorer.aipowergrid.io/ext/getaddress/AYaFnf8rENKbHFR6B8doiC5vqjKZGCRZ9B'
response = requests.get(AIPGurl)
AIPGdata = response.json()

AIPGbalance = AIPGdata['balance']

print ('AI Power Grid:', AIPGbalance)