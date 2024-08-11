#git add .
#git commit -m "update readme with a description"
#git push origin main
from window import Window, Point, Line
win = Window(800, 600)

point1 = Point(12,20)
point2 = Point(30,40)
line = Line(point1, point2)
win.draw_line(line, "Red")

win.wait_for_close()# keep this at the end 