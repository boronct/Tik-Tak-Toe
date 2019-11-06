from graphics import *

def main():
    win = GraphWin("Tik-Tak-Toe", 600, 600)

    l1 = Line(Point(0,200),Point(600,200)).draw(win)
    l1.setWidth(10)
    l2 = Line(Point(0,400),Point(600,400)).draw(win)
    l2.setWidth(10)
    l3 = Line(Point(200,0),Point(200,600)).draw(win)
    l3.setWidth(10)
    l4 = Line(Point(400,0),Point(400,600)).draw(win)
    l4.setWidth(10)

    win.getMouse()
main()

# This is a comment from dad.
