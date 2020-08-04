"""
yapf --in-place --recursive --style="{indent_width: 4}" *.py  << to format files
figure out how to do that automatically later^
Sources:
https://towardsdatascience.com/scraping-multiple-amazon-stores-with-python-5eab811453a8
https://leimao.github.io/blog/YAPF-Quick-Tutorial/
https://www.w3schools.com/python/ref_string_format.asp
https://docs.python.org/3/library/email.examples.html
https://github.com/google/yapf#example
"""
import smtplib

import requests
from bs4 import BeautifulSoup


def price_ripper(urls):
    # http://www.networkinghowtos.com/howto/common-user-agent-list/
    HEADERS = ({
        'User-Agent':
        'Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/41.0.2228.0 Safari/537.36',
        'Accept-Language': 'en-US, en;q=0.5'
    })

    # Loop must end after all urls are used
    for url in urls:
        # fetch the URL
        page = requests.get(url, headers=HEADERS)

        # blend the soup up by BeautifulSoup
        soup = BeautifulSoup(page.content, features="lxml")

        # receive the title
        title = soup.find(id='productTitle').get_text().strip()
        print(title)

        # receive the price
        price = float(
            soup.find(id='priceblock_ourprice').get_text().replace(
                '$', '').replace(',', '').strip())
        print("$" + str(price))

        if price < urls[url]:
            print("ALERT A LOWER PRICE HAS BEEN FOUND")
            # send an email that a lower price has been found
            server = smtplib.SMTP_SSL('smtp.gmail.com', 465)
            server.login(
                "youremail@gmail.com",
                "app-specific password (if 2-step verifaction is on) ")
            server.sendmail(
                "toperson@place.com", "fromperson@place.com",
                "This is an automated alert: the price on {} has went down to {} from {}"
                .format(title, price, urls[url]).encode('utf-8'))
            server.quit()


products = {
    # "url": original_price
    "https://smile.amazon.com/gp/product/B08951RHL6/ref=ox_sc_saved_title_1?smid=A2EM68VTUA1J0Y&psc=1":
    149.95,
    "https://smile.amazon.com/gp/product/B07MB8P28S/ref=ox_sc_act_title_1?smid=A2W34NP6H9HC8F&psc=1":
    9.99
}
price_ripper(products)
