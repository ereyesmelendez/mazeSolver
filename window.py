from tkinter import Tk, BOTH, Canvas
class Window:
    def __init__(self, width, height):
        self.__root = Tk()
        self.__root.title("Title")
        self.__canvas = Canvas(self.__root, width=width, height=height)
        self.__canvas.pack()
        self.__running = False

    def redraw(self):
        self.__root.update_idletasks()
        self.__root.update() 
    
    def wait_for_close(self, running=True):
        self.__running = True
        while self.__running is True:
            self.redraw()
    
    def close(self, running=False):
        self.__running = False
        self.__root.protocol()
        
