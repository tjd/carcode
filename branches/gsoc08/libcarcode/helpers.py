import sys, os

import pygame
from pygame.locals import *

class Loader:
    """ Loader class for carcode resources (images, sounds, etc). """
    class __Loader__:
        def __init__(self):
            self.base_path = []
            self.image_path = []
            self.sound_path = []
            
            def check_path(path):
                try:
                    os.stat(path)
                except:
                    return False
                    
                media = os.path.join(path, 'media')
                try:
                    os.stat(media)
                except:
                    return False
                return True
                
            CARCODE_PATH = os.path.dirname(sys.modules[__name__].__file__)
            if check_path(CARCODE_PATH):
                self.base_path.append(CARCODE_PATH)
                self.image_path.append(os.path.join(CARCODE_PATH, 'media', 'images'))
                self.sound_path.append(os.path.join(CARCODE_PATH, 'media', 'sound'))
            else:
                path = CARCODE_PATH
                for i in xrange(2):
                    path,  basedir = os.path.split(path) 
                    if check_path(path):
                        self.base_path.append(path)
                        self.image_path.append(os.path.join(path, 'media', 'images'))
                        self.sound_path.append(os.path.join(path, 'media', 'sound'))
                        break
            unix_path = '/usr/share/carcode'
            if check_path(unix_path):
                self.base_path.append(unix_path)
                self.image_path.append(os.path.join(unix_path, 'media', 'images'))
                self.sound_path.append(os.path.join(unix_path, 'media', 'sound'))
            
        def get_image_path(self,  filename):
            for path in self.image_path:
                fullpath = os.path.join(path, filename)
                try:
                    os.stat(fullpath)
                    return fullpath
                except:
                    pass
            raise IOError
            
        def get_sound_path(self,  filename):
            for path in self.sound_path:
                fullpath = os.path.join(path, filename)
                try:
                    os.stat(fullpath)
                    return fullpath
                except:
                    pass
            raise IOError
        
        def load_image(self,  filename,  colorkey = None):
            fullname = self.get_image(filename)
            try:
                image = pygame.image.load(fullname)
            except pygame.error, message:
                print 'Cannot load image:', fullname
                raise SystemExit, message
            image = image.convert_alpha()
            if colorkey is not None:
                if colorkey is -1:
                    colorkey = image.get_at((0,0))
                image.set_colorkey(colorkey, RLEACCEL)
            return image, image.get_rect()
            
        def load_sound(filename, volume = 0.5):
            fullname = self.get_sound(filename)
            try:
                sound = pygame.mixer.Sound(fullname)
                sound.set_volume(volume)
            except pygame.error, message:
                print 'Cannot load sound:', fullname
                raise SystemExit, message
            return sound
    
    __singleton__ = None
    def __init__(self):
         # Check if we have singleton instance, if not initialize one.
        if Loader.__singleton__ is None:
            Loader.__singleton__ = Loader.__Loader__()
        self.__singleton__ = Loader.__singleton__
    
    def get_image_path(self,  filename):
        """ Return the full path to file from standard carcode image paths 
        
        @param filename string with filename to search
        @return string with full path to file
        """
        return self.__singleton__.get_image_path(filename)
    
    def get_sound_path(self,  filename):
        """ Return the full path to file from standard carcode sound paths 
        
        @param filename string with filename to search
        @return string with full path to file
        """
        return self.__singleton__.get_sound_path(filename)
    
    def load_image(self, filename):
        """ Load a image file to pygame surface from carcode standard image paths 
        
        @param filename string with image filename
        @return tuple with surface, image rect
        """
        return self.__singleton__.load_image(filename)
    
    def load_sound(self, filename):
        """ Load a sound file to pygame sound from carcode standard sound paths 
        
        @param filename string with image filename
        @return sound object
        """
        return self.__singleton__.load_sound(filename)


def load_texture(filename):
    # Generate a new Texture
    texture = glGenTextures(1)

    # Load image data and convert to packet string
    img, rect = load_image(fielname)
    data = pygame.image.tostring(img, "RGBA")

    # Set current context texture
    glBindTexture(GL_TEXTURE_2D, self.texture)

    w = img.get_width()
    h = img.get_height()

    # Bind data to texture
    glPixelStorei(GL_UNPACK_ALIGNMENT,1)
    glTexImage2D(GL_TEXTURE_2D, 0, GL_RGBA, w, h, 0, GL_RGBA, GL_UNSIGNED_BYTE, data)

    return texture

def load_sound(filename, volume = 0.5):
    loader = Loader()
    fullname = loader.get_sound_path(filename)
    try:
        sound = pygame.mixer.Sound(fullname)
        sound.set_volume(volume)
    except pygame.error, message:
        print 'Cannot load sound:', fullname
        raise SystemExit, message

    return sound

def load_image(filename, colorkey = None):
    """ Utility function for loading images.
    Returns (image, rectangle).
    """
    loader = Loader()
    fullname = loader.get_image_path(filename)
    try:
        image = pygame.image.load(fullname)
    except pygame.error, message:
        print 'Cannot load image:', fullname
        raise SystemExit, message
    image = image.convert_alpha()
    if colorkey is not None:
        if colorkey is -1:
            colorkey = image.get_at((0,0))
        image.set_colorkey(colorkey, RLEACCEL)
    return image, image.get_rect()
