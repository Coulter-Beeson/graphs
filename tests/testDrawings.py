import unittest

from project.drawings.drawing import Drawing, ForceDrawing, TwoVector
from testGraphs import test_vertices, test_edges
from project.graphs.graph import Graph
from math import sqrt

class TestDrawing(unittest.TestCase):

	def setUp(self):

		G = Graph(test_vertices(),test_edges())

		self.D = Drawing(G,1000,1000)

		self.D.draw()


	def test_blank(self):
		self.assertEqual(True,True)

class TestForceDrawing(TestDrawing):


	def setUp(self):

		self.G = Graph( test_vertices(), test_edges() )
		self.h = 1000
		self.w = 2000
		self.k = int(sqrt((self.h*self.w)/self.G.n)) # 632

		self.D = ForceDrawing( self.G, self.h, self.w )

	def test_init(self):
		self.assertEqual( self.D.G, Graph( test_vertices(), test_edges() ) )
		self.assertEqual( self.D.h, self.h)
		self.assertEqual( self.D.w, self.w)

		self.assertEqual( self.D.k, self.k )

	def test_f(self):
		fr = self.D.f_r
		fa = self.D.f_a

		self.assertEqual( fa(0),  0)
		self.assertEqual( fa(25), 0)
		self.assertEqual( fa(50), 3)
		self.assertEqual( fa(51), 4)
		self.assertEqual( fa(632), 632)
		self.assertEqual( fa(1000), 1582)

		#if two vertices less than k away repulsion is great
		self.assertEqual( fr(0),  self.h/2)
		self.assertEqual( fr(5),  79884)
		self.assertEqual( fr(632), 632)
		self.assertEqual( fr(1000), 399)

	def test_force(self):

		fr = self.D.f_r
		fa = self.D.f_a

		v_0 = TwoVector(0,0)
		v_1 = TwoVector(1,2)
		v_2 = TwoVector(2,4)
		v_3 = TwoVector(3,6)

		self.assertEqual( self.D.force(v_0, fa), TwoVector() )
		self.assertEqual( self.D.force(v_0, fr), TwoVector(self.h/2,self.h/2) )
		




