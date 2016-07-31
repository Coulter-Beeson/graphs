
import numpy as np

#Square Matrix over the field GF(2)
class BooleanMatrix(object):

	#O(n)
	def __init__(self, n):
		self.M = [0]*n
		self.n = n

	#O(n^2)
	def __str__(self):

		S = ""

		for x in self.M:
			row = "["
			for j in range(self.n):
				if x % 2 == 1:
					row += " 1 "
				else:
					row += " 0 "
				x = x >> 1

			S += row + "] \n" 
		
		return S 

	__repr__ = __str__

	#self[i,j] in O(1) self[i] in O(n)
	#TODO: fix set, del, slices, and exceptions
	def __getitem__(self, key):

		try:
			i,j = key
			
			return (self.M[i] >> j) % 2

		except TypeError:
			v =[0]*self.n

			x = self.M[key]

			for j in range(self.n):
				if (x >> j) % 2:
					v[j] = 1

			return v			


	#Given a Matrix B B[i] = val for Val Bool[], or B[i.j] = val 
	def __setitem__(self, key, val):
		
		try:
			i,j = key
	
			if val and not (self.M[i] >> j) % 2:
				self.toggle(i,j)
			if not val and (self.M[i] >> j) % 2:
				self.toggle(i,j)

		except TypeError:

			x = 0

			for i, v in enumerate(val):
				if v:
					x += 2**i
			self.M[key] = x


	#O(1)
	def toggle(self, i, j):
		self.M[i] = self.M[i] ^ 2**j

	#O(n^2)
	# Given a matrix M, returns the minor Mi,i for an index i
	# Does not modify M
	def minor(self, r):

		B = BooleanMatrix(self.n - 1)

		for i in range(r):
			for j in range(r):
				B[i,j] = self[i,j]

		for i in range(r+1,self.n):
			for j in range(r):
				B[i-1,j] = self[i,j]

		for i in range(r):
			for j in range(r+1,self.n):
				B[i, j - 1] = self[i,j]

		for i in range(r+1,self.n):
			for j in range(r+1,self.n):
				B[i-1,j-1] = self[i,j]
			
			
		return B
	#O(1)
	def inc(self, i = 1):
		self.M += [0]*i
		self.n += 1


	# complements of the Graph G
	#O(n)
	def __invert__(self):
		self.M =[ ~self.M[i] & (2**self.n - 1) for i in range(self.n) ]

