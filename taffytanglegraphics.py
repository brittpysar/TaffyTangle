import stdio
import stddraw
import pygame as pg

stddraw.setXscale(-5, 9)
stddraw.setYscale(-6.5, 6.5)

def grid():
    stddraw.line(-3.55, 4, -3.55, -5)
    stddraw.line(-3.55, -5, 3.55, -5)
    stddraw.line(3.55, 4, 3.55, -5)
    stddraw.setFontSize(50)
    stddraw.text(6.5, 5.1, 'score')

    stddraw.setPenRadius(.02)
    stddraw.line(5, 3.5, 5, 4.5)
    stddraw.line(5, 4.5, 8, 4.5)
    stddraw.line(8, 4.5, 8, 3.5)
    stddraw.line(8, 3.5, 5, 3.5)
    stddraw.setPenRadius(.02)

    stddraw.setPenColor(stddraw.WHITE)
    stddraw.filledRectangle(5, 3.5, 3, 1)
    stddraw.show(0)

def box(x, y):
    stddraw.setPenRadius(.02)
    stddraw.setPenColor(stddraw.BLACK)
    stddraw.line((x - .48), (y - .48),(x + .48), (y - .48))
    stddraw.line((x + .48), (y - .48), (x + .48), (y + .48))
    stddraw.line((x + .48), (y + .48), (x - .48), (y + .48))
    stddraw.line((x - .48), (y + .48), (x - .48), (y - .48))

def clear(x, y):
    stddraw.setPenColor(stddraw.WHITE)
    stddraw.filledRectangle(x - .51, y - .51, 1.05, 1.05)
    stddraw.show(100)

def clear_score():
    stddraw.setPenColor(stddraw.WHITE)
    stddraw.filledRectangle(4, 1, 6, 2)

def update_score(x):
    stddraw.setPenColor(stddraw.WHITE)
    stddraw.filledRectangle(5, 3.5, 3, 1)
    stddraw.show(1)
    stddraw.setFontSize(45)
    stddraw.setPenColor(stddraw.BLACK)
    stddraw.text(6.5, 4, x)
    stddraw.show(1)

def invalid_taffy():
    stddraw.setFontSize(24)
    stddraw.setPenColor(stddraw.RED)
    stddraw.text(6.5, 2, 'Please choose')
    stddraw.text(6.5, 1.5, 'a valid taffy')
    stddraw.show(1500)

def invalid_swap():
    stddraw.setFontSize(24)
    stddraw.setPenColor(stddraw.RED)
    stddraw.text(6.5, 2, 'No match detected!')
    stddraw.text(6.5, 1.5, 'Try again.')
    stddraw.show(1500)

def grid_zero(x, y):
    stddraw.setPenColor(stddraw.WHITE)
    stddraw.filledRectangle(x - .51, y - .51, 1.05, 1.05)
    stddraw.show(10)

def grid_one(x, y):
    stddraw.setPenColor(stddraw.BLUE)
    xd = [x + .4, x - .25, x + .25, x - .4]
    yd = [ y + .4, y + .4, y - .4, y - .4]
    stddraw.filledPolygon(xd, yd)
    stddraw.show(10)

def grid_two(x, y):
    stddraw.setPenColor(stddraw.RED)
    stddraw.filledSquare(x, y, .45)
    stddraw.show(10)

def grid_three(x,y):
    stddraw.setPenColor(stddraw.YELLOW)
    stddraw.filledCircle(x, y, .45)
    stddraw.show(10)

def grid_four(x,y):
    stddraw.setPenColor(stddraw.ORANGE)
    yd = [y + .4, y, y - .4, y]
    xd = [x, x + .4, x, x - .4]
    stddraw.filledPolygon(xd, yd)
    stddraw.show(10)

def grid_five(x,y):
    stddraw.setPenColor(stddraw.GREEN)
    xt = [x, x - .4, x+ .4]
    yt = [y + .4, y - .4, y - .4]
    stddraw.filledPolygon(xt, yt)
    stddraw.show(10)

def grid_six(x,y):
    stddraw.setPenColor(stddraw.MAGENTA)
    xd = [ x - .2, x + .45, x + .2, x - .45]
    yd = [ y + .4, y + .4, y - .4, y - .4]
    stddraw.filledPolygon(xd, yd)
    stddraw.show(10)

def reset_hmatches(x):
    for i in range (9):
        for j in range(7):
            x = 0

def reset_vmatches(x):
    for j in range(7):
        for i in range(9):
            x = 0

def reset_c1():
    stddraw.setPenColor(stddraw.WHITE)
    stddraw.filledRectangle(-3.5, -5, 1, 9)

def reset_c2():
    stddraw.setPenColor(stddraw.WHITE)
    stddraw.filledRectangle(-2.5, -5, 1, 9)

def reset_c3():
    stddraw.setPenColor(stddraw.WHITE)
    stddraw.filledRectangle(-1.5, -5, 1, 9)

def reset_c4():
    stddraw.setPenColor(stddraw.WHITE)
    stddraw.filledRectangle(-0.5, -5, 1, 9)

def reset_c5():
    stddraw.setPenColor(stddraw.WHITE)
    stddraw.filledRectangle(0.5, -5, 1, 9)

def reset_c6():
    stddraw.setPenColor(stddraw.WHITE)
    stddraw.filledRectangle(1.5, -5, 1, 9)

def reset_c7():
    stddraw.setPenColor(stddraw.WHITE)
    stddraw.filledRectangle(2.5, -5, 1, 9)
