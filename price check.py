import bs4, requests

def get_ikea_price(product_url):
    res = requests.get(product_url)
    res.raise_for_status()

    soup = bs4.BeautifulSoup(res.text, 'html.parser')
    elements = soup.select('#price1')
    return elements[0].text.strip()


print('Paste URL:')
url = input()
price = get_ikea_price(url)
print(price)
