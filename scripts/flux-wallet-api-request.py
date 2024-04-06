import requests
from decimal import Decimal

urlFlux = 'https://api.runonflux.io/explorer/balance?address=t1V3mUTb3W4CtPAQ53Vbvh8m6qCsT9kJbY6'
response = requests.get(urlFlux)
Fluxdata = response.json()

Fluxbalance = Fluxdata['data']

str_Fluxtotal = str(Fluxbalance)
newFluxBalance = Decimal(str_Fluxtotal[:-8] + '.' + str_Fluxtotal[-8:])

print ('Flux Balance:', newFluxBalance)