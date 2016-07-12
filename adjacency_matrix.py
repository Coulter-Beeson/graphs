from graph import Graph
from sets import Set

class AdjacencyMatrix(Graph):

	#O(|V| + |E|) = O(n + m)
	def __init__(self, V = Set(), E = Set()):
		self.M = []
		self.VM = {}
		self.IVM = {}
		self.n = 0
		self.m = 0

		for v in V:
			self.add_vertex(v)

		for e in E:
			self.add_edge(e)


	#O(n)
	def V(self):
		return Set({v for v in self.VM})

	#O(n^2)
	#TODO: prune reversed elements?
	def E(self):

		S = { (self.IVM[i], self.IVM[j]) 
			for i in range(self.n) 
			for j in range(self.n)
			if i < j
			and (self.M[i] >> j) % 2 }

		return Set(S)


	#TODO: Abstract the iteration for matrix numpy?
	def M(self, i ,j):

		if i is None and j is None:

			L = []

			for i in range(self.n):
				row = []
				x = self.M[i]
				for j in range(self.n):
					if x % 2 == 1:
						row += [1]
					else:
						row += [0]
					x = x >> 1
				L.append(row)
		
			return L

		if j is None:

			row = []
	
			for i in range(self.n):
				for j in range(self.n):
					if x % 2 == 1:
						row += [1]
					else:
						row += [0]
					x = x >> 1

			return row

		else:
			
			return (self.M[i] >> j ) % 2

				
	#O(1) If v is not in V and n < 64
	def add_vertex(self, v):

		#
		#TODO: Adjust resizing to accomidate graphs for |G| > 64
		#

		self.VM[v] = self.n
		self.IVM[self.n] = v
		self.M += [0]			#O(1) 	\\If n < w*k for some constant k
								#		\\currently stuck to less than 64
		self.n += 1


	#O(1) if e is an edge
	#crashes if e is not an edge
	def add_edge(self, e):

		(u,v) = e

		if self.adjacent(u,v):
			return	False

		i = self.VM[u]
		j = self.VM[v]

		self.M[i] += 1 << j
		self.M[j] += 1 << i

		self.m += 1

		return True


	#O(1) if e is in E
	def remove_edge(self, e):
		(u,v) = e

		if not self.adjacent(u,v):
			return

		i = self.VM[u]
		j = self.VM[v]

		self.M[i] -= 1 << j
		self.M[j] -= 1 << i

	#O(1) if (u,v) is in E
	def adjacent(self, u, v):
		i = self.VM[u]
		j = self.VM[v]

		return (self.M[i] >> j) % 2 == 1

	#O(n)
	#Open Neighbourhood of v
	def N(self, v):
		S = Set()

		i = self.VM[v]			
		x = self.M[i]


		for k in range(self.n):
			if x % 2 == 1:
				S.add( self.IVM[k] )
			x = x >> 1

		return S


