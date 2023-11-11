import urllib.request
from urllib.parse import urljoin

import requests
from bs4 import BeautifulSoup


def images(url):
    # use requests to get the text of the HTML
    headers = {
        'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/17.1 Safari/605.1.15',
        'referer': 'https://www.google.com/'
    }
    page = requests.get(url, headers=headers).text

    # pass page to BeautifulSoup to parse
    soup = BeautifulSoup(page, 'html.parser')

    # refactor parsed page to return urls of images
    img_urls = soup.find_all('img')

    # put all image links into a list
    urls = [img['src'] for img in img_urls]

    # using set() to remove duplicates
    nodupes = list(set(urls))

    # make urls absolute in for in the event we don't get the full url in the beginning
    absolute = []
    for image in nodupes:
        absolute.append(urljoin(url, image))

    # to print all links before returning list, uncomment the section below
    # for reference in absolute:
    #     print(reference)
    return absolute


quickUrl = "https://en.wikipedia.org/wiki/Pokémon"

listOfImages = images(quickUrl)
i = 0
for newImage in listOfImages:
    full_path = r"/insert_path_here" + str(i) + ".png"
    urllib.request.urlretrieve(newImage, full_path)
    print("Downloaded: " + full_path)
    i = i + 1
    