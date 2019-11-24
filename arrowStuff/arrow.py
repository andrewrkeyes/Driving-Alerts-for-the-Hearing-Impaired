from graphics import *


window = GraphWin("Arrow", 800, 550)

def main():
    entry1 = Entry(Point(300, 50),20)
    entry1.draw(window)

    aLine = Line(Point(window.getWidth()/2,window.getHeight()/2+50), Point(window.getWidth()/2,window.getHeight()/2-50))
    aLine.draw(window)
    bLine = Line(Point(window.getWidth()/2-50,window.getHeight()/2+50), Point(window.getWidth()/2+50,window.getHeight()/2-50))
    bLine.draw(window)
    cLine = Line(Point(window.getWidth()/2-50,window.getHeight()/2-50), Point(window.getWidth()/2+50,window.getHeight()/2+50))
    cLine.draw(window)
    setWidth(aLine,bLine,cLine)


    savedValue = entry1.getText()
    while True:   
        k = window.checkKey()
        location = entry1.getText()
        if location != savedValue:
            savedValue = location
            print(location)
            undrawAll(aLine,bLine,cLine)
            if location == '12':
                aLine = Line(Point(window.getWidth()/2,100), Point(window.getWidth()/2,450))
                aLine.draw(window)
                bLine = Line(Point(window.getWidth()/2,100), Point(window.getWidth()/2-20,window.getHeight()/2-80))
                bLine.draw(window)
                cLine = Line(Point(window.getWidth()/2,100), Point(window.getWidth()/2+20,window.getHeight()/2-80))
                cLine.draw(window)
            if location == '3':
                aLine = Line(Point(100,window.getHeight()/2), Point(700,window.getHeight()/2))
                aLine.draw(window)
                bLine = Line(Point(700,window.getHeight()/2), Point(window.getWidth()/2+80,window.getHeight()/2-20))
                bLine.draw(window)
                cLine = Line(Point(700,window.getHeight()/2), Point(window.getWidth()/2+80,window.getHeight()/2+20))
                cLine.draw(window)
            if location == '6':
                aLine = Line(Point(window.getWidth()/2,100), Point(window.getWidth()/2,450))
                aLine.draw(window)
                bLine = Line(Point(window.getWidth()/2,450), Point(window.getWidth()/2-20,window.getHeight()/2+80))
                bLine.draw(window)
                cLine = Line(Point(window.getWidth()/2,450), Point(window.getWidth()/2+20,window.getHeight()/2+80))
                cLine.draw(window)
            if location == '9':
                aLine = Line(Point(100,window.getHeight()/2), Point(700,window.getHeight()/2))
                aLine.draw(window)
                bLine = Line(Point(100,window.getHeight()/2), Point(window.getWidth()/2-80,window.getHeight()/2-20))
                bLine.draw(window)
                cLine = Line(Point(100,window.getHeight()/2), Point(window.getWidth()/2-80,window.getHeight()/2+20))
                cLine.draw(window)
            
            
            setWidth(aLine,bLine,cLine)
    window.getMouse() # pause for click in window
    window.close()

def undrawAll(aLine,bLine,cLine):
    aLine.undraw()
    bLine.undraw()
    cLine.undraw()

def setWidth(aLine,bLine,cLine):
    aLine.setWidth(6)
    bLine.setWidth(6)
    cLine.setWidth(6)



main()