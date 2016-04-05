import COMMONS, pygame

class Ball:

    def __init__(self, center, radius, vel, hole, color=(255,255,255)):

        self.radius = radius
        self.x      = center[0]
        self.y      = center[1]
        self.color  = color
        self.vel    = vel
        self.hole   = hole


    def move(self):

        self.x += self.vel[0] # x coordinate
        self.y += self.vel[1]


    def check_board_bounce(self):

        if self.y <= self.radius or self.y >= COMMONS.WINDOWHEIGHT - self.radius:
            self.vel[1] = -self.vel[1]


    def get_rect(self):

        return pygame.Rect(self.x - self.radius, self.y - self.radius, 2* self.radius, 2* self.radius)

   