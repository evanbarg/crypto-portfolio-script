import requests
from decimal import Decimal

Ironfishurl = 'https://ironfish.herominers.com/api/stats_address?address=e30c90d020bb35c22b8cc40f8d2db71c269d91345e5e1dfa1504fea7d1b9b61a'
response = requests.get(Ironfishurl)
Ironfishdata = response.json()

Ironfishbalance = Ironfishdata['stats']['paid']

str_Ironfishtotal = str(Ironfishbalance)
newIronfishBalance = Decimal(str_Ironfishtotal[:-8] + '.' + str_Ironfishtotal[-8:])

print ('Ironfish Balance:', newIronfishBalance)