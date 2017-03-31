import requests
import bs4
import os

url = "http://concordpastor.blogspot.com"

def get_text_from_web(url):

    response = requests.get(url)
    soup = bs4.BeautifulSoup(response.text, 'html.parser')
    post = soup.find(id = 'main-wrapper').find(class_='post-body').get_text()
    return post

#html = get_html_from_web(url)

#soup = bs4.BeautifulSoup(html, 'html.parser')

#date = soup.find(id = 'main-wrapper').find('h2').get_text()

#print date

#title = soup.find(id = 'main-wrapper').find('h3').get_text()

#print title

text = get_text_from_web(url)

format_text = text.strip().split()
print format_text

#print post

#def dump_post(name):
#    filename = os.path.abspath(os.path.join(name, '.txt'))
#    with open(filename, "w") as file:
