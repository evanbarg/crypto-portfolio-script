import requests
from decimal import Decimal

Zephurl = 'https://zephyr.herominers.com/api/stats_address?address=ZEPHYR2P59B7YyyJG5XwCMDVpxwQkzPzTeHqQ6xN7kKLEji48it4Tf2GL95Jzhit1KBAD9dFwZpsED3gaA6Acqcgi6hJBHUQxPS4c'

response = requests.get(Zephurl)
Zephdata = response.json()

Zephbalance = (Zephdata['stats']['paid'])

str_Zephtotal = str(Zephbalance)
newZephBalance = Decimal(str_Zephtotal[:-12] + '.' + str_Zephtotal[-12:]) + 1

print('Zephyr Balance:', newZephBalance)