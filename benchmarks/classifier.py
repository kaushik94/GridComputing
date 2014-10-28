from server import server
import fileprocessing as fp
from textblob.classifiers import NaiveBayesClassifier
from textblob import TextBlob
import glob
import sysinfo as si
import sys
from tabulate import tabulate

def train(num_training=20, num_test=10):
    input_files = glob.glob('MovieReviews/txt_sentoken/pos/*.txt')
    s = server(MAX=int(sys.argv[1]))
    A = [(inp, 'pos') for inp in input_files[0:num_training]]
    input_files = glob.glob('MovieReviews/txt_sentoken/neg/*.txt')
    A.extend([(inp, 'neg') for inp in input_files[0:num_training]])
    s.addJobs(A)
    #print A
    print "Traing classifier on the following files: "
    #print "File name          file type"
    headers = ["File Name", "file review type"]
    table = zip([i[0][30:len(i[0])-1] for i in A], [i[1] for i in A])
    print tabulate(table, headers, tablefmt="grid")
    """
    for i in A:
	print i[0][26:len(i[0])-1],
        print "       ",
	print i[1]
    """
    training = s.start()
    cl = NaiveBayesClassifier(training)
    return cl

def test(cl, num_test=10):
    inp = glob.glob('MovieReviews/txt_sentoken/pos/*.txt')
    test = []
    for _input in inp[0:num_test]:
    	test.append(fp.parse_movie_tags(_input, 'pos'))
    #print test
    print cl.accuracy(test)
    print cl.show_informative_features(10)

if __name__ == '__main__':
    MAX = 3
    print "Running simulation on machine :"
    si.print_sysinfo()
    C = train(50, 10)
    print "test results passed with accuracy: ", test(C, 10)
