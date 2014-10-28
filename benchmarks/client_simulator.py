import os
from client import client

class simulator():
	def __init__(self, address='localhost', port=6000, MAX = 3, auth='secret password'):
		self.number = MAX
		self.address = address
		self.port = port
		self.output = []
		self.children = []
		self.auth = auth

	def simulate(self):
		for i in xrange(self.number):
			pid = os.fork()
			if pid:
				#self.children.append(pid)
				pass
			else:
				C = client((self.address, self.port), self.auth)
				self.children.append(C)
				print "created"
				self.output.append(C.start())
				return self.output
		for child in self.children:
			child.close()

	def output():
		return self.output()
		
		
