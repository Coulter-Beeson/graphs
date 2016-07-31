import numpy as np
import random


class Drawing(object):

	def __init__(self, G, h, w):
		self.G = G
		self.h = h
		self.w = w

		self.Pos = {}

	def draw(self):
		self.Pos = { v : np.array( [random.randint( 0, self.w ), random.randint( 0, self.h)] ) for v in self.G.V()}

		return self.Pos

	def __str__(self):
		return  "Pos: "+ str(self.Pos)

	__repr__ = __str__


	def __iter__(self):
		for p in self.Pos.items():
			yield p

	def __getitem__(self, key):

		(x,y) = self.Pos[key]
		return (x,y)

	def __setitem__(self, key, val):
		i,j = val
		self.Pos[key] = np.array([i,j])



		


