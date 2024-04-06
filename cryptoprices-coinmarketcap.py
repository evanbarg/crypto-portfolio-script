import requests
from bs4 import BeautifulSoup
import pandas as pd
import openpyxl
from openpyxl.formatting.rule import ColorScaleRule, DataBarRule
from openpyxl.styles import NamedStyle, Font
from decimal import Decimal
from datetime import datetime

#--------------------------------time-and-date-----------------------------------
now = datetime.now()
dt_string = now.strftime("%d/%m/%Y %H:%M:%S")

#-----------------------pull-prices-and-create-spreadsheet-----------------------
urlCMC = 'https://coinmarketcap.com/watchlist/649ecd4ad665352badbf5c1e'
response = requests.get(urlCMC)
soup = BeautifulSoup(response.text, 'html.parser')

# Find the table that contains the data
table = soup.find('table', class_='cmc-table')

# Find all table rows (excluding the header row)
rows = table.find_all('tr')[1:]

# Create empty lists to store the data
names = []
prices = []

# Iterate through each row and extract the name and price
for row in rows:
    # Find the columns within the row
    columns = row.find_all('td')

    # Extract the name and price from the columns
    name = columns[2].text.strip()
    price = columns[3].text.strip()

    # Append the data to the respective lists
    names.append(name)
    prices.append(price)
    

# Create a DataFrame to store the data
data = {'Name': names, 'Price': prices}
df = pd.DataFrame(data)

# Save the DataFrame to a spreadsheet (CSV or Excel)
df.to_excel('coinmarketcap_data.xlsx', index=False)
# Alternatively, you can use df.to_excel() to save as an Excel file


#----------------------------------Wallet-Balances--------------------------------------
# Gets Flux Balance
urlFlux = 'https://api.runonflux.io/explorer/balance?address=t1V3mUTb3W4CtPAQ53Vbvh8m6qCsT9kJbY6'
response = requests.get(urlFlux)
Fluxdata = response.json()

Fluxbalance = Fluxdata['data']

str_Fluxtotal = str(Fluxbalance)
newFluxBalance = Decimal(str_Fluxtotal[:-8] + '.' + str_Fluxtotal[-8:])

print ('Flux Balance:', newFluxBalance)

# Gets Kaspa Balance
url = 'https://api.kaspa.org/addresses/kaspa%3Aqr9rzljkpgm8n3vp445vmua4cy38mkhqzcdx0ge2xqp57jptjmxjcsf2g66c5/balance'
response = requests.get(url)
data = response.json()

Kaspabalance = data['balance']

str_Kaspatotal = str(Kaspabalance)
newKaspaBalance = Decimal(str_Kaspatotal[:-8] + '.' + str_Kaspatotal[-8:])

print ('Kaspa Balance:', newKaspaBalance)

# Gets Radiant Balance
urlRadiant = 'https://radiantexplorer.com/ext/getbalance/12ZnbELhFgmFCKygB5PW3yYkigNGZ2da72'
response = requests.get(urlRadiant)
Radiantdata = response.json()

Radiantbalance = response.text

print('Radiant Balance:', Radiantbalance)

# Gets Chia Balance
urlChia = 'https://xchscan.com/api/account/balance?address=xch1cx5gmxkmyjtafw9am6snre905whznlx7jw8rgkamgd2ahdplkyus7stfny'
response = requests.get(urlChia)
Chiadata = response.json()

Chiabalance = Chiadata['xch']

print('Chia Balance:', Chiabalance)

# Gets Alephium Balance
Alephiumurl = 'https://alephium.herominers.com/api/stats_address?address=1D77zWgTUpCZHf9nBrS5Ytd2vj3q4AmMJuibDb9G7ri92'

response = requests.get(Alephiumurl)
Alephiumdata = response.json()

Alephiumbalance = (Alephiumdata['stats']['paid'])

str_Alephiumtotal = str(Alephiumbalance)
newAlephiumBalance = Decimal(str_Alephiumtotal[:-18] + '.' + str_Alephiumtotal[-18:])

print('Alephium Balance:', newAlephiumBalance)

# Gets Ergo Balance 
urlErgo = 'https://api.ergoplatform.com/addresses/9g47GkWEzeTcwFZNWBNgUvxHD7QnjLr5r9g2SnzdNVyCXjS7Aze'

response = requests.get(urlErgo)
Ergodata = response.json()

Ergobalance = Ergodata["transactions"]["totalBalance"]

str_Ergototal = str(Ergobalance)
newErgoBalance = Decimal(str_Ergototal[:-9] + '.' + str_Ergototal[-9:])

print ('Ergo Balance:', newErgoBalance)

# Gets Ironfish Balance
Ironfishurl = 'https://ironfish.herominers.com/api/stats_address?address=e30c90d020bb35c22b8cc40f8d2db71c269d91345e5e1dfa1504fea7d1b9b61a'
response = requests.get(Ironfishurl)
Ironfishdata = response.json()

Ironfishbalance = Ironfishdata['stats']['paid']

str_Ironfishtotal = str(Ironfishbalance)
newIronfishBalance = Decimal(str_Ironfishtotal[:-8] + '.' + str_Ironfishtotal[-8:])

print ('Ironfish Balance:', newIronfishBalance)

# Gets Monero Balance
XMRurl = 'https://monero.herominers.com/api/stats_address?address=47DyG4ADcqwbaFtBtN4x4vfPwWsrWenFM4J611K8jgv5MbsWxz2hQqof5mtb1ssCa4BmugRZXTjnRLrdjMqR9mubSNowiRr'
response = requests.get(XMRurl)
XMRdata = response.json()

XMRbalance = XMRdata['stats']['paid']

str_XMRtotal = str(XMRbalance)
newXMRBalance = Decimal(str_XMRtotal[:-11] + '.' + str_XMRtotal[-11:])

print ('Monero Balance:', newXMRBalance)

#Gets RTM Balance
#RTMurl = 'https://mike-engine.herokuapp.com/personaladd?session=ab6d1494-e1e1-4933-9def-3c3ce86e438b&bc=RTM&v=a001'

#response = requests.get(RTMurl)
#RTMdata = response.json()

#RTMbalance = (RTMdata[0]['deposited'])

#print('Raptoreum Balance:', RTMbalance)

#Gets Dynex Balance 
Dynexurl = 'https://dynex.herominers.com/api/stats_address?address=Xwoes5W3quwb2wGx5E4VfSDzCsxvnhaLrVDwzfDKqyx8CoGKxWXsCx3AAogJawjumFN3sqAcwsBKSfdm9dnU8Neg2NbV3mfoh'

response = requests.get(Dynexurl)
Dynexdata = response.json()

Dynexbalance = (Dynexdata['stats']['paid'])

str_Dynextotal = str(Dynexbalance)
newDynexBalance = Decimal(str_Dynextotal[:-9] + '.' + str_Dynextotal[-9:])
floatDynexBalance = float(newDynexBalance)
newNewDynexBalance = floatDynexBalance + 3.07
print('Dynex Balance:', newNewDynexBalance)

#Gets Versus Balance
Verusurl = 'https://luckpool.net/verus/miner/RMGMD7ErBNGFXJmy7hKWgpXAmEfdxh8Yhu'
response = requests.get(Verusurl)
Verusdata = response.json()

Verusbalance = Verusdata['paid']

print ('Verus Balance:', Verusbalance)

#Gets Zephyr Balance
Zephurl = 'https://zephyr.herominers.com/api/stats_address?address=ZEPHYR2P59B7YyyJG5XwCMDVpxwQkzPzTeHqQ6xN7kKLEji48it4Tf2GL95Jzhit1KBAD9dFwZpsED3gaA6Acqcgi6hJBHUQxPS4c'
response = requests.get(Zephurl)
Zephdata = response.json()

Zephbalance = Zephdata['stats']['paid']

str_Zephtotal = str(Zephbalance)
newZephBalance = Decimal(str_Zephtotal[:-12] + '.' + str_Zephtotal[-12:])

print ('Zephyr Balance:', newZephBalance)


#----------------------------------------insert-data-into-spread-sheet----------------------------------
#loads the file
workbook = openpyxl.load_workbook("C:/Users/evan/Desktop/Wallets/Crypto Project/coinmarketcap_data.xlsx")

#select sheet
sheet = workbook['Sheet1']

#Bold Font
bold_font = Font(bold=True)

#Insert Column Balance
cell = sheet['C1']
cell.value = 'Balance'
sheet['C1'].font = bold_font

#Insert Column Total$$
cell = sheet['D1']
cell.value = '$$$$'
sheet['D1'].font = bold_font

#Insert XMR Balance
cell = sheet['C2']
cell.value = newXMRBalance

#Insert Kaspa Balance
cell = sheet['C3']
cell.value = newKaspaBalance

#Insert Chia Balance
cell = sheet['C4']
cell.value = Chiabalance

#Insert Flux Balance
cell = sheet['C5']
cell.value = newFluxBalance

#Insert Ergo Balance
cell = sheet['C6']
cell.value = newErgoBalance

#Insert Verus Balance
cell = sheet['C7']
cell.value = Verusbalance

#Insert Dynex Balance
cell = sheet['C8']
cell.value = newNewDynexBalance

#Insert Alephium Balance
cell = sheet['C9']
cell.value = newAlephiumBalance

#Insert Radiant Balance
cell = sheet['C11']
cell.value = Radiantbalance

#Insert Ironfish Balance
cell = sheet['C12']
cell.value = newIronfishBalance

#Insert RTM Balance
#cell = sheet['C12']
#cell.value = RTMbalance

#Insert Zephyr Balance
cell = sheet['C13']
cell.value = newZephBalance


#----------------------------------create-formulas-----------------------------
#format cells to Currency
currency_style = NamedStyle(name='currency', number_format='"$"#,####0.0000')

#XMR $$balance
cell = sheet['D2']  
cell.value = '=B2*C2'
cell = sheet['D2'].style = currency_style

#CHIA $$balance
cell = sheet['D3']
cell.value = '=B3*C3'
cell = sheet['D3'].style = currency_style

#Flux $$balance
cell = sheet['D4']
cell.value = '=B4*C4'
cell = sheet['D4'].style = currency_style

#Kaspa $$balance
cell = sheet['D5']
cell.value = '=B5*C5'
cell = sheet['D5'].style = currency_style

#Ergo $$balance
cell = sheet['D6']
cell.value = '=B6*C6'
cell = sheet['D6'].style = currency_style

#Dynex $$balance
cell = sheet['D7']
cell.value = '=B7*C7'
cell = sheet['D7'].style = currency_style

#Verus $$balance
cell = sheet['D8']
cell.value = '=B8*C8'
cell = sheet['D8'].style = currency_style

#Radiant $$balance
cell = sheet['D9']
cell.value = '=B9*C9'
cell = sheet['D9'].style = currency_style

#Alephium $$balance
cell = sheet['D10']
cell.value = '=B10*C10'
cell = sheet['D10'].style = currency_style

#Ironfish $$balance
cell = sheet['D11']
cell.value = '=B11*C11'
cell = sheet['D11'].style = currency_style

#RTM $$balance
cell = sheet['D12']
cell.value = '=B12*C12'
cell = sheet['D12'].style = currency_style
cell = sheet['B12'].style = currency_style

#Zephyr $$balance
#cell = sheet['D12']
#cell.value = '=B12*C12'
#cell = sheet['D12'].style = currency_style

#Conditional Formatting Data Bars
balance_databar_rule = DataBarRule(start_type='num', start_value=0, end_type='num', end_value=120,
                           color="FF638EC6", showValue=True)

balance_range_for_formatting = "D2:D12"
sheet.conditional_formatting.add(balance_range_for_formatting, balance_databar_rule)

#Total balance
cell = sheet['D17']
cell.value = '=SUM(D2:D15)'
cell = sheet['D17'].style = currency_style


#-----------------------Desktop ROI---------------------
#Column Name
cell = sheet['J1']
cell.value = 'Desktop Build'
sheet['J1'].font = bold_font

#Days Mined
cell = sheet['J2']
cell.value = 'Start Mine Date'

cell = sheet['K2']
cell.value = '3/26/2023'

cell = sheet['J3']
cell.value = 'Days Mined'

cell = sheet['K3']
cell.value = '=TODAY()-K2'

#Return on investment
cell = sheet['J6']
cell.value = 'ROI'

cell = sheet['K6']
cell.value = '=-1800+D17-D5'
cell = sheet['K6'].style = currency_style
#conditional formatting
ROI_color_scale_rule = ColorScaleRule(start_type='num', start_value=-1800, start_color='FF0000', 
                                  mid_type='num', mid_value=0, mid_color='FFFF00', 
                                  end_type='num', end_value=1800, end_color='00FF00')
ROI_formatting = "K6"
sheet.conditional_formatting.add(ROI_formatting, ROI_color_scale_rule)

#--------------------------KS0-Pro----------------------------------------------------
#Column Name
cell = sheet['N1']
cell.value = 'KS0 Pro'
sheet['N1'].font = bold_font

#Days Mined
cell = sheet['N2']
cell.value = 'Start Mine Date'

cell = sheet['O2']
cell.value = '12/27/2023'

cell = sheet['N3']
cell.value = 'Days Mined'

cell = sheet['O3']
cell.value = '=TODAY()-O2'

#Return on investment
cell = sheet['N6']
cell.value = 'ROI'

cell = sheet['O6']
cell.value = '=-560+D3'
cell = sheet['O6'].style = currency_style
#conditional formatting
ROI_color_scale_rule = ColorScaleRule(start_type='num', start_value=-560, start_color='FF0000', 
                                  mid_type='num', mid_value=0, mid_color='FFFF00', 
                                  end_type='num', end_value=560, end_color='00FF00')
ROI_formatting = "O6"
sheet.conditional_formatting.add(ROI_formatting, ROI_color_scale_rule)


#-----------------------TimeStamp-----------------------------------
cell = sheet['J30']
cell.value = 'Date Created'

cell = sheet['K30']
cell.value = dt_string

#--------------------------Save-the-modified-spreadsheet------------------------------------
workbook.save('C:/Users/evan/Desktop/Wallets/Crypto Project/coinmarketcap_data.xlsx')




