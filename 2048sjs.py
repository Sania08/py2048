def addnum(grida):

    i=random.randrange(0,k)
    j=random.randrange(0,k)
    if grida[i][j]==0:
        grida[i][j] = random.choice([2, 4])
    else:
        grida=addnum(grida)
    return grida


def move_left(col):
    new_col = np.zeros(k, dtype=col.dtype)
    j = 0
    s = None
    for i in range(col.size):
        if col[i] != 0: # number different from zero
            if s == None:
                s = col[i]
            else:
                if s == col[i]:
                    new_col[j] = 2 * col[i]
                    j += 1
                    s = None
                else:
                    new_col[j] = s
                    j += 1
                    s = col[i]
    if s != None:
        new_col[j] = s
    return new_col


def down(gridd):
    gridd = np.rot90(gridd, -1)
    for i in range(0, k):
        gridd[i] = move_left(gridd[i])
    gridd=np.rot90(gridd)
    return gridd


def up(gridu):
    gridu = np.rot90(gridu)
    for i in range(0, k):
        gridu[i] = move_left(gridu[i])
    gridu = np.rot90(gridu,-1)
    return gridu


def left(gridl):
    for i in range(0, k):
        gridl[i] = move_left(gridl[i])
    return gridl


def right(gridr):
    gridr=np.fliplr(gridr)
    for i in range(0, k):
        gridr[i] = move_left(gridr[i])
    gridr=np.fliplr(gridr)
    return gridr


def prt(pgrid):
    for i in range(0,k):
        for j in range(0,k):
            print(int(grid[i][j]),end=" ")
        print()


def equal(grid_1,grid_2):
    comparison = grid_1 == grid_2
    equal_arrays = comparison.all()

    return(equal_arrays)



import numpy as np
import random
import msvcrt
import os
import time


print("### WELCOME TO 2048 GAME ###")
k=int(input("enter the size of grid:"))
grid= np.zeros(shape=(k,k))
w=int(input("Enter the winning number:"))
grid = addnum(grid)
print(grid)
status=0
while (status==0):
    r = 0
    adj = 0

    print("Press the key")
    x = msvcrt.getch()
    if  ord(x)==115:
        m=grid.copy()
        grid = down(grid)

    elif ord(x) ==119:
        m=grid.copy()
        grid = up(grid)

    elif ord(x) ==97:
        m=grid.copy()
        grid = left(grid)

    elif ord(x) ==100:
        m=grid.copy()
        grid = right(grid)

    time.sleep(1)
    os.system('cls')

    if equal(m,grid)==True:
        print("invalid move")
    else:
        grid = addnum(grid)
        print(grid)





#winning condition
    for i in range(0,k):
        for j in range(0,k):
            if grid[i][j]==w:
                print("YOU WIN!!!")
                status=1
#loosing condition
    for i in range(0, k):
        for j in range(0, k):
            if grid[i][j] == 0:
                r = 1


    for i in range(0,k-1):
            for j in range(0, k-1):
                if grid[i][j]==grid[i][j+1] or grid[i][j]==grid[i+1][j]:
                        adj=1


    if r==0 and adj==0:
        print("OOPS YOU LOST!!!")
        status=1







