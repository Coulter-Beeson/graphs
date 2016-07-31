from sets import Set


class Graph(object):

	#O(V) + O(E) storage
	def __init__(self, Verts = Set(), Edges = Set()):		
		self.vert_set = Set(Verts)
		self.n = len(self.vert_set)

		self.edge_set = Set(Edges)
		self.m = len(self.edge_set)

	def __eq__(self, other):
		if not isinstance( other, Graph):
			return False

		return ( self.V() == other.V() and self.E() == other.E() )

	def __ne__(self, other):
		return not self.__eq__(other)


	def __hash__(self):
		return hash(self.V()) + hash(self.E())

	def __contains__(self,elt):
		try:
			(i,j) = elt
			return (i,j) in self.edge_set

		except TypeError:
			return elt in self.vert_set

	#Graph union
	def __add__(self,other):
		return graph_opp(G,H, Set.union)

	#G & H
	def __and__(self,other):
		return graph_opp(G,H, Set.intersection)

	#G - H
	def __sub__(G,H):
		return graph_opp(G,H, Set.discard)

	# G ^ H, (G + H) - (G & H)
	def __xor__(G,H):
		return sub( add(G,H), intersection(G,H) )

	def __invert__(G):

		(V,E) = G

		E = { Edge(u,v) for u in V for v in V if Edge(u,v) not in E and u != v }

		return Graph(V,E)

	#applies Set operation opp to both vertex and edge sets
	#and returns the graph induced by these two new sets
	def graph_opp(G,H,opp):
		(V_G, E_G) = G
		(V_H, E_H) = H

		V = opp( V_G, V_H ) 
		E = opp( E_G, E_H )

		return Graph(V,E)


	def V(self):
		return self.vert_set

	def E(self):
		return self.edge_set

	def __str__(self):
		return "< " + str(self.V()) + " , " + str(self.E()) + " >"

	__repr__ = __str__

	# (V,E) = G unpacks G as two sets
	def __iter__(self):
		yield self.vert_set
		yield self.edge_set

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

