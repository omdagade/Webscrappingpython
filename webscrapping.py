import requests
from bs4 import BeautifulSoup
import smtplib
import time

url = input("ENTER THE PRODUCT URL-: ")
while True:
    re = requests.get(url)
    res = re.content

    soup = BeautifulSoup(res , 'html.parser')

    price = float(soup.find('p', {"id": "money"}).text[:3])

    if price < 200:
        smt = smtplib.SMTP('smtp.gmail.com', 587)
        smt.ehlo()
        smt.starttls()
        smt.login('jethalalgada9325@gmail.com', 'dyzbigvfuufdtzvf')
        smt.sendmail('jethalalgada9325@gmail.com','omdagade9325@gmail.com',
                     f"Subject: Price has dropped!!!!\n\nPrice of the product you were looking to buy has been dropped to {price}. Go fast and buy the product using the link- {url} \n\nRegards Om Dagade\nomdagade9325@gmail.com")
        smt.quit()
    time.sleep(24*60*60)


