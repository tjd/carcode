
class EventDispatcher:
    def __init__(self):
        self.__events__ = {}
        self.enabled = True
        
    def subscribe(self, event, func):
        if self.__events__.has_key(event):
            self.__events__[event].append(func)
        else:
            self.__events__[event] = [func]
        
    def enable(self):
        self.enabled = True
        
    def disable(self):
        self.enabled = False
        
    def dispatch(self, event, *args):
        if not self.enabled:
            return 0
        if not self.__events__.has_key(event):
            return 0
        for handler in self.__events__[event]:
            handler(*args)
        return 1