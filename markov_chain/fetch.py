import requests
import bs4

url = "http://concordpastor.blogspot.com"

def get_html_from_web(url):

    response = requests.get(url)
    return response.text

html = get_html_from_web(url)

soup = bs4.BeautifulSoup(html)

print html