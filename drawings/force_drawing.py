from drawing import Drawing
import numpy as np
from math import sqrt



class ForceDrawing_2D(Drawing):

	def __init__(self, G, h, w):

		#sets graph and view size
		self.G = G
		self.h = h
		self.w = w

		#ideal edge length
		self.k = int(sqrt( (h*w)/G.n ))

		#force functions and distance
		self.f_r = lambda x: self.k*self.k/x
		self.f_a = lambda x: (x*x)/self.k
		self.dist = lambda v,u=self.zero_vec() : int(sqrt( (v[0]-u[0])**2 + (v[1]-u[1])**2))

		#initialize dictionaries
		self.Pos  = Drawing(G,h,w).draw()
		self.Disp = { v : self.zero_vec() for v in G.V()}

		#initialize tempurature vector
		# t = ( max_vert, max_horx, step_count )
		self.t = np.array( [h/5,w/5, 0] )


	def __str__(self):
		return  "Pos: "+ str(self.Pos) +"\n" + "Disp: " + str(self.Disp)



	def set_attractive_force(self, fa):
		self.f_a = fa

	def set_repulsive_force(self, fr):
		self.f_r = fr

	def reset_temperature(self):
		self.t = np.array( [h/5,w/5, 0] )

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
			self.Disp[v] = self.zero_vec()
			for u in self.G.V():
				if u != v:
					diff = self.Pos[v] - self.Pos[u]

					while( diff.all == (0,0) ):
						x = random.randint(-5,5)
						y = random.randint(-5,5)
						diff += np.array( [x,y] )

					self.Disp[v] += self.force(diff, self.f_r)		

	def update_position(self):
		for v in self.G.V():

			min_x, min_y = self.minimum(self.Disp[v] , self.t)

			self.Disp[v] = np.array( [min_x, min_y] )
			self.Pos[v] += self.Disp[v]
			v_x, v_y = self.Pos[v]

			v_x = min(self.w, max(0, v_x))
			v_y = min(self.h, max(0, v_y))

			self.Pos[v] = np.array([ v_x, v_y] )


	def force(self, diff, f):
			mag_diff = self.dist(diff)

			ff = f(mag_diff) 

			if mag_diff == 0:
				mag_diff = 1
				diff += np.array( [1,1] )

			return (ff/ mag_diff) * diff


	def minimum(self,u,v):

		u_x, u_y    = u
		v_x, v_y, i = v

		c_x = min( abs(u_x), abs(v_x) )
		c_y = min( abs(u_y), abs(v_y) )

		if (u_x < 0):
			c_x = -c_x
		if (u_y < 0):
			c_y = -c_y

		return np.array( [c_x, c_y] )


	
	def cool_temp(self):

		( t_x, t_y, i ) = self.t

		if t_x <= 16:
			return

		if i % 16 == 0:

			t_x = t_x / 2
			t_y = t_y / 2

		self.t = np.array( [t_x, t_y, i + 1] )

	def zero_vec(self):
		return np.zeros(2, dtype= np.int)
