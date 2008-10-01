from OpenGL.GL import *
from OpenGL.GLUT import glutBitmapCharacter, GLUT_BITMAP_8_BY_13

from pygame.locals import *

from constants import *
from widget import Widget
from label import Label

class Checkbox(Widget):
    def __init__(self,  text = "",  *args,  **kargs):
        Widget.__init__(self,  *args,  **kargs)
        
        self.boxsize = self.size[1]
        self.checked = False
        
        y = (self.size[1] / 2) + 6
        
        self.text = Label(text, pos=(self.boxsize+2,  0),  size=(self.size[0] - self.boxsize,  self.size[1]),  fontcolor=self.fontcolor)
        
    def events(self,  event):
        if event.type == MOUSEBUTTONUP:
            inX = lambda x: x >= self.pos[0] and x <= self.pos[0]+self.size[0]
            inY = lambda y: y >= self.pos[1] and y <= self.pos[1]+self.size[1]
            
            if inX(event.pos[0]) and inY(event.pos[1]):
                self.checked = not self.checked
                return True
            return False
            
    def draw(self):
        glPushMatrix()
        glTranslatef(self.pos[0], self.pos[1], 0)
        
        glColor4f(*self.forecolor)
        glRecti(0, 0,  self.boxsize,  self.boxsize)
        
        glColor4f(*self.backcolor)
        glRecti(1, 1,  self.boxsize-1,  self.boxsize-1)
        
        if self.checked :
            glColor4f(*self.forecolor)
            glRecti(4, 4,  self.boxsize - 4,  self.boxsize - 4)
        
        self.text.draw()
        glPopMatrix()