from tkinter import Tk, BOTH, Canvas
class Window:
    def __init__(self, width, height):
        self.__root = Tk()
        self.__root.title("Title")
        self.__canvas = Canvas(self.__root, width=width, height=height)
        self.__canvas.pack()
        self.__running = False
        self.__root.protocol("WM_DELETE_WINDOW", self.close)

    def draw_line(self, Line, fill_color):
        Line.draw(self.__canvas, fill_color)


    def redraw(self):
        self.__root.update_idletasks()
        self.__root.update() 
    
    def wait_for_close(self, running=True):
        self.__running = True
        while self.__running is True:
            self.redraw()
    
    def close(self):
        self.__running = False
        
        
class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

class Line:
    def __init__(self,point1, point2):
        self.point1 = point1
        self.point2 = point2

    def draw(self, Canvas, fill_color):
        Canvas.create_line(self.point1.x, self.point1.y, self.point2.x, self.point2.y, fill=fill_color, width=2)
