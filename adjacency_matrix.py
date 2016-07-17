from graph import Graph, Edge
from sets import Set
from boolean_matrix import BooleanMatrix

class AdjacencyMatrix(Graph):

	#O(|V| + |E|) = O(n + m)
	def __init__(self, V = Set(), E = Set()):
		self.Matrix = BooleanMatrix(len(V))  
		self.VM = {}
		self.IVM = {}
		self.n = 0
		self.m = 0

		for v in V:
			self.add_vertex(v)

		for (u,v) in E:
			self.add_edge(u,v)


	#O(n)
	def V(self):
		return Set({v for v in self.VM})

	#O(n^2)
	def E(self):

		S = { Edge(self.IVM[i], self.IVM[j]) 
			for i in range(self.n) 
			for j in range(self.n)
			if i < j
			and self.Matrix[i,j] }

		return Set(S)


	#TODO: Abstract the iteration for matrix numpy?
	def M(self):
		return self.Matrix
				
	#O(1) 
	def add_vertex(self, v):

		if v in self.VM:
			return

		self.VM[v] = self.n
		self.IVM[self.n] = v
		self.Matrix.inc()			
		self.n += 1


	#TODO: fix this so that VM and IVM point to the right places
	def remove_vertex(self, v):

		if v not in self.VM:
			return

		i = self.VM[v]

		for u in self.N(v):
			self.remove_edge(u,v)

		P = [ (j,self.IVM[j]) for j in range(i + 1, self.n)  ]

		for (j,k) in P:
			self.VM[k] = j - 1
			self.IVM[j-1] = k

		del self.VM[v]
		del self.IVM[self.n - 1]
		self.Matrix = self.Matrix.minor(i)

		self.n -= 1



	#O(1) if e is an edge
	#crashes if e is not an edge
	def add_edge(self, u, v):

		if self.adjacent(u,v):
			return	False

		i = self.VM[u]
		j = self.VM[v]

		self.Matrix[i,j] = 1
		self.Matrix[j,i] = 1

		self.m += 1

		return True


	#O(1) if e is in E
	def remove_edge(self, u, v):

		if not self.adjacent(u,v):
			return

		i = self.VM[u]
		j = self.VM[v]

		self.Matrix[i,j] = 0 
		self.Matrix[j,i] = 0 

		self.m -= 1

	#O(1) if (u,v) is in E
	def adjacent(self, u, v):
		i = self.VM[u]
		j = self.VM[v]

		return self.Matrix[i,j]

	#O(n)
	#Open Neighbourhood of v
	def N(self, v):
		S = Set()

		i = self.VM[v]			
		v_i = self.Matrix[i]


		for k,v in enumerate(v_i):
			if v:
				S.add( self.IVM[k] )

		return S


