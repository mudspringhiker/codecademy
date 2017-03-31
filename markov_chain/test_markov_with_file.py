from markov_python.cc_markov import MarkovChain

def create_Markov_chain(text_file):
    mc = MarkovChain()
    mc.add_file(text_file)
    return mc.generate_text()

def generate_display_text(text):
    print ' '.join(text)

textfile = "concordpastro0331.txt"
markov = create_Markov_chain(textfile)

generate_display_text(markov)