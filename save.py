for i in range(7):
    for j in range(9):
        if grid[i][j] == 0:
            grid[i][j] = random.randrange(1,7)
            if grid[i][j] == 0:
                tt.grid_zero(xvalues[i][j], yvalues[i][j])
            elif grid[i][j] == 1:
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


for i in range(7):
    for j in range(9):
        grid[i][j] = fall[i][j]
        fall[i][j] = 0
        if grid[i][j] == 0:
            if i == 0:
                tt.reset_c1()
            elif i == 1:
                tt.reset_c2()
            elif i == 2:
                tt.reset_c3()
            elif i == 3:
                tt.reset_c4()
            elif i == 4:
                tt.reset_c5()
            elif i == 5:
                tt.reset_c6()
            elif i == 6:
                tt.reset_c7()

if (grid[m][n] == grid[s][t+1] and grid[m][n] == grid[s][t-1]) or (grid[m][n] == grid[s][t+1] and grid[m][n] == grid[s][t+2]) or (grid[m][n] == grid[s][t-1] and grid[m][n] == grid[s][t-2]) or (grid[m][n] == grid[s+1][t] and grid[m][n] == grid[s-1][t]) or (grid[m][n] == grid[s+1][t] and grid[m][n] == grid[s+2][t]) or (grid[m][n] == grid[s-1][t] and grid[m][n] == grid[s-2][t]) and (grid[s][t] == grid[m][n+1] and grid[s][t] == grid[m][n-1]) or (grid[s][t] == grid[m][n+1] and grid[s][t] == grid[m][n+2]) or (grid[s][t] == grid[m][n-1] and grid[s][t] == grid[m][n-2]) or (grid[s][t] == grid[m+1][n] and grid[s][t] == grid[m-1][n]) or (grid[s][t] == grid[m+1][n] and grid[s][t] == grid[m+2][n]) or (grid[s][t] == grid[m-1][n] and grid[s][t] == grid[m-2][n]):

for i in range(5):
    for i in range(7):
        if (grid[i][j] == grid[i+1][j]) and (grid[i][j] == grid[i+2][j]) and (grid[i][j] == grid[i][j+1]) and (grid[i][j] == grid[i][j+2]):
            tt.clear(xvalues[i][j], yvalues[i][j])
            tt.clear(xvalues[i+1][j], yvalues[i+1][j])
            tt.clear(xvalues[i+2][j], yvalues[i+2][j])
            tt.clear(xvalues[i][j+1], yvalues[i][j+1])
            tt.clear(xvalues[i][j+2], yvalues[i][j+2])
            grid[i][j] = 0
            grid[i+1][j] = 0
            grid[i+2][j] = 0
            grid[i][j+1] = 0
            grid[i][j+2] = 0

        if (grid[i][j] == grid[i+1][j]) and (grid[i][j] == grid[i+2][j]) and (grid[i][j] == grid[i+2][j+1]) and (grid[i][j] == grid[i+2][j+2]):
            tt.clear(xvalues[i][j], yvalues[i][j])
            tt.clear(xvalues[i+1][j], yvalues[i+1][j])
            tt.clear(xvalues[i+2][j], yvalues[i+2][j])
            tt.clear(xvalues[i+2][j+1], yvalues[i+2][j+1])
            tt.clear(xvalues[i+2][j+2], yvalues[i+2][j+2])
            grid[i][j] = 0
            grid[i+1][j] = 0
            grid[i+2][j] = 0
            grid[i+2][j+1] = 0
            grid[i+2][j+2] = 0


        if (grid[i][j] == grid[i][j+1]) and (grid[i][j] == grid[i][j+2]) and (grid[i][j] == grid[i+1][j+2]) and (grid[i][j] == grid[i+2][j+2]):
            tt.clear(xvalues[i][j], yvalues[i][j])
            tt.clear(xvalues[i][j+1], yvalues[i][j+1])
            tt.clear(xvalues[i][j+2], yvalues[i][j+2])
            tt.clear(xvalues[i+1][j+2], yvalues[i+1][j+2])
            tt.clear(xvalues[i+2][j+2], yvalues[i+2][j+2])
            grid[i][j] = 0
            grid[i][j+1] = 0
            grid[i][j+2] = 0
            grid[i+1][j+2] = 0
            grid[i+2][j+2] = 0

        if (grid[i][j] == grid[i][j+1]) and (grid[i][j] == grid[i][j+2]) and (grid[i][j] == grid[i-1][j+2]) and (grid[i][j] == grid[i-2][j+2]):
            tt.clear(xvalues[i][j], yvalues[i][j])
            tt.clear(xvalues[i][j+1], yvalues[i][j+1])
            tt.clear(xvalues[i][j+2], yvalues[i][j+2])
            tt.clear(xvalues[i-1][j+2], yvalues[i-1][j+2])
            tt.clear(xvalues[i-2][j+2], yvalues[i-2][j+2])
            grid[i][j] = 0
            grid[i][j+1] = 0
            grid[i][j+2] = 0
            grid[i-1][j+2] = 0
            grid[i-2][j+2] = 0



for i in range(5):
    for j in range(9):
        if (grid[i][j] == grid[i+1] and grid[i][j] == grid[i][j+2]) or (grid[i][j] == grid[i+1][j] and grid[i][j] == grid[i+2][j]):
            check = True
        else:
            tt.invalid_swap()
            tt.clear_score()
            stddraw.show(10)
            swap1 = grid[m][n]
            swap2 = grid[s][t]
            tt.clear(xvalues[m][n], yvalues[m][n])
            tt.clear(xvalues[s][t], yvalues[s][t])
            grid[m][n] = swap2
            grid[s][t] = swap1
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
