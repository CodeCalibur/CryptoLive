from bs4 import BeautifulSoup
import requests
import time
import pandas as pd
import matplotlib.pyplot as plt

#Finding the class which stores the Crypto Price
def get_crypto_price(coin):
    url = 'https://www.google.com/search?q='+coin+'+price'
    HTML = requests.get(url)
    soup = BeautifulSoup(HTML.text, 'html.parser')
    text = soup.find('div',attrs = {'class':'BNeawe iBp4i AP7Wnd'}).find('div',attrs = {'class':'BNeawe iBp4i AP7Wnd'}).text

    return text

#Analysis of Cryptocurrency
print("ANALYSIS OF CRYPTOCURRENCY\n\n")
crypto_abrv = input("Abbreviation of Cryptocurrency :")
temp_add = 'D:\GitHub\Crypto\_USD_2020-05-20_2021-05-19-CoinDesk.csv'
file_add = temp_add[:17]+crypto_abrv+temp_add[17:]
df_crypto = pd.read_csv(file_add)
df = pd.DataFrame({crypto_abrv:df_crypto['Closing Price (USD)']})

#Printing the entire data set of entered cryptocurrency
print('Data Set for Cryptocurrency '+crypto_abrv+' :\n',df_crypto)

#Printing the statistics for entered cryptocurrency
print('Statistics of '+crypto_abrv+' :\n',df.describe())

#Graphical Analysis
plt.style.use('fivethirtyeight')
crypto_set = df
plt.figure(figsize = (14,5))
for c in crypto_set.columns.values:
    plt.plot(crypto_set[c],label = c)

#Plotting the graph
plt.title('Cryptocurrency Graph')
plt.xlabel('Days')
plt.ylabel('Crypto Price ($)')
plt.legend(crypto_set.columns.values,loc='upper left')
plt.show()

#Main function that stores the updated price of cryptcurrency
def main():

    prev_price=-1
    crypto=input('Enter Cryptocurrency :')

    while True:
        price=get_crypto_price(crypto)

        if price!=prev_price:
            print('Updated Price of '+crypto+' = '+price)
            prev_price=price
            
        time.sleep(3)

main()

