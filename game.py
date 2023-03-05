import turtle

MARGIN = 50 
BOARD_WIDTH = 600
DIMENSION = 3
CELL_SIZE = BOARD_WIDTH / DIMENSION
DELTA = CELL_SIZE / 8
data = []
for _ in range (DIMENSION):
    temp = []
    for _ in range (DIMENSION):
        temp.append(0)
    data.append(temp)

#turtle.onscreenclick

def checkAnyWin(ln):
    if sum(ln) == DIMENSION:
        return 'x'
    elif sum(ln) == -DIMENSION:
        return'o'
    
    return ''

def checkWin():
    # check cols
    for i in range(DIMENSION):
        ln = data[i]
        w = checkAnyWin(ln)
        if w != '':
            return w

    # check rows
    for i in range(DIMENSION):
        ln = []
        for j in range(DIMENSION):
            ln.append(data[j][i])
            
        w = checkAnyWin(ln)
        if w != '':
            return w
    
    # check main diagnal
    ln = []
    for i in range(DIMENSION):
        for j in range(DIMENSION):
            if i == j:
                ln.append(data[i][j])

    w = checkAnyWin(ln)
    if w !='':
        return w

    # check auti diagnal
    ln = []
    for i in range(DIMENSION):
        for j in range(DIMENSION):
            if i + j == DIMENSION - 1:
                ln.append(data[i][j])
    
    w = checkAnyWin(ln)
    if w != '':
        return w

    for i in range(DIMENSION):
        for j in range(DIMENSION):
            if data[i][j] == 0:
                return ''

    return '-'



def drawLine(x1, y1, x2, y2, color = '#cb997e'):
    t = turtle.Turtle()
    t.hideturtle()
    t.speed(0)
    t.penup()
    t.goto(x1,y1)
    t.pendown()
    t.goto(x2,y2)


def drawXPiece(x, y) :
    t = turtle.Turtle()
    t.hideturtle()
    t.speed(0)
    t.color('#cb997e')
    t.width(DELTA)

    t.penup()
    t.goto(x-CELL_SIZE/2 + DELTA, y - CELL_SIZE/2 + DELTA)
    t.pendown()
    t.goto(x+CELL_SIZE/2 - DELTA, y + CELL_SIZE/2 - DELTA)

    t.penup()
    t.goto(x+CELL_SIZE/2 - DELTA, y - CELL_SIZE/2 + DELTA)
    t.pendown()
    t.goto(x-CELL_SIZE/2 + DELTA, y + CELL_SIZE/2 - DELTA)

def drawOPieceV(x,y) :
    t = turtle.Turtle()
    t.hideturtle()
    t.speed(0)
    t.color('#ddbea9')
    t.width(DELTA)
    t.penup()
    t.goto(x,y)
    t.pendown()
    t.dot(CELL_SIZE-DELTA*2)
    t.color('#ffe8d6')
    t.dot(CELL_SIZE-DELTA*4)

def dropXPiece(col, row):
    x = -BOARD_WIDTH / 2 + col * CELL_SIZE + CELL_SIZE / 2
    y = -BOARD_WIDTH / 2 + row * CELL_SIZE + CELL_SIZE / 2
    drawXPiece(x, y)
    data[col][row] = 1

def dropOPiece(col, row):
    x = -BOARD_WIDTH / 2 + col * CELL_SIZE + CELL_SIZE / 2
    y = -BOARD_WIDTH / 2 + row * CELL_SIZE + CELL_SIZE / 2
    drawOPieceV(x, y)
    data[col][row] = -1

def declareWinner(w):
    t = turtle.Turtle()
    t.hideturtle()
    t.penup()
    t.goto(-BOARD_WIDTH / 2, -BOARD_WIDTH / 2 - 50)
    statement = w + ' wins :)' 
    if w == 'x' :
        t.color('#cb997e')
    elif w == 'o' :
        t.color('#ddbea9')
    else:
        t.color('#8b8d70')
        statement = 'tie :('
    t.write(statement, font = ('Courier', 50, 'normal', 'bold'))

def handleClick(x, y):
    # if click is outside the board, ignore it
    if x < -BOARD_WIDTH / 2 or x > BOARD_WIDTH / 2 or y <-BOARD_WIDTH / 2 or y > BOARD_WIDTH / 2:
        return
    global cur_player
    col, row = xy2ColRow(x, y)
    if data[col][row] != 0: # do nothing if there's already a piece at col, row
        return

    if cur_player == 'x':
        dropXPiece(col, row)
        cur_player = 'o'
    else:
        dropOPiece(col, row)
        cur_player = 'x'
    
    w = checkWin()
    if w == '':
        return
    declareWinner(w)
    answer = turtle.textinput('Play once more?', 'Does thou desire to play once more? (yes/no)')
    if answer == 'y':
        reset()

def reset():
    global data
    data = ([0 for i in range(DIMENSION)] for j in range(DIMENSION))
    turtle.clearscreen()
    drawBoard()
    playGame()

def playGame():
    sn = turtle.Screen()
    sn.onclick(handleClick)

cur_player = 'x'

def xy2ColRow(x, y):
    startX = -BOARD_WIDTH / 2
    startY = -BOARD_WIDTH / 2
    col = int((x - startX) / CELL_SIZE)
    col = int((x + BOARD_WIDTH / 2) / CELL_SIZE)
    row = int((y + BOARD_WIDTH / 2) / CELL_SIZE)
    return col, row

def drawBoard():
    turtle.setup(BOARD_WIDTH + MARGIN * 2, BOARD_WIDTH + MARGIN * 2)
    startX = -BOARD_WIDTH / 2
    startY = -BOARD_WIDTH / 2

    for i in range(DIMENSION + 1) :
        x1 = startX
        y1 = startY + i * BOARD_WIDTH / DIMENSION
        x2 = startX + BOARD_WIDTH
        y2 = startY + i * BOARD_WIDTH / DIMENSION   
        drawLine(x1,y1,x2,y2)

    for i in range(DIMENSION + 1):
        x1 = startX + i * BOARD_WIDTH / DIMENSION
        y1 = startY
        x2 = startX + i * BOARD_WIDTH / DIMENSION
        y2 = startY + BOARD_WIDTH
        drawLine(x1,y1,x2,y2)

 


#main logic
drawBoard()
playGame()
turtle.done()

#O O
# L
# n