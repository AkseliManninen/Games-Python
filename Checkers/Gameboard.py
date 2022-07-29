# Notes
# Imports

import pygame as pg
pg.init()

# Creating a screen and a surface
width = 640
height = 640

screen = pg.display.set_mode((width, height))
surface = pg.Surface((screen.get_size()))

rects = []


# Setting colors
fillColor         = (255, 255, 255)
gridColor         = (0, 0, 0)


# Drawing a black square to every other slot
gridSize = 8
def drawGrid():
    for i in range(gridSize):
        for j in range(gridSize):
                if (i % 2 == 0 and j % 2 == 0) or (i % 2 == 1 and j % 2 == 1):
                    rect = pg.Rect((width / gridSize * i), ((height - (height - width)) / gridSize * j), width / gridSize, (height - (height - width)) / gridSize)
                    rects.append(rect)
                    pg.draw.rect(surface, gridColor, rect)

# Drawing surface to the screen
def draw(surface):
    screen.blit(surface, (0, 0))
    pg.display.update()


# Keeping track of locations of the blue pieces

# Initial positions
bluePiecesLocations = [(1,1), (1, 3), (2, 2), (3, 1), (3, 3), (4, 2), (5, 1), (5, 3), (6, 2), (7, 1), (7, 3), (8, 2)]
greenPieceLocations = [(1, 7), (2, 6), (2, 8), (3, 7), (4, 6), (4, 8), (5, 7), (6, 6), (6, 8), (7, 7), (8, 6), (8, 8)]

# Drawing the pieces to the board

squareCenter = width / gridSize / 2
pieceSize = width / gridSize / 2 * 0.8

def drawPieces():
    for i in bluePiecesLocations:
        pg.draw.circle(surface, (0,0,255), [(i[0] - 1) * 80 + squareCenter, (i[1] - 1) * 80 + squareCenter], pieceSize)
    
    for i in greenPieceLocations:
        pg.draw.circle(surface, (0,255,0), [(i[0] - 1) * 80 + squareCenter, (i[1] - 1) * 80 + squareCenter], pieceSize)
        

def highlightSquare():
    rect = pg.Rect((width / gridSize * 1), ((height - (height - width)) / gridSize * 1), width / gridSize, (height - (height - width)) / gridSize)
    pg.draw.rect(surface, (250, 250, 210), rect)

def removeHighlight():
    rect = pg.Rect((width / gridSize * 1), ((height - (height - width)) / gridSize * 1), width / gridSize, (height - (height - width)) / gridSize)
    pg.draw.rect(surface, (0, 0, 0), rect)

def main():

    surface.fill(fillColor)
    drawGrid()

    running = True
    click = False

    #main loop
    while running:
        # The surface is constantly drawn
        draw(surface)
        drawPieces()
            
        for event in pg.event.get():
            if event.type == pg.MOUSEBUTTONDOWN:
                highlightSquare()
            elif event.type == pg.MOUSEBUTTONUP:
                removeHighlight()
            elif event.type == pg.QUIT:
                running = False

main()

