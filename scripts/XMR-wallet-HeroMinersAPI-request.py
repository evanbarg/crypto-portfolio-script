import requests
from decimal import Decimal

XMRurl = 'https://monero.herominers.com/api/stats_address?address=47DyG4ADcqwbaFtBtN4x4vfPwWsrWenFM4J611K8jgv5MbsWxz2hQqof5mtb1ssCa4BmugRZXTjnRLrdjMqR9mubSNowiRr'
response = requests.get(XMRurl)
XMRdata = response.json()

XMRbalance = XMRdata['stats']['paid']

str_XMRtotal = str(XMRbalance)
newXMRBalance = Decimal(str_XMRtotal[:-12] + '.' + str_XMRtotal[-12:])

print ('Monero Balance:', newXMRBalance)