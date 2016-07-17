from sets import Set


class Graph(object):

	#O(V) + O(E) storage
	def __init__(self, V = Set(), E = Set()):		
		self.vert_set = V
		self.n = 0

		self.edge_set = E
		self.m = 0

	def V(self):
		return self.vert_set

	def E(self):
		return self.edge_set

	def __str__(self):
		return "< " + str(self.V()) + " , " + str(self.E()) + " >"

	__repr__ = __str__

	#O(1)
	def add_edge(self, u, v):

		e = Edge(u,v)

		if e in self.E():
			return

		self.E().add(e)
		self.m += 1

	#O(E)
	def remove_edge(self, u, v):
		e = Edge(u,v)

		if e not in self.E():
			return

		self.E().discard(e)
		self.m -= 1

    #O(1)
	def add_vertex(self, v):
		if v in self.V():
			return

		self.V().add(v)
		self.n += 1

	#O(E)
	def remove_vertex(self, v):
		if v not in self.V():
			return

		for u in self.N(v):
			self.remove_edge(u,v)

		self.V().discard(v)
		self.n -= 1


	#O(n^2)
	def adjacent(self, u, v):
		return Edge(u,v) in self.E()
	
	#O(n)
	def is_vertex(self, v):
		return v in self.V()


	#Open Neighbourhood of v
	# G X V -> V
	#O(n^2)
	def N(self, v):
		S = { y for (x,y) in self.E() if v == x } | { x for (x,y) in self.E() if v == y}
		return Set(S)

	#Closed Neighbourhood of v
	def CN(self, v):
		S = self.N(v)
		S.add(v)
		return S

class Edge(object):

	def __init__(self, u, v, data = None):
		self.u = u
		self.v = v
		self.data = data


	def __eq__(self, other):
		if not isinstance( other, self.__class__ ):
			return False

		return ( (self.u == other.u and self.v == other.v) or (self.v == other.u and self.u == other.v) )

	def __ne__(self, other):
		return not self.__eq__(other)


	def __hash__(self):
		return hash(self.u) + hash(self.v)

	def __str__(self):
		return "(" + str(self.u) + "," + str(self.v) + ")"

	__repr__ = __str__

	def __iter__(self):
		yield self.u
		yield self.v

	def get_val(self):
		return self.data

	def set_val(self, val):
		self.data = val


