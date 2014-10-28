import string

def file_to_words(filename):
    """Read a file and return a sequence of (word, occurances) values.
    """
    STOP_WORDS = set([
            'a', 'an', 'and', 'are', 'as', 'be', 'by', 'for', 'if', 'in', 
            'is', 'it', 'of', 'or', 'py', 'rst', 'that', 'the', 'to', 'with',
            ])
    TR = string.maketrans(string.punctuation, ' ' * len(string.punctuation))

    #print multiprocessing.current_process().name, 'reading', filename
    output = []

    dic = {}
    with open(filename, 'rt') as f:
        for line in f:
            line = line.translate(TR) # Strip punctuation
            for word in line.split():
                word = word.lower()
                if word.isalpha() and word not in STOP_WORDS:
		    if word in dic:
                    	dic[word] += 1
		    else:
			dic[word] = 0
    return dic

def parse_movie_tags(filename, tag):
    TR = string.maketrans(string.punctuation, ' ' * len(string.punctuation))

    #print multiprocessing.current_process().name, 'reading', filename
    output = []

    dic = {}
    with open(filename, 'rt') as f:
	for line in f:
            line = line.translate(TR) # Strip punctuation
            for word in line.split():
                word = word.lower()
                if word.isalpha():
			output.append(word)
    return (output, tag)

def parse_movie(filename):
    TR = string.maketrans(string.punctuation, ' ' * len(string.punctuation))

    #print multiprocessing.current_process().name, 'reading', filename
    output = []

    dic = {}
    with open(filename, 'rt') as f:
	for line in f:
            line = line.translate(TR) # Strip punctuation
            for word in line.split():
                word = word.lower()
                if word.isalpha():
			output.append(word)
    return output
