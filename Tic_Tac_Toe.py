#ON PART FIVE of coding spot tutorial


import pygame ,sys
import numpy as np

pygame.init()
WIDTH = 600
HEIGHT = 600
LINE_WIDTH = 10
#BOARD
B_ROW = 3
B_COL = 3
#RGB
BG_COLOUR = (48, 184, 177)
RED_COLOUR = (255,0,0)
LINE_COLOUR = (23,145,135)

CIRCLE_RADIUS = 60
CIRCLE_WIDTH = 15
CIRCLE_COLOUR = pygame.Color(221, 237, 237)
CROSS_WIDTH = 25
CROSS_COLOUR = pygame.Color(110, 122, 122)
SPACE = 55


screen = pygame.display.set_mode((WIDTH,HEIGHT))
pygame.display.set_caption('TIC TAC TOE')
screen.fill(BG_COLOUR)

#board
board = np.zeros((B_ROW, B_COL))

def mark_square(row, col, player):
    board[row][col] = player

def available_square(row,col):
    if board[row][col] == 0:
        return True
    else:
        False

def is_board_full():
    for row in range(B_ROW):
        for col in range(B_COL):
            if board[row][col] == 0:
                return False
    return True

def draw_fig():
    for row in range(B_ROW):
        for col in range(B_COL):
            if board[row][col]==1:
                pygame.draw.circle(screen, CIRCLE_COLOUR, (int(col*200+100),int(row*200+100)), CIRCLE_RADIUS, CIRCLE_WIDTH)
            elif board[row][col]==2:
                pygame.draw.line(screen, CROSS_COLOUR, (col*200 + SPACE,row*200+200 - SPACE),(col*200+200 - SPACE,row*200 + SPACE),CROSS_WIDTH)
                pygame.draw.line(screen, CROSS_COLOUR, (col*200 + SPACE,row* 200 + SPACE),(col*200+200 - SPACE, row*200+200 - SPACE),CROSS_WIDTH)


#lines
def draw_lines():
    #horizontal lines
    pygame.draw.line(screen, LINE_COLOUR, (0,200), (600,200), LINE_WIDTH)
    pygame.draw.line(screen, LINE_COLOUR, (0,400), (600,400), LINE_WIDTH)
    #vertical lines
    pygame.draw.line(screen, LINE_COLOUR, (200,0), (200,600), LINE_WIDTH)
    pygame.draw.line(screen, LINE_COLOUR, (400,0), (400,600), LINE_WIDTH)

draw_lines()
player = 1
game_over = False


def check_win(player):
    for col in range(B_COL):
        if board[0][col] == player and board[1][col] == player and board[2][col] == player:
            draw_vertical_win_line(col, player)
            return True

    for row in range(B_ROW):
        if board[0][row] == player and board[1][row] == player and board[2][row] == player:
            draw_horizontal_win_line(row, player)
            return True

    if board[2][0] == player and board[1][1] == player and board[0][2] == player:
        draw_asc_diagnol(player)
        return True

    if board[0][0] == player and board[1][1] == player and board[2][2] == player:
        draw_desc_diagnol(player)
        return True

    return False
    

def draw_vertical_win_line(col, player):
    posX = col*200 + 100
    if player == 1:
        colour = CIRCLE_COLOUR
    elif player ==2:
        colour = CROSS_COLOUR

    pygame.draw.line(screen, colour, (posX, 15), (posX, HEIGHT - 15),15)

def draw_horizontal_win_line(row, player):
    posY = row*200+100
    if player == 1:
        colour = CIRCLE_COLOUR
    elif player ==2:
        colour = CROSS_COLOUR

    pygame.draw.line(screen, colour, (15, posY), (WIDTH - 15, posY),15)

def draw_asc_diagnol(player):
    if player == 1:
        colour = CIRCLE_COLOUR
    elif player ==2:
        colour = CROSS_COLOUR

    pygame.draw.line(screen, colour, (15, HEIGHT -15), (WIDTH - 15, 15),15)




def draw_desc_diagnol(player):
    if player == 1:
        colour = CIRCLE_COLOUR
    elif player ==2:
        colour = CROSS_COLOUR

    pygame.draw.line(screen, colour, (15, 15), (WIDTH - 15, HEIGHT - 15 ),15)

def restart():
    screen.fill(BG_COLOUR)
    draw_lines()
    player = 1
    for row in range(B_ROW):
        for col in range(B_COL):
            board[row][col] = 0


#mainloop
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

        if event.type == pygame.MOUSEBUTTONDOWN and not game_over:
            mouseX = event.pos[0]#x
            mouseY = event.pos[1]#y
            clicked_row = int(mouseY // 200)
            clicked_col = int(mouseX // 200)

            if available_square(clicked_row, clicked_col):
                if player == 1:
                    mark_square(clicked_row, clicked_col, 1)
                    if check_win(player):
                        game_over = True
                    player = 2
                elif player == 2:
                    mark_square(clicked_row, clicked_col, 2)
                    if check_win(player):
                        game_over = True
                    player = 1
                draw_fig()
                # print(board)
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_r:
                restart()
                game_over = False

    pygame.display.update()           