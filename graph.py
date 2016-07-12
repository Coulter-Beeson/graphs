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
	def add_edge(self, e):
		if e in self.E():
			return

		self.E().add(e)
		self.m += 1

	#O(E)
	def remove_edge(self, e):
		(u,v) = e

		if (u,v) not in self.E() and (v,u) not in self.E():
			return

		self.E().discard((u,v))
		self.E().discard((v,u))
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

		self.V().discard(v)
		self.n -= 1

		E = self.E().copy()

		for (x,y) in E:
			if x == v or y == v:
				self.remove_edge((x,y))

	#O(n^2)
	def adjacent(self, u, v):
		return (u,v) in self.E() or (v,u) in self.E()
	
	#O(n)
	def is_vertex(self, v):
		return v in self.V()


	#Open Neighbourhood of v
	# G X V -> V
	#O(n^2)
	def N(self, v):

		S = { y for (x,y) in self.E() if x == v}.union( x for (x,y) in self.E() if y == v)

		return Set(S)

	#Closed Neighbourhood of v
	def CN(self, v):
		return self.N(v).union({v})


