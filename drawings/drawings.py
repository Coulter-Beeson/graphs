
import random
from math import sqrt

class ForceDrawing(object):

	def __init__(self, G, h, w):
		self.G = G
		self.h = h
		self.w = w

		self.k = int(sqrt((h*w)/G.n))

		self.f_r = lambda x: self.k/x 
		self.f_a = lambda x: (x*x)/self.k
		self.dist = lambda v,u=TwoVector(): int(sqrt( (v.x-u.x)**2 + (v.y-u.y)**2))

		self.Pos  = { v : TwoVector( random.randint(0,G.n*2)+(w/2),random.randint(0,G.n*2)+(h/2) ) for v in G.V()}
		self.Disp = { v : TwoVector() for v in G.V()}
		self.t = TwoVector()

	def draw(self, i):

		for step in range(i):

			self.add_force_repulsive()

			self.add_force_attractive()

			self.update_position()

			self.cool_temp()
		

	def add_force_attractive(self):
		for (u,v) in self.G.E():
			
			diff = self.Pos[v] - self.Pos[u]
			f_a = self.force(diff, self.f_a)

			self.Disp[v] -= f_a 
			self.Disp[u] += f_a


	def add_force_repulsive(self):
		for v in self.G.V():
			self.Disp[v] = TwoVector()
			for u in self.G.V():
				if u != v:
					diff = self.Pos[v] - self.Pos[u]

					self.Disp[v] += self.force(diff, self.f_r)		

	def update_position(self):
		for v in self.G.V():

			self.Pos[v] += self.cooled_displacment(v)
			v_x, v_y = self.Pos[v]

			v_x = min(self.w/2, max(-self.w/2, v_x))
			v_y = min(self.l/2, max(-self.l/2, v_y))

			self.Pos[v] = TwoVector(v_x, v_y)


	def force(self, diff, f):
			mag_diff = self.dist(diff)

			if mag_diff == 0:
				mag_diff = 1

			return (f(mag_diff) / mag_diff) * diff


	def cooled_displacment(self,v):

		min_x, min_y = self.minimum(v,self.t)

		d_x, d_y = (1/dist(self.Disp[v]))*self.Disp[v]

		return TwoVector( min_x*d_x  , min_y*d_y  )


	def minimum(self,u,v):
		return TwoVector( min(u.x, v.x) , min(u.y, v.y))


	
	def cool_temp(self):
		return self.t

		


class TwoVector(object):

	def __init__(self,x=0,y=0):
		self.x = x
		self.y = y

	def __str__(self):
		return "(" + str(self.x) + "," + str(self.y) + ")"

	__repr__ = __str__ 

	def __add__(self,u):
		return TwoVector(self.x + u.x, self.y + u.y)

	def __sub__(self,u):
		return TwoVector(self.x - u.x, self.y - u.y)

	def __rmul__(self,c):
		return TwoVector(c*self.x, c*self.y)

	def __eq__(self,other):
		return self.x == other.x and self.y == other.y

	def __ne__(self,other):
		return not __eq__

	def __hash__(self):
		return hash(self.x) + hash(self.y)	

	def __iter__(self):
		yield self.x
		yield self.y
