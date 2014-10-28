from server import server

if __name__ == '__main__':
    MAX = 3
    import operator
    import glob

    input_files = glob.glob('MovieReviews/txt_sentoken/pos/*.txt')
    s = server()
    A = [(inp, 'pos') for inp in input_files[0:20]]
    input_files = glob.glob('MovieReviews/txt_sentoken/neg/*.txt')
    A.extend([(inp, 'neg') for inp in input_files[0:20]])
    s.addJobs(A)
    print A
    print s.start()
