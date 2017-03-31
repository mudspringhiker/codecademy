
from markov_python.cc_markov import MarkovChain
from fetch import get_text_from_web, save

def main():
    # get data from web
    url = "http://concordpastor.blogspot.com"
    blogfile = fetch_data_from_web(url, "concordpastor0331")
    #print blogfile
    # create Markov chain wiht clean text data
    markov = create_Markov_chain(blogfile)

    generate_display_text(markov)

def fetch_data_from_web(url, filename):
    text = get_text_from_web(url)
    file = save(filename, text)
    return file

def create_Markov_chain(text_file):
    mc = MarkovChain()
    mc.add_file(text_file)
    return mc.generate_text()

def generate_display_text(text):
    print ' '.join(text)


if __name__ == '__main__':
    main()