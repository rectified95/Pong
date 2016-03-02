import COMMONS, pygame

class Paddle():

	def __init__(self, x, y, width, height, color, speed, ball):

		self.width 	= width
		self.height = height
		self.color 	= color
		self.x 		= x
		self.y 		= y
		self.speed	= speed
		self.ball 	= ball


	def move(self, mult):

		if mult == -1 and self.y - self.speed >= 0:
			self.y -= self.speed
		elif mult == 1 and self.y + self.speed <= COMMONS.WINDOWHEIGHT - self.height:
			self.y += self.speed


	def reset_state(self):

		self.width = width


	def get_rect(self):

		return pygame.Rect(self.x, self.y, self.width, self.height)
