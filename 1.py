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
    #bigger to smaller
    if('medium' in board[row][1]):
        if((('small' in board[row][0]) and ('big' in board[row][2])) or (('big' in board[row][0]) and ('small' in board[row][2]))):
            return True
    if('medium' in board[1][column]):
        if((('small' in board[0][column]) and ('big' in board[2][column])) or (('big' in board[0][column]) and ('small' in board[2][column]))):
            return True
    #diagonals
    if('medium' in board[1][1]):
        #diagonal 1
        if((('big' in board[0][0]) and ('small' in board[2][2])) or (('small' in board[0][0]) and ('big' in board[2][2]))):
            return True
        #diagonal 2
        if((('small' in board[0][2]) and ('big' in board[2][0])) or (('big' in board[0][2]) and ('small' in board[2][0]))):
            return True
    return False

sum = 0
for i in range(100):
    newGame()
    while(placeRandomRing()):
        steps += 1
    #print(steps)
    sum += steps + 1
print(sum/100)
