from graphics import *

def main():
    win = GraphWin("Arrow", 1000, 1000)
    aLine = Line(Point(1,1), Point(999,999))
    aLine.draw(win)
    bLine = Line(Point(999,999), Point(1,1))
    bLine.draw(win)
    win.getMouse() # pause for click in window
    win.close()
main()