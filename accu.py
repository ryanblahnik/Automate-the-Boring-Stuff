import bs4, requests

def get_desc(url):
    res1 = requests.get(url)
    res1.raise_for_status()

    soup1 = bs4.BeautifulSoup(res1.text, 'html.parser')
    elements1 = soup1.select('div.info:nth-child(4)')
    return elements1

def get_temp(url):
    res2 = requests.get(url)
    res2.raise_for_status()

    soup2 = bs4.BeautifulSoup(res2.text, 'html.parser')
    elements2 = soup2.select('strong.temp:nth-child(2)')
    return elements2

def get_feel(url):
    res3 = requests.get(url)
    res3.raise_for_status()

    soup3 = bs4.BeautifulSoup(res3.text, 'html.parser')
    elements3 = soup3.select('span.realfeel:nth-child(4)')
    return elements3



desc = get_desc('http://www.accuweather.com/en/us/')
temp = get_temp('http://www.accuweather.com/en/us/')
feel = get_feel('http://www.accuweather.com/en/us/')                
print(desc, temp, feel)

