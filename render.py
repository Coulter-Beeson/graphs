import pygame
from pygame.locals import *

from OpenGL.GL import *
from OpenGL.GLU import *


class Render(object):


	def __init__(self, D):
		self.D = D

	def display(self):
		
		glBegin(GL_LINES)
    	
		for edge in self.D.G.E():
			for vertex in edge:
				glVertex2fv(self.D[vertex])
		glEnd()

		glPointSize(10.0)
		glBegin(GL_POINTS)

		for vertex in self.D.G.V():
			(x,y) = self.D[vertex]
			glVertex2f( x,y )

		glEnd()

	def run(self):

		pygame.init()

		display = (self.D.w+50,self.D.h+50)
		pygame.display.set_mode(display, DOUBLEBUF|OPENGL)

		gluOrtho2D(-25,self.D.w+25, -25,self.D.h+25)


		while True:
			for event in pygame.event.get():
				if event.type == pygame.QUIT:
					pygame.quit()
					return				

			glClear(GL_COLOR_BUFFER_BIT|GL_DEPTH_BUFFER_BIT)
			self.display()
			pygame.display.flip()
			pygame.time.wait(10)


