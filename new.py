import stdio
import random
import taffytanglegraphics as tt
import stddraw

#set values
score = 0
draw = True
play = False
click = 1
hmatch = 0
vmatch = 0
check = False
nomatch = False
drop = False

#board initialization
grid = [[0,0,0,0,0,0,0,0,0], [0,0,0,0,0,0,0,0,0], [0,0,0,0,0,0,0,0,0], [0,0,0,0,0,0,0,0,0], [0,0,0,0,0,0,0,0,0], [0,0,0,0,0,0,0,0,0], [0,0,0,0,0,0,0,0,0]]
xvalues = [[-3, -3, -3, -3, -3, -3, -3, -3, -3], [-2, -2, -2, -2, -2, -2, -2, -2, -2], [-1, -1, -1, -1, -1, -1, -1, -1, -1], [0, 0, 0, 0, 0, 0, 0, 0, 0], [1, 1, 1, 1, 1, 1, 1, 1, 1], [2, 2, 2, 2, 2, 2, 2, 2, 2], [3, 3, 3, 3, 3, 3, 3, 3, 3]]
yvalues = [[-4.5, -3.5, -2.5, -1.5, -0.5, .5, 1.5, 2.5, 3.5], [-4.5, -3.5, -2.5, -1.5, -0.5, .5, 1.5, 2.5, 3.5], [-4.5, -3.5, -2.5, -1.5, -0.5, .5, 1.5, 2.5, 3.5], [-4.5, -3.5, -2.5, -1.5, -0.5, .5, 1.5, 2.5, 3.5], [-4.5, -3.5, -2.5, -1.5, -0.5, .5, 1.5, 2.5, 3.5], [-4.5, -3.5, -2.5, -1.5, -0.5, .5, 1.5, 2.5, 3.5], [-4.5, -3.5, -2.5, -1.5, -0.5, .5, 1.5, 2.5, 3.5]]
hmatches = [0,0,0,0,0,0,0]
vmatches = [0,0,0,0,0,0,0,0,0]
fall = [[0,0,0,0,0,0,0,0,0], [0,0,0,0,0,0,0,0,0], [0,0,0,0,0,0,0,0,0], [0,0,0,0,0,0,0,0,0], [0,0,0,0,0,0,0,0,0], [0,0,0,0,0,0,0,0,0], [0,0,0,0,0,0,0,0,0]]

while draw == True:
    #generate initial board
    tt.grid()
    for i in range (7):
        for j in range (9):
            taffy = random.randrange(1,7)
            grid[i][j] = taffy

    #loop through and eliminate any matches
    for i in range (7):
        for j in range(9):
            if grid[i][j] == grid[i][j-1]:
                if taffy <= 5:
                    taffy += 1
                    grid[i][j] = taffy
                elif taffy > 5:
                    taffy -= 1
                    grid[i][j] = taffy
            elif  grid[i][j] == grid[i-1][j]:
                if taffy <= 5:
                    taffy += 1
                    grid[i][j] = taffy
                elif taffy > 5:
                    taffy -= 1
                    grid[i][j] = taffy


    #draw the taffies according to array
    for i in range (7):
        for j in range (9):
            if grid[i][j] == 1:
                tt.grid_one(xvalues[i][j], yvalues[i][j])
            elif grid[i][j] == 2:
                tt.grid_two(xvalues[i][j], yvalues[i][j])
            elif grid[i][j] == 3:
                tt.grid_three(xvalues[i][j], yvalues[i][j])
            elif grid[i][j] == 4:
                tt.grid_four(xvalues[i][j], yvalues[i][j])
            elif grid[i][j] == 5:
                tt.grid_five(xvalues[i][j], yvalues[i][j])
            elif grid[i][j] == 6:
                tt.grid_six(xvalues[i][j], yvalues[i][j])
    draw = False
    play = True
    stddraw.show(1000)

#start game play
while play == True and score < 100:
    #first click, draw box around clicked taffy
    if click == 1:
        if stddraw.mousePressed():
            mx = stddraw.mouseX()
            my = stddraw.mouseY()
            xn = (mx - (-3.5))
            yn = (my - (-5.0))
            n = int(yn)
            m = int(xn)
            tt.box(xvalues[m][n], yvalues[m][n])
            click = 2
            stddraw.show(10)
        stddraw.show(10)
    #second click
    if click == 2:
        if stddraw.mousePressed():
            x2 = stddraw.mouseX()
            y2 = stddraw.mouseY()
            xn2 = (x2 - (-3.5))
            yn2 = (y2 - (-5.0))
            t = int(yn2)
            s = int(xn2)
            stddraw.show(10)

            #forbid diagonal swaps
            if (m - s == 1 or m - s == -1) and (n - t == 1 or n - t == -1):
                tt.invalid_taffy()
                tt.clear_score()
                stddraw.show(10)
                tt.clear(xvalues[m][n], yvalues[m][n])
                stddraw.show(10)
                if grid[m][n] == 1:
                    tt.grid_one(xvalues[m][n], yvalues[m][n])
                elif grid[m][n] == 2:
                    tt.grid_two(xvalues[m][n], yvalues[m][n])
                elif grid[m][n] == 3:
                    tt.grid_three(xvalues[m][n], yvalues[m][n])
                elif grid[m][n] == 4:
                    tt.grid_four(xvalues[m][n], yvalues[m][n])
                elif grid[m][n] == 5:
                    tt.grid_five(xvalues[m][n], yvalues[m][n])
                elif grid[m][n] == 6:
                    tt.grid_six(xvalues[m][n], yvalues[m][n])
                click = 1

            #if second click is adjacent to first click, swap taffies
            elif (m - s == 1 or m - s == -1) or (n - t == 1 or n - t == -1):
                swap1 = grid[m][n]
                swap2 = grid[s][t]
                tt.clear(xvalues[m][n], yvalues[m][n])
                tt.clear(xvalues[s][t], yvalues[s][t])
                grid[m][n] = swap2
                grid[s][t] = swap1
                if grid[m][n] == 1:
                    tt.grid_one(xvalues[m][n], yvalues[m][n])
                elif grid[m][n] == 2:
                    tt.grid_two(xvalues[m][n], yvalues[m][n])
                elif grid[m][n] == 3:
                    tt.grid_three(xvalues[m][n], yvalues[m][n])
                elif grid[m][n] == 4:
                    tt.grid_four(xvalues[m][n], yvalues[m][n])
                elif grid[m][n] == 5:
                    tt.grid_five(xvalues[m][n], yvalues[m][n])
                elif grid[m][n] == 6:
                    tt.grid_six(xvalues[m][n], yvalues[m][n])
                if grid[s][t] == 1:
                    tt.grid_one(xvalues[s][t], yvalues[s][t])
                elif grid[s][t] == 2:
                    tt.grid_two(xvalues[s][t], yvalues[s][t])
                elif grid[s][t] == 3:
                    tt.grid_three(xvalues[s][t], yvalues[s][t])
                elif grid[s][t] == 4:
                    tt.grid_four(xvalues[s][t], yvalues[s][t])
                elif grid[s][t] == 5:
                    tt.grid_five(xvalues[s][t], yvalues[s][t])
                elif grid[s][t] == 6:
                    tt.grid_six(xvalues[s][t], yvalues[s][t])
                check = True


            #forbid nonadjacent swaps
            if m - s > 1 or m - s < -1:
                tt.invalid_taffy()
                tt.clear_score()
                stddraw.show(10)
                tt.clear(xvalues[m][n], yvalues[m][n])
                stddraw.show(10)
                if grid[m][n] == 1:
                    tt.grid_one(xvalues[m][n], yvalues[m][n])
                elif grid[m][n] == 2:
                    tt.grid_two(xvalues[m][n], yvalues[m][n])
                elif grid[m][n] == 3:
                    tt.grid_three(xvalues[m][n], yvalues[m][n])
                elif grid[m][n] == 4:
                    tt.grid_four(xvalues[m][n], yvalues[m][n])
                elif grid[m][n] == 5:
                    tt.grid_five(xvalues[m][n], yvalues[m][n])
                elif grid[m][n] == 6:
                    tt.grid_six(xvalues[m][n], yvalues[m][n])
                click = 1

            #forbid nonadjacent moves
            if n - t > 1 or n - t < -1:
                tt.invalid_taffy()
                tt.clear_score()
                stddraw.show(10)
                tt.clear(xvalues[m][n], yvalues[m][n])
                stddraw.show(10)
                if grid[m][n] == 1:
                    tt.grid_one(xvalues[m][n], yvalues[m][n])
                elif grid[m][n] == 2:
                    tt.grid_two(xvalues[m][n], yvalues[m][n])
                elif grid[m][n] == 3:
                    tt.grid_three(xvalues[m][n], yvalues[m][n])
                elif grid[m][n] == 4:
                    tt.grid_four(xvalues[m][n], yvalues[m][n])
                elif grid[m][n] == 5:
                    tt.grid_five(xvalues[m][n], yvalues[m][n])
                elif grid[m][n] == 6:
                    tt.grid_six(xvalues[m][n], yvalues[m][n])
                click = 1


            #check if swap results in match
            while check == True:

                hmatch = 0
                for i in range(9):
                    if (grid[m][i] == grid[m][n]):
                        hmatch += 1
                if hmatch >= 3:
                    for i in range(5):
                        if (grid[m][i] == grid[m][n]) and (grid[m][i+1] == grid[m][n]) and (grid[m][i+2] == grid[m][n]) and (grid[m][i+3] == grid[m][n]) and (grid[m][i+4] == grid[m][n]):
                            grid[m][i] = 0
                            grid[m][i+1] = 0
                            grid[m][i+2] = 0
                            grid[m][i+3] = 0
                            grid[m][i+4] = 0
                            for i in range(7):
                                if grid[m][i] == 0:
                                    tt.grid_zero(xvalues[m][i], yvalues[m][i])
                                    stddraw.show(100)

                    for i in range(6):
                        if (grid[m][i] == grid[m][n]) and (grid[m][i+1] == grid[m][n]) and (grid[m][i+2] == grid[m][n]) and (grid[m][i+3] == grid[m][n]):
                            grid[m][i] = 0
                            grid[m][i+1] = 0
                            grid[m][i+2] = 0
                            grid[m][i+3] = 0
                            for i in range(7):
                                if grid[m][i] == 0:
                                    tt.grid_zero(xvalues[m][i], yvalues[m][i])
                                    stddraw.show(100)
                    for i in range(7):
                        if (grid[m][i] == grid[m][n]) and (grid[m][i+1] == grid[m][n]) and (grid[m][i+2] == grid[m][n]):
                            grid[m][i] = 0
                            grid[m][i+1] = 0
                            grid[m][i+2] = 0
                            for i in range(7):
                                if grid[m][i] == 0:
                                    tt.grid_zero(xvalues[m][i], yvalues[m][i])
                                    stddraw.show(100)

                check = False
                drop = True
                click = 1

                hmatch = 0
                for i in range(9):
                    if (grid[s][i] == grid[s][t]):
                        hmatch += 1
                if hmatch >= 3:
                    for i in range(5):
                        if (grid[s][i] == grid[s][t]) and (grid[s][i+1] == grid[s][t]) and (grid[s][i+2] == grid[s][t]) and (grid[s][i+3] == grid[s][t]) and (grid[s][i+4] == grid[s][t]):
                            grid[s][i] = 0
                            grid[s][i+1] = 0
                            grid[s][i+2] = 0
                            grid[s][i+3] = 0
                            grid[s][i+4] = 0
                            for i in range(9):
                                if grid[s][i] == 0:
                                    tt.grid_zero(xvalues[s][i], yvalues[s][i])
                                    stddraw.show(100)

                    for i in range(6):
                        if (grid[s][i] == grid[s][t]) and (grid[s][i+1] == grid[s][t]) and (grid[s][i+2] == grid[s][t]) and (grid[s][i+3] == grid[s][t]):
                            grid[s][i] = 0
                            grid[s][i+1] = 0
                            grid[s][i+2] = 0
                            grid[s][i+3] = 0
                            for i in range(9):
                                if grid[s][i] == 0:
                                    tt.grid_zero(xvalues[s][i], yvalues[s][i])
                                    stddraw.show(100)
                    for i in range(7):
                        if (grid[s][i] == grid[s][t]) and (grid[s][i+1] == grid[s][t]) and (grid[s][i+2] == grid[s][t]):
                            grid[s][i] = 0
                            grid[s][i+1] = 0
                            grid[s][i+2] = 0
                            for i in range(9):
                                if grid[s][i] == 0:
                                    tt.grid_zero(xvalues[s][i], yvalues[s][i])
                                    stddraw.show(100)
                check = False
                drop = True
                click = 1

                vmatch = 0
                for i in range(7):
                    if (grid[i][n] == grid[m][n]):
                        vmatch += 1
                if vmatch >= 3:
                    for i in range(3):
                        if (grid[i][n] == grid[m][n]) and (grid[i+1][n] == grid[m][n]) and (grid[i+2][n] == grid[m][n]) and (grid[i+3][n] == grid[m][n]) and (grid[i+4][n] == grid[m][n]):
                            grid[i][n] = 0
                            grid[i+1][n] = 0
                            grid[i+2][n] = 0
                            grid[i+3][n] = 0
                            grid[i+4][n] = 0
                            for i in range(7):
                                if grid[i][n] == 0:
                                    tt.grid_zero(xvalues[i][n], yvalues[i][n])
                                    stddraw.show(100)

                    for i in range(4):
                        if (grid[i][n] == grid[m][n]) and (grid[i+1][n] == grid[m][n]) and (grid[i+2][n] == grid[m][n]) and (grid[i+3][n] == grid[m][n]):
                            grid[i][n] = 0
                            grid[i+1][n] = 0
                            grid[i+2][n] = 0
                            grid[i+3][n] = 0
                            for i in range(7):
                                if grid[i][n] == 0:
                                    tt.grid_zero(xvalues[i][n], yvalues[i][n])
                                    stddraw.show(100)
                    for i in range(5):
                        if (grid[i][n] == grid[m][n]) and (grid[i+1][n] == grid[m][n]) and (grid[i+2][n] == grid[m][n]):
                            grid[i][n] = 0
                            grid[i+1][n] = 0
                            grid[i+2][n] = 0
                            for i in range(7):
                                if grid[i][n] == 0:
                                    tt.grid_zero(xvalues[i][n], yvalues[i][n])
                                    stddraw.show(100)
                check = False
                drop = True
                click = 1

                vmatch = 0
                for i in range(7):
                    if (grid[i][t] == grid[s][t]):
                        vmatch += 1
                if vmatch >= 3:
                    for i in range(3):
                        if (grid[i][t] == grid[s][t]) and (grid[i+1][t] == grid[s][t]) and (grid[i+2][t] == grid[s][t]) and (grid[i+3][t] == grid[s][t]) and (grid[i+4][t] == grid[s][t]):
                            grid[i][t] = 0
                            grid[i+1][t] = 0
                            grid[i+2][t] = 0
                            grid[i+3][t] = 0
                            grid[i+4][t] = 0
                            for i in range(7):
                                if grid[i][t] == 0:
                                    tt.grid_zero(xvalues[i][t], yvalues[i][t])
                                    stddraw.show(100)

                    for i in range(4):
                        if (grid[i][t] == grid[s][t]) and (grid[i+1][t] == grid[s][t]) and (grid[i+2][t] == grid[s][t]) and (grid[i+3][t] == grid[s][t]):
                            grid[i][t] = 0
                            grid[i+1][t] = 0
                            grid[i+2][t] = 0
                            grid[i+3][t] = 0
                            for i in range(7):
                                if grid[i][t] == 0:
                                    tt.grid_zero(xvalues[i][t], yvalues[i][t])
                                    stddraw.show(100)
                    for i in range(5):
                        if (grid[i][t] == grid[s][t]) and (grid[i+1][t] == grid[s][t]) and (grid[i+2][t] == grid[s][t]):
                            grid[i][t] = 0
                            grid[i+1][t] = 0
                            grid[i+2][t] = 0
                            for i in range(7):
                                if grid[i][n] == 0:
                                    tt.grid_zero(xvalues[i][t], yvalues[i][t])
                                    stddraw.show(100)

                check = False
                drop = True
                click = 1





            stddraw.show(10)
        stddraw.show(10)
    stddraw.show(10)
stddraw.show()
