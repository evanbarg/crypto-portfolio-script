import requests
from decimal import Decimal

urlChia = 'https://xchscan.com/api/account/balance?address=xch1cx5gmxkmyjtafw9am6snre905whznlx7jw8rgkamgd2ahdplkyus7stfny'
response = requests.get(urlChia)
Chiadata = response.json()

Chiabalance = Chiadata['xch']

print('Chia Balance:', Chiabalance)