import requests
import bs4
import os


def get_text_from_web(url):

    response = requests.get(url)
    soup = bs4.BeautifulSoup(response.text, 'html.parser')
    post = soup.find(id = 'main-wrapper').find(class_='entry-content').get_text()
    post = post.strip()
    post = post.strip("Image source")
    post = post.strip()
    post = post.strip("Subscribe to A Concord Pastor Comment")
    post = post.strip()
    post = post.strip("Tweet")
    post = post.strip().encode('utf-8')
    return post


def save(name, post):
    filename = os.path.abspath(os.path.join(name + '.txt'))
    with open(filename, "w") as file:
        file.write(post)
    return filename


#url = "http://concordpastor.blogspot.com"

#text = get_text_from_web(url)

#print text

#save("concordpastor", text)