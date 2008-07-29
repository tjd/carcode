
class Widget:
    """ Base widget class """
    def __init__(self, *args,  **kargs):
        """
        @param pos tuple with widget position (x, y)
        @param size tuple with widget size (width, height)
        @param backcolor tuple with background color information (r, g, b, a)
        @param forecolor tuple with foreground color information (r, g, b, a)
        @param fontcolor tuple with font color information (r, g, b, a)
        """
        hasPos = False
        hasSize = False
        
        if len(args) > 0:
            try:
                self.pos = [int(x) for x in args[0]]
                hasPos = True
            except:
                pass
            try:
                self.size = [int(x) for x in args[1]]
                hasSize = True
            except:
                pass
                
        if kargs.has_key('backcolor'):
            self.backcolor = kargs['backcolor']
            if len(self.backcolor) == 3:
                self.backcolor +=  (1.0, )
        else:
            self.backcolor = (0.3,  0.3,  0.3,  1.0)
            
        if kargs.has_key('forecolor'):
            self.forecolor = kargs['forecolor']
            if len(self.forecolor) == 3:
                self.forecolor +=  (1.0, )
        else:
            self.forecolor = (1.0,  1.0,  1.0,  1.0)
            
        if kargs.has_key('fontcolor'):
            self.fontcolor = kargs['fontcolor']
            if len(self.fontcolor) == 3:
                self.fontcolor +=  (1.0, )
        else:
            self.fontcolor = (1.0,  1.0,  1.0,  1.0)
        
        if kargs.has_key('pos'):
            if not hasPos:
                self.pos = [int(x) for x in kargs['pos']]
        else:
            if not hasPos:
                self.pos = (0, 0)
        
        if kargs.has_key('size'):
            if not hasSize:
                self.size = [int(x) for x in kargs['size']]
        else:
            if not hasSize:
                self.size = (10, 10)
            
    def set_size(self,  size):
        """ Set the size of the widget
        
        @param size tuple with widget size (width, height)
        """
        self.size = size
        self.on_resize()
    
    def on_resize(self):
        """ Function called when widget is resized """
        pass
    
    def get_size(self):
        """ Get the widget size tuple 
        
        @return widget size tuple (width, height)
        """
        return self.size
    
    def set_pos(self,  pos):
        """ Set the widget position 
        
        @param pos tuple with widget position (x, y)
        """
        self.pos = pos
    
    def get_pos(self):
        """ Get the widget position tuple 
        
        @return widget position tuple (x, y)
        """
        return self.pos
        
    def events(self,  event):
        """ Widget event processing function 
        
        @param event event object
        @return True if the widget handles the event, false otherwise
        """
        pass
        
    def draw(self):
        """ Draw the widget """
        pass
