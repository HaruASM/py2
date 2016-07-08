import tkinter as tk

class Popmodal :

    def __init__ (self, w = 400, h = 300) :
        self.width = w
        self.height = h
        self.root = tk.Tk()
        
        self.mainDialog = tk.Frame( self.root, width = self.width, height = self.height)
        self.mainDialog.pack( side = tk.RIGHT )
        
        self.root.bind("<Escape>", self.exit)
        self.root.bind("<Key>", self.keys )
        
    def keys(self, event) :
        print( event.keysym )

                       
    def update(self):
        self.root.update()

    def exit(self, event) :
        self.root.destroy()



if __name__ == '__main__' :
    print("hello".format("py"))
    
    menu = Popmodal()
    menu.root.update()

    howToOut = tk.Message( menu.root, text = "ESC key is out" )

    howToOut.pack()    
    
