
from markov_python.cc_markov import MarkovChain
import fetch

def main():
    # get data from web
    url = "http://concordpastor.blogspot.com"
    file = fetch_data_from_web(url)
    # create Markov chain wiht clean text data
    text = create_Markov_chain(file)
    # generate and display text using the Markov chain
    generate_display_text(text)

def fetch_data_from_web(url):
    pass




def create_Markov_chain(text_file):
    mc = MarkovChain()
    mc.add_file(text_file)
    return mc.generate_text()


def generate_display_text(text):
    print ' '.join(text)


if __name__ == '__main__':
    main()