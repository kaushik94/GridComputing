import sys
from multiprocessing.connection import Listener, Client
import fileprocessing as fp

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

address = ('localhost', 6000)
conn = Client(address, authkey='secret password')
_jobs = conn.recv()
train = []
print "This client is running the following files "
print "file name                 tag"
for _job in _jobs:
	_file, tag = _job
	print _file,
	print "              "
	print tag
	train.append(fp.parse_movie_tags(_file, tag))
conn.send(train)
