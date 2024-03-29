from graphics import *


window = GraphWin("Arrow", 800, 550)

def main():
    value = 0;
    entry1 = Entry(Point(300, 50),20)
    entry1.draw(window)
    if value==1:
        label = Text(Point(window.getWidth()/2-5,20),"Honk")
        label.setSize(30)
        label.draw(window)
    if value==0:
        label = Text(Point(window.getWidth()/2-5,20),"Siren")
        label.setTextColor('red')
        label.setSize(30)
        label.draw(window)
    

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
            if location == '1':
                aLine = Line(Point(window.getWidth()/2,100+10), Point(window.getWidth()/2,450))
                aLine.draw(window)
                bLine = Line(Point(window.getWidth()/2+20,100), Point(window.getWidth()/2-80,window.getHeight()/2-80))
                bLine.draw(window)
                cLine = Line(Point(window.getWidth()/2-20,100), Point(window.getWidth()/2+80,window.getHeight()/2-80))
                cLine.draw(window)
            if location == '2':
                aLine = Line(Point(window.getWidth()/4,window.getHeight()*3/4), Point(window.getWidth()*3/4,window.getHeight()/4))
                aLine.draw(window)
                bLine = Line(Point(window.getWidth()*3/4-150,window.getHeight()/4), Point(window.getWidth()*3/4+30,window.getHeight()/4))
                bLine.draw(window)
                cLine = Line(Point(window.getWidth()*3/4,window.getHeight()/4+150), Point(window.getWidth()*3/4,window.getHeight()/4-30))
                cLine.draw(window)
            if location == '3':
                aLine = Line(Point(100,window.getHeight()/2), Point(700-20,window.getHeight()/2))
                aLine.draw(window)
                bLine = Line(Point(700,window.getHeight()/2+20), Point(window.getWidth()/2+180,window.getHeight()/2-90))
                bLine.draw(window)
                cLine = Line(Point(700,window.getHeight()/2-20), Point(window.getWidth()/2+180,window.getHeight()/2+90))
                cLine.draw(window)
            if location == '4':
                aLine = Line(Point(window.getWidth()/4,window.getHeight()/4), Point(window.getWidth()*3/4,window.getHeight()*3/4))
                aLine.draw(window)
                bLine = Line(Point(window.getWidth()*3/4-150,window.getHeight()*3/4), Point(window.getWidth()*3/4+30,window.getHeight()*3/4))
                bLine.draw(window)
                cLine = Line(Point(window.getWidth()*3/4,window.getHeight()*3/4-150), Point(window.getWidth()*3/4,window.getHeight()*3/4+30))
                cLine.draw(window)
            if location == '5':
                aLine = Line(Point(window.getWidth()/2,100), Point(window.getWidth()/2,450-10))
                aLine.draw(window)
                bLine = Line(Point(window.getWidth()/2+20,450), Point(window.getWidth()/2-80,window.getHeight()/2+80))
                bLine.draw(window)
                cLine = Line(Point(window.getWidth()/2-20,450), Point(window.getWidth()/2+80,window.getHeight()/2+80))
                cLine.draw(window)
            if location == '6':
                aLine = Line(Point(window.getWidth()/4,window.getHeight()*3/4), Point(window.getWidth()*3/4,window.getHeight()/4))
                aLine.draw(window)
                bLine = Line(Point(window.getWidth()/4+150,window.getHeight()*3/4), Point(window.getWidth()/4-30,window.getHeight()*3/4))
                bLine.draw(window)
                cLine = Line(Point(window.getWidth()/4,window.getHeight()*3/4-150), Point(window.getWidth()/4,window.getHeight()*3/4+30))
                cLine.draw(window)
            if location == '7':
                aLine = Line(Point(100+20,window.getHeight()/2), Point(700,window.getHeight()/2))
                aLine.draw(window)
                bLine = Line(Point(100,window.getHeight()/2+20), Point(window.getWidth()/2-180,window.getHeight()/2-90))
                bLine.draw(window)
                cLine = Line(Point(100,window.getHeight()/2-20), Point(window.getWidth()/2-180,window.getHeight()/2+90))
                cLine.draw(window)
            if location == '8':
                aLine = Line(Point(window.getWidth()/4,window.getHeight()/4), Point(window.getWidth()*3/4,window.getHeight()*3/4))
                aLine.draw(window)
                bLine = Line(Point(window.getWidth()/4+150,window.getHeight()/4), Point(window.getWidth()/4-30,window.getHeight()/4))
                bLine.draw(window)
                cLine = Line(Point(window.getWidth()/4,window.getHeight()/4+150), Point(window.getWidth()/4,window.getHeight()/4-30))
                cLine.draw(window)
            
            
            setWidth(aLine,bLine,cLine)
    window.getMouse() # pause for click in window
    window.close()

def undrawAll(aLine,bLine,cLine):
    aLine.undraw()
    bLine.undraw()
    cLine.undraw()

def setWidth(aLine,bLine,cLine):
    aLine.setWidth(60)
    bLine.setWidth(60)
    cLine.setWidth(60)



main()