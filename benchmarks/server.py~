from multiprocessing.connection import Client, Listener
import time

def chunks(seq, num):
  avg = len(seq) / float(num)
  out = []
  last = 0.0

  while last < len(seq):
    out.append(seq[int(last):int(last + avg)])
    last += avg

  return out

class server():

	def __init__(self, sock=6000, ip='localhost', authkey='secret password', MAX=3):
		self.sock = sock
		self.ip = ip
		self.authkey = authkey
		self.connections = []
		self.scale = MAX
		self.jobs = []
		self.outputs = []
		self.socket = None

	def setScale(self, scale):
		self.scale = scale

	def addJobs(self, _list):
		self.jobs.extend(_list)

	def _listen(self):
		scale = self.scale
		while True:
			if scale:
				scale -= 1
				conn = self.socket.accept()
				self.connections.append(conn)
				#print 'connection accepted from', conn.last_accepted
			else:
				break
	def start(self):
		self.socket = Listener((self.ip, self.sock), authkey=self.authkey)
		self._listen()
		next = self.scale-1
		scheduler = chunks(self.jobs, self.scale)
		if len(self.jobs) is 0:
			print "Please add some jobs before you start me !!"
			return
		for each in scheduler:
			self.connections[next].send(each)
			next -= 1
			if next < 0:
				break

		now = time.time()
		for conn in self.connections:
			x = conn.recv()
			self.outputs.extend(x)
			conn.close()
		self.socket.close()
		t = time.time() - now
		print str("Took me " + str(t) + " time")
		return self.outputs
