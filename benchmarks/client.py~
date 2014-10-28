import sys
from multiprocessing.connection import Listener, Client
import fileprocessing as fp
from tabulate import tabulate

"""
class client():
	def __init__(self, address, authkey):
		self.address = address
		self.authkey = authkey
		self.conn = None

	def start(self):
		self.conn = Client(self.address, self.authkey)
		_file, tag = self.conn.recv()
		#print _file
		self.conn.send(fp.parse_movie_tags(_file, tag))
		
	def close(self):
		self.conn.close()
"""

address = ('localhost', 8000)
conn = Client(address, authkey='secret password')
_jobs = conn.recv()
train = []
headers = ["File Name", "file review type"]
A = _jobs
#table = zip([i[0][30:len(i[0])-1] for i in A], [i[1] for i in A])
#print tabulate(table, headers, tablefmt="grid")
"""
print "This client is running the following files "
print "file name                 tag"
"""
for _job in _jobs:
	_file, tag = _job
	#print _file,
	#print "              "
	#print tag
	train.append(fp.parse_movie_tags(_file, tag))
conn.send(train)
