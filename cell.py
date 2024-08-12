from window import Window, Point, Line
class Cell:
    def __init__(self, win=None):
        self.has_left_wall = True
        self.has_right_wall = True
        self.has_top_wall = True
        self.has_bottom_wall = True
        self._x1 = None
        self._y1 = None
        self._x2 = None
        self._y2 = None
        self._win = win
        self.visited = False

    def draw(self, x1: int, y1: int, x2: int, y2: int):
        self._x1 = min(x1, x2)
        self._y1 = min(y1, y2)
        self._x2 = max(x1, x2)
        self._y2 = max(y1, y2)
        if self._win is None:
            return
        
        left_wall_fill = "black" if self.has_left_wall else "white"
        right_wall_fill = "black" if self.has_right_wall else "white"
        top_wall_fill = "black" if self.has_top_wall else "white"
        bottom_wall_fill = "black" if self.has_bottom_wall else "white"
        self._win.draw_line(
            Line(Point(self._x1, self._y1), Point(self._x1, self._y2)),
            left_wall_fill
        )
        self._win.draw_line(
            Line(Point(self._x2, self._y1), Point(self._x2, self._y2)),
            right_wall_fill
        )
        self._win.draw_line(
            Line(Point(self._x1, self._y1), Point(self._x2, self._y1)),
            top_wall_fill
        )
        self._win.draw_line(
            Line(Point(self._x1, self._y2), Point(self._x2, self._y2)),
            bottom_wall_fill
        )