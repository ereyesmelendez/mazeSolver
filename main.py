#git add .
#git commit -m "update readme with a description"
#git push origin main
from window import Window, Point, Line
from cell import Cell
win = Window(800, 600)

point1 = Point(12,20)
point2 = Point(30,40)
line = Line(point1, point2)
win.draw_line(line, "Red")

grid = [[Cell(win) for _ in range(20)] for _ in range(20)]
cell_size = 20
for i, row in enumerate(grid):
    for j, cell in enumerate(row):
        x1=j * cell_size
        y1 = i * cell_size
        x2 = (j +1) * cell_size
        y2 = (i +1) * cell_size
        cell.draw(x1, y1, x2, y2)

win.wait_for_close()# keep this at the end 