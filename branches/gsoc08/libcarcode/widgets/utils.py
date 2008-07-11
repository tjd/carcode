from OpenGL.GL import *
from OpenGL.GLUT import glutBitmapCharacter, GLUT_BITMAP_8_BY_13

from pygame.locals import *

class Dummy:
    pass

colors = [(1.0, 0.0, 0.0, 0.5), (0.0, 1.0, 0.0, 0.8), (0.0, 0.0, 1.0, 0.9)]

class Clipper:
    """ Region clipping manager object 
    Uses Stencil Buffer and manages multiple
    superimposing regions, uses singleton-like
    pattern from ASPN cookbook:
        http://aspn.activestate.com/ASPN/Cookbook/Python/Recipe/52558
    """
    class __Clipper2:
        def __init__(self):
            self.regions = 0
                
        def begin(self, region):
            # If we have 0 clipping regions clean stencil buffer
            # and set the stencil function to always modify the buffer.
            if self.regions == 0:
                glClear(GL_STENCIL_BUFFER_BIT)
                glEnable(GL_STENCIL_TEST)
                op = (GL_REPLACE,GL_REPLACE,GL_REPLACE)
                func = (GL_ALWAYS,1,1)
            else:
                op = (GL_KEEP, GL_KEEP,GL_INCR)
                func = (GL_EQUAL,self.regions,self.regions)
            
            glColorMask(GL_FALSE, GL_FALSE, GL_FALSE, GL_FALSE)
            
            glStencilOp(*op)
            glStencilFunc(*func)
            glRecti(*region)
            
            self.regions += 1
            
            glColorMask(GL_TRUE,GL_TRUE,GL_TRUE,GL_TRUE)
            glStencilFunc(GL_EQUAL,self.regions, self.regions)
            glStencilOp(GL_KEEP,GL_KEEP,GL_KEEP)
        
        def end(self):
            self.regions -= 1
            if self.regions == 0:
                glDisable(GL_STENCIL_TEST)
            else:
                glColorMask(GL_TRUE,GL_TRUE,GL_TRUE,GL_TRUE)
                glStencilFunc(GL_EQUAL,self.regions, self.regions)
                glStencilOp(GL_KEEP,GL_KEEP,GL_KEEP)

    __singleton = None
    
    def __init__(self):
        # Check if we have singleton instance, if not initialize one.
        if Clipper.__singleton is None:
            Clipper.__singleton = Clipper.__Clipper2()
        self.__singleton = Clipper.__singleton
        
    def begin(self, *args):
        """Begin cliping region defined by a rectangle
        
            @param x1 Upper left rect vector X
            @param y1 Upper left rect vector Y
            @param x2 Bottom right rect vector X
            @param y2 Bottom right rect vector Y
        """
        self.__singleton.begin(*args)
        
    def end(self):
        """ End cliping region """
        self.__singleton.end()


def mangle_event(event, obj_pos):
    """ Mangle mouse events data with object offsets 
    
        @param event original event object from pygame
        @param obj_pos tuple with object position to offset (x, y)
    """
    if event.type == MOUSEBUTTONUP or event.type == MOUSEBUTTONDOWN:
        nevent = Dummy()
        nevent.type = event.type
        nevent.pos = (event.pos[0] - obj_pos[0], event.pos[1] - obj_pos[1])
    else:
        nevent = event
    return nevent