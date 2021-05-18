from bs4 import BeautifulSoup
import requests
import time

def get_crypto_price(coin):

    url = 'https://www.google.com/search?q='+coin+'+price'

    HTML=requests.get(url)

    soup=BeautifulSoup(HTML.text, 'html.parser')

    text=soup.find('div',attrs={'class':'BNeawe iBp4i AP7Wnd'}).find('div',attrs={'class':'BNeawe iBp4i AP7Wnd'}).text

    return text

#Function that updates the price of cryptcurrency
def main():

    prev_price=-1
    crypto=input('Enter Cryptocurrency :')

    while True:
        price=get_crypto_price(crypto)

        if price!=prev_price:
            print('Price of '+crypto+'='+price)
            prev_price=price
        
        time.sleep(3)


main()
