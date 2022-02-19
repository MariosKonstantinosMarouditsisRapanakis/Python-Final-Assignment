import random

def newGame():
    #generate/reset a board, a pool of rings and the step counter
    global board, rings, steps
    board = [ [ [], [], [] ], [ [], [], [] ], [ [], [], [] ] ]
    rings = ['small', 'medium', 'big']*9
    steps = 0

def placeRandomRing():
    #get a random ring out of the pool
    ring = rings.pop(random.randrange(len(rings)))
    while(True):
        #get random position
        row = random.randrange(3)
        column = random.randrange(3)
        #check if the ring can be put there
        if(not(ring in board[row][column])):
            board[row][column].append(ring)
            return not(checkEnd(ring, row, column))

def checkEnd(ring, row, column):
    #check regarding same sized rings
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
    #check for different sized rings (we always check if the medium size is placed correctly first, for some small optimizarion)
    #horizontal
    if('medium' in board[row][1]):
        if((('small' in board[row][0]) and ('big' in board[row][2])) or (('big' in board[row][0]) and ('small' in board[row][2]))):
            return True
    #vertical
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
    #add 1 step, since the winning one doesn't register in the while loop. (can be optimized by initiating steps as 1 in the newGame() but it might have been confusing to the reader)
    sum += steps + 1
print(sum/100)
