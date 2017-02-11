''''Author: Mohammad Hamad
    Class: CSCI 487 - AI, IUPUI'''''

#imports
import random

# number of queens (also N x N board)
N = 8

S = [] #index is x pos, val is y pos

hits   = [] #hits on queens
board  = [] #board of hits

WIDTH  = N
HEIGHT = N

NUM_QUEENS = N
randomNumSeed = 1238
active_col = -1


# i is the column
def getHitsAtQueen(i):
    return board[i][S[i]]


def getQueenPos(i):
    return [i, S[i]]


#checks if you have the final state
def isFinalState():

        for i in range(0,NUM_QUEENS):
            if board[i][S[i]] != 0:
                return False

       #if all values is 0
        return True


#hits cell(tile) on board
def hitCell(x,y):

    board[x][y] += 1


#keeps track of conflicts on the board
def conflictCounting():

    #loop thru all queens:
    for s in range(len(S)):
        #get queens coordinate
        q = getQueenPos(s)
        qx = q[0]
        qy = q[1]

        # col
        col = qx #doesn't change
        row = 0  #changes
        for row in range(HEIGHT):
            if row != qy:
                hitCell(col,row)

        # row
        col = 0  #changes
        row = qy #doesn't change
        for col in range(WIDTH):
            if col != qx:
                hitCell(col,row)

        # diagonal up-right
        col = qx #changes
        row = qy #changes
        while True:
            col += 1
            row -= 1
            if col >= WIDTH or row < 0:
                break
            hitCell(col,row)

        # diagonal up-left
        col = qx #changes
        row = qy #changes
        while True:
            col -= 1
            row -= 1
            if col < 0 or row < 0:
                break
            hitCell(col,row)

        # diagonal down-right
        col = qx #changes
        row = qy #changes
        while True:
            col += 1
            row += 1
            if col >= WIDTH or row >= HEIGHT:
                break
            hitCell(col,row)

        # diagonal down-left
        col = qx #changes
        row = qy #changes
        while True:
            col -= 1
            row += 1
            if col < 0 or row >= HEIGHT:
                break
            hitCell(col,row)


def create_board():
    for i in range(N):
        sub = []
        board.append(sub)
        for j in range(N):
            board[i].append(0)



def print_hits():
    for i in range(len(board)):
        print("")
        for j in range(len(board[i])):
            print(board[i][j], end="")
            print(" ", end="")
        print("")


def print_queens():
    print("\nQueens: ")
    for i in range(len(S)):
        print(" [" + str(i) + ", " + str(S[i]) + "] ")

#clears board
def clear():
    for i in range(len(board)):
        for j in range(len(board[i])):
            board[i][j] = 0

#inits board,queens,hits
#uses min-conflict strategy
def initialize():
    # seed the random number generator
    random.seed(randomNumSeed)


    create_board()

    #init search index
    active_col = 0

    # make 1st queen in random row on 1st col
    r = random.randint(0, 100000) % (N - 1)
    S.append(r)

    conflictCounting()

    print("BEFORE: ")

    print_hits()

    print_queens()

    for col in range(N):
        #min hits so far
        tMin = 999

        #cells with min hits so far
        tCells = []

        for row in range(N):

            #check min if
            if tMin >= board[col][row]:

                #if hits same as lowest hits so far
                if tMin == board[col][row]:
                    #add cell
                    tCells.append(row)

                #if found cell with fewer hits
                else:
                    #record lower hit count
                    tMin = board[col][row]

                    #clear list of cells, add new lower-hit cell
                    tCells = []
                    tCells.append(row)

        #if we are not at the last col
        if col != N-1:

            #add queen to list
            S.append(random.choice(tCells))

            clear()

            #update hits
            conflictCounting()

#min-conflict strategy to solve the problem
def search():
    while True:

        # pick random column
        while True:
            col = random.randint(0, 1000000) % (N-1)
            # except this one
            if col != active_col:
                if getHitsAtQueen(col) > 0:
                    break


        tMin = 10000


        tCells = []


        for row in range(N):

            if row != getQueenPos(col)[1]:

                if tMin >= board[col][row]:

                    if tMin == board[col][row]:
                        tCells.append(row)

                    else:

                        tMin = board[col][row]

                        tCells = []
                        tCells.append(row)

        if len(tCells) == 0:
            next

        # move queen to a tile with the minimum value of conflicts
        S[col] = random.choice(tCells)

        clear()

        conflictCounting()

        return col

def main():

    initialize()
    print("\n\nAFTER INIT: ")
    print_hits()
    print_queens()

    counter = 0

    while isFinalState() == False:
        active_col = search()
        counter += 1
        print("Queen moves: " + str(counter))
        if counter >= 500:
            print("Error.")
            break

    print('FINAL SOLUTION: ')
    print_hits()
    print_queens()

if __name__ == "__main__":
    main()