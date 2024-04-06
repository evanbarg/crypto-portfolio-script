import requests
from decimal import Decimal

Dynexurl = 'https://dynex.herominers.com/api/stats_address?address=Xwoes5W3quwb2wGx5E4VfSDzCsxvnhaLrVDwzfDKqyx8CoGKxWXsCx3AAogJawjumFN3sqAcwsBKSfdm9dnU8Neg2NbV3mfoh'

response = requests.get(Dynexurl)
Dynexdata = response.json()

Dynexbalance = (Dynexdata['stats']['paid'])

str_Dynextotal = str(Dynexbalance)
newDynexBalance = Decimal(str_Dynextotal[:-9] + '.' + str_Dynextotal[-9:])
floatDynexBalance = float(newDynexBalance)
newNewDynexBalance = floatDynexBalance + 3.07
print('Dynex Balance:', newNewDynexBalance)