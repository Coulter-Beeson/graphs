import unittest

from project.graphs.graph import Graph, Edge
from project.graphs.adjacency_matrix import AdjacencyMatrix 
from sets import Set



def test_vertices():
	return  Set( { 'a', 'b', 'c', 'd', 'e' } )

def test_edges():
	E_pairs = Set( { ('a', 'b'), ('a', 'c'), ('b', 'd'), ('c', 'd'), ('d', 'e') } )
	E = Set()

	for (u,v) in E_pairs:
		E.add(Edge(u,v))

	return E

class TestGraph(unittest.TestCase):

	
	def give_graph(self, V, E):
		return Graph(V,E)

	def setUp(self):
		#			 b
		#			/ \
		#		   /   \
		#	G =	 a      d - - - e
		#		   \   /
		#			\ /
		#			 c
		#
		#				 b
		#				/
		#			   /
		#	H = x - - a
		#			   \
		#				\
		#				 c

		
		V = test_vertices()
		E = test_edges()

		self.G = self.give_graph(V,E)

		self.V = V.copy()
		self.E = E.copy()
		self.n = self.G.n
		self.m = self.G.m


	def test_add_vertex(self):

		#Check the new Graph is empty
		self.assertEqual( self.G.V(), self.V )
		self.assertEqual( self.G.n, self.n )

		self.G.add_vertex( 'x' )

		#Check Graph only has 'a'
		self.assertEqual( self.G.V(), self.V.union( {'x'} ) )
		self.assertEqual( self.G.n, self.n + 1 )

	def test_add_edge(self):

		self.assertEqual( self.G.E(), self.E )
		self.assertEqual( self.G.m, self.m )

		self.G.add_edge( 'd','a' )

		self.assertEqual( self.G.E(), self.E.union( { Edge('d','a') } ) )
		self.assertEqual( self.G.m, self.m + 1 )

	def test_remove_edge_forward(self):

		self.assertEqual( self.G.E(), self.E )
		self.assertEqual( self.G.m, self.m )

		self.G.remove_edge( 'a','b' )
		self.E.remove( Edge('a','b') )


		self.assertEqual( self.G.E(), self.E )
		self.assertEqual( self.G.m, self.m - 1 ) 


	def test_remove_edge_backward(self):

		self.assertEqual( self.G.E(), self.E )
		self.assertEqual( self.G.m, self.m )

		self.G.remove_edge('b','a')
		self.E.remove( Edge('a','b') )

		self.assertEqual( self.G.E(), self.E )
		self.assertEqual( self.G.m, self.m - 1 )

	def test_remove_vertex_a(self):

		self.G.remove_vertex( 'a' )
		self.V.remove( 'a' )
		self.E.remove( Edge('a', 'b') )
		self.E.remove( Edge('a', 'c') )

		self.assertEqual( self.G.V(), self.V )
		self.assertEqual( self.G.n, self.n - 1 )
		self.assertEqual( self.G.E(), self.E )
		self.assertEqual( self.G.m, self.m - 2 )

	def test_remove_vertex_d(self):

		self.G.remove_vertex( 'd' )

		self.V.remove( 'd' )
		S_points = Set( { ('b', 'd'), ('c', 'd'), ('d', 'e') } )
		S = Set()

		for (u,v) in S_points:
			S.add(Edge(u,v))

		self.E = self.E - S
		
		self.assertEqual( self.G.V(), self.V )
		self.assertEqual( self.G.n, self.n - 1 )
		self.assertEqual( self.G.E(), self.E )
		self.assertEqual( self.G.m, self.m - 3 )

	def test_adjacent_forward(self):

		self.assertTrue(  self.G.adjacent( 'a', 'b' ) )
		self.assertFalse( self.G.adjacent( 'a', 'd' ) )


	def test_adjacent_backward(self):

		self.assertTrue(  self.G.adjacent( 'b', 'a' ) )
		self.assertFalse( self.G.adjacent( 'd', 'a' ) )

	def test_open_neighbourhood(self):
	
		N_a = self.G.N( 'a' )	
		N_b = self.G.N( 'b' )	
		N_d = self.G.N( 'd' )	
		N_e = self.G.N( 'e' )

		self.assertEqual( N_a, Set( { 'b', 'c' } ) )	
		self.assertEqual( N_b, Set( { 'a', 'd' } ) )	
		self.assertEqual( N_d, Set( { 'b', 'c', 'e' } ) )	
		self.assertEqual( N_e, Set( { 'd' } ) )	


	def test_closed_neighbourhood(self):

		N_a = self.G.CN( 'a' )	
		N_b = self.G.CN( 'b' )	
		N_d = self.G.CN( 'd' )	
		N_e = self.G.CN( 'e' )

		self.assertEqual( N_a, Set( { 'b', 'c', 'a' } ) )	
		self.assertEqual( N_b, Set( { 'a', 'd', 'b' } ) )	
		self.assertEqual( N_d, Set( { 'b', 'c', 'e', 'd' } ) )	
		self.assertEqual( N_e, Set( { 'd' , 'e' } ) )	


class TestAdjacencyMatrixBaseMethods(TestGraph):

	def give_graph(self, V, E):
		return AdjacencyMatrix(V,E)


if __name__ == '__main__':
	unittest.main()