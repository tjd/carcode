from OpenGL.GL import *
from OpenGL.GLUT import glutBitmapCharacter, GLUT_BITMAP_8_BY_13

from pygame.locals import *

class Label:
    def __init__(self, text, pos, color):
        self.text = text
        self.pos = list(pos)
        self.color = color
        self.size = [len(text) * 8, 13]
    
    def set_text(self, text):
        self.text = text
        self.size = [len(text) * 8, 13]
        
    def events(self, event):
        return False
    
    def draw(self):
        glPushMatrix()
        glTranslatef(self.pos[0], self.pos[1], 0)
        
        if len(self.color) == 3:
            glColor3f(*self.color)
        else:
            glColor4f(*self.color)
            
        glRasterPos3i(0, 0, 0)
        for c in self.text:
            glutBitmapCharacter(GLUT_BITMAP_8_BY_13, ord(c))
            
        glPopMatrix()