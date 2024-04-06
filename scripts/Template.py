import requests
import urllib3
from decimal import Decimal

urllib3.disable_warnings()

# Make a GET request to the URL
response = requests.get('https://backend-v115.mainnet.alephium.org/addresses/1D77zWgTUpCZHf9nBrS5Ytd2vj3q4AmMJuibDb9G7ri92/balance',verify=False)

# Parse the JSON response
AlphData = response.json()

# Print the "balance" value
AlphBalance = AlphData['balance']

str_AlphTotal = str(AlphBalance)

newAlphBalance = Decimal(str_AlphTotal[:-18] + '.' + str_AlphTotal[-18:])

print ('Alphium Balance:', newAlphBalance)
