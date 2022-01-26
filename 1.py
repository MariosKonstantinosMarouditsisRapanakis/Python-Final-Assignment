import random

def newGame():
    global board, rings, steps
    board = [ [ [], [], [] ], [ [], [], [] ], [ [], [], [] ] ]
    rings = ['small', 'medium', 'big']*9
    steps = 0

def placeRandomRing():
    ring = rings.pop(random.randrange(len(rings)))
    while(True):
        row = random.randrange(3)
        column = random.randrange(3)
        if(not(ring in board[row][column])):
            board[row][column].append(ring)
            # print(board[0])
            # print(board[1])
            # print(board[2])
            # print('------------')
            return not(checkEnd(ring, row, column))

def checkEnd(ring, row, column):
    #horizontal
    if((ring in board[row][0]) and (ring in board[row][1]) and (ring in board[row][2])):
        return True
    #vertical
    if((ring in board[0][column]) and (ring in board[1][column]) and (ring in board[2][column])):
        return True
    #check middle square for faster exits if not filled
    if(ring in board[1][1]):
        #diagonal 1
        if((ring in board[0][0]) and (ring in board[2][2])):
            return True
        #diagonal 2
        if((ring in board[0][2]) and (ring in board[2][0])):
            return True

sum = 0
for i in range(10000):
    newGame()
    while(placeRandomRing()):
        steps += 1
    #print(steps)
    sum += steps + 1
print(sum/10000)
