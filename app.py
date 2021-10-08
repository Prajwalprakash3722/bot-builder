import numpy as np
from random import randint
import time


def point_generator():
    return randint(10), randint(10)


def SL_genrator(nL, nS):
    start = time.process_time()
    # ladders

    small_ladders = int(0.66 * nL)
    large_ladders = nL - small_ladders

    ladders = {}

    # generating small ladders
    count = 0
    while count != nL:
        r1 = randint(1, 9)
        c1 = randint(0, 9)

        while (r1, c1) == (0, 0) or (r1, c1) == (9, 0) or ((r1, c1) in ladders.keys()):
            r1 = randint(1, 9)
            c1 = randint(0, 9)

        r2 = randint(1, 9)
        c2 = randint(0, 9)

        dist = abs(r1 - r2) + abs(c1 - c2)
        while (
            (r1, c1) == (0, 0)
            or (r1, c1) == (9, 0)
            or (r1, c1) == (r2, c2)
            or ((r2, c2) in ladders.values())
            or (r1 <= r2)
        ):
            r2 = randint(1, 9)
            c2 = randint(0, 9)
            if time.process_time() - start > 1:
                return

        count += 1
        ladders[(r1, c1)] = (r2, c2)
    count = 0
    snakes = {}
    while count != nS:
        r1 = randint(1, 9)
        c1 = randint(0, 9)

        while (
            (r1, c1) == (0, 0)
            or (r1, c1) == (9, 0)
            or ((r1, c1) in snakes.keys())
            or ((r1, c1) in ladders.keys())
        ):
            r1 = randint(1, 9)
            c1 = randint(0, 9)
            if time.process_time() - start > 1:
                return

        r2 = randint(1, 9)
        c2 = randint(0, 9)

        dist = abs(r1 - r2) + abs(c1 - c2)
        while (
            (r1, c1) == (0, 0)
            or (r1, c1) == (9, 0)
            or (r1, c1) == (r2, c2)
            or ((r2, c2) in snakes.values())
            or (r1 >= r2)
        ):
            r2 = randint(1, 9)
            c2 = randint(0, 9)
            if time.process_time() - start > 1:
                return

        count += 1
        snakes[(r1, c1)] = (r2, c2)

    return [ladders, snakes]


temp = SL_genrator(6, 5)
while not temp:
    print("redoing")
    temp = SL_genrator(6, 5)

# print(temp)
import tkinter as tk
from time import sleep
from random import randint

root = tk.Tk()

Grid = []
for i in range(10):
    GridRow = []
    for j in range(10):
        GridRow.append("Empty")
    Grid.append(GridRow)
Grid[0][0] = "End"
Grid[9][0] = "Start"


# #Snakes

for (_key, _val) in temp[1].items():
    print(_key, _val)
    Grid[_key[0]][_key[1]] = [_val[0], _val[1], "S"]

# #Ladders

for (_key, _val) in temp[0].items():
    Grid[_key[0]][_key[1]] = [_val[0], _val[1], "L"]

# [Row,Collumn]
# player1 = [9,0]
# player2 = [9,0]
# print(Grid)
players = []
players_clrs = ["purple", "cyan", "pink", "blue"]
for i in range(4):
    players.append([9, 0])
print(players)
LabelGrid = []


def updateGrid():
    global players
    global players_clrs
    global LabelGrid
    global Grid
    for i in LabelGrid:
        i.grid_forget()
    for i in range(10):
        for j in range(10):
            root.grid_rowconfigure(i, weight=1, minsize=60)
            root.grid_columnconfigure(j, weight=1, minsize=60)
            Label = tk.Label(root)
            Label.grid(column=j, row=i, sticky="nsew")
            LabelGrid.append(Label)
            if (i + j) % 2 == 0:
                Label.configure(bg="Black")
            if Grid[i][j] == "Empty":
                Label.configure(text="")
            elif Grid[i][j] == "Start":
                Label.configure(text="Start", bg="Sky Blue")
            elif Grid[i][j] == "End":
                Label.configure(text="End", bg="Gold")
            else:
                LabelText = (
                    "Leads to\nCollumn "
                    + str(Grid[i][j][1])
                    + "\nRow "
                    + str(Grid[i][j][0])
                )
                Label.configure(
                    text=LabelText, bg="Red" if Grid[i][j][2] == "S" else "Green"
                )

    for i in range(3):
        p = tk.Label(root, text="Player" + str(i + 1), bg=players_clrs[i])
        p.grid(column=players[i][1], row=players[i][0], sticky="n")
        LabelGrid.append(p)
    # p2 = tk.Label(root,text="Player 2",bg="Blue")
    # p2.grid(column=player2[1],row=player2[0],sticky="s")
    # LabelGrid.append(p2)
    root.update()


def movePlayer(player, spaces):
    global Grid
    endSpace = player
    for _ in range(spaces):
        if endSpace == [0, 0]:
            return endSpace
        if endSpace[0] % 2 == 1:
            if endSpace[1] == 9:
                endSpace[0] -= 1
            else:
                endSpace[1] += 1
        elif endSpace[1] == 0:
            endSpace[0] -= 1
        else:
            endSpace[1] -= 1
    if type(Grid[endSpace[0]][endSpace[1]]) == list:
        print("here")
        return [Grid[endSpace[0]][endSpace[1]][0], Grid[endSpace[0]][endSpace[1]][1]]
    return endSpace


Turn = 0
Winner = ""

Text = tk.Label(root, text="Loading")
WaitVariable = tk.IntVar()
Button = tk.Button(root, text="Roll", command=lambda: WaitVariable.set(1))
Text.grid(column=0, row=10, columnspan=10, sticky="nsew")
Button.grid(column=0, row=11, columnspan=10, sticky="nsew")

root.grid_rowconfigure(10, weight=1, minsize=32)
root.grid_rowconfigure(11, weight=1, minsize=32)

updateGrid()
while True:
    Text.configure(text="Player " + str(Turn + 1) + "s turn")
    Button.wait_variable(WaitVariable)
    roll = randint(1, 6)
    Text.configure(text="Rolled a " + str(roll))

    players[Turn] = movePlayer(players[Turn], roll)
    if players[Turn] == [0, 0]:
        Winner = "Player " + str(Turn)
        break
    # if Turn%2 == 1:
    #   player1 = movePlayer(player1,roll)
    #   if player1 == [0,0]:
    #     Winner = "Player 1"
    #     break
    # else:
    #   player2 = movePlayer(player2,roll)
    #   if player2 == [0,0]:
    #     Winner = "Player 1"
    #     break
    Turn = (1 + Turn) % 3
    updateGrid()
    sleep(1)

Text.configure(text=Winner + " wins!")
updateGrid()
