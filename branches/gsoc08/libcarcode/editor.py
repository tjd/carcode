import os
import widgets

template = """
class CarScript:
    def __init__(self, car):
        # Your initialization code here
        pass
        
    def update(self, car):
        # Main script code here
        pass
"""

class Editor(widgets.Window):
    def __init__(self, filename="", callback=None):
        widgets.Window.__init__(self, "Editor: ", size=(700, 500), backcolor=(0.2,0.2,0.2))
        self.centered = True
        self.callback = callback
        self.filename = filename
        
        self.layout = widgets.Pack(size=self.size, margin=3, padding=4)
        self.layout_menu = widgets.Pack(widgets.HORIZONTAL, margin=3, padding=5, size=(32, 32))
        
        self.txtEditor = widgets.TextArea()
        
        if filename:
            try:
                fd = file(filename, 'r')
                self.txtEditor.set_text(fd.read())
                fd.close()
                self.label.set_text('Editor: %s' % os.path.basename(filename))
            except:
                pass
        else:
            self.txtEditor.set_text(template)
            self.label.set_text('Editor: *New File*')
        
        self.btnSave = widgets.Button(widgets.Label("Save"))
        self.btnClose = widgets.Button(widgets.Label("Close"))
        
        self.btnClose.onClick.subscribe(self.cbClose)
        self.btnSave.onClick.subscribe(self.cbSave)
        
        self.layout_menu.add_entity(self.btnSave)
        self.layout_menu.add_entity(self.btnClose)
        
        self.layout.add_entity(self.layout_menu, expand=False)
        self.layout.add_entity(self.txtEditor)
        
        self.add_entity(self.layout)
    
    def cbSaveDlg(self, filename):
        self.filename = filename
        if filename != "":
            fd = file(filename, 'w')
            fd.write(self.txtEditor.get_text())
            fd.close()
            self.label.set_text("Editor: %s" % os.path.basename(filename))
        
    def cbSave(self, btn):
        if self.filename:
            self.cbSaveDlg(self.filename)
        else:
            dlg = widgets.FileSaveDialog("Save File", callback=self.cbSaveDlg, size=(320, 240))
            self.parent.add_entity(dlg)
        
    def cbClose(self, btn):
        self.parent.remove_entity(self)
        if self.callback is not None:
            self.callback(self.filename)