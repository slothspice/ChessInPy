import pygame
import chessBoard

pygame.init()
gameDisplay = pygame.display.set_mode((800, 800))
pygame.display.set_caption("PyChess")

clock = pygame.time.Clock()


firstBoard = chessBoard.Board()
firstBoard.createBoard()
firstBoard.printBoard()

print(firstBoard.gameTiles[1].pieceOnTile.calculateLegalMoves(firstBoard))


def createSqParams():

    allSqRanges = []
    xMin = 0
    xMax = 100
    yMin = 0
    yMax = 100
    for _ in range(8):
        for _ in range(8):
            allSqRanges.append([xMin, xMax, yMin, yMax])
            xMin += 100
            xMax += 100
        xMin = 0
        xMax = 100
        yMin += 100
        yMax += 100

    return allSqRanges

allSqParams = createSqParams()




allTiles = []
allPieces = []

def squares(x, y, w, h, color):
    pygame.draw.rect(gameDisplay, color, [x, y, w, h])
    allTiles.append([color, [x, y, w, h]])


def drawChessPieces():

    xpos = 0
    ypos = 0
    row = 0
    color = 0
    width = 100
    height = 100
    black = (66,134,244)
    white = (143,155,175)
    number = 0

    for _ in range(8):

        for _ in range(8):
            if color % 2 == 0:
                squares(xpos, ypos, width, height, white)

                if not firstBoard.gameTiles[number].pieceOnTile.toString() == "-":
                    img = pygame.image.load("./ChessArt/" + firstBoard.gameTiles[number].pieceOnTile.alliance[0].upper() + firstBoard.gameTiles[
                        number].pieceOnTile.toString().upper() + ".png")
                    img = pygame.transform.scale(img, (100, 100))
                    allPieces.append([img, [xpos, ypos], firstBoard.gameTiles[number].pieceOnTile])
                    #gameDisplay.blit(img, (xpos, ypos))

                xpos += 100
            else:

                squares(xpos, ypos, width, height, black)

                if not firstBoard.gameTiles[number].pieceOnTile.toString() == "-":
                    img = pygame.image.load("./ChessArt/" + firstBoard.gameTiles[number].pieceOnTile.alliance[0].upper() + firstBoard.gameTiles[
                        number].pieceOnTile.toString().upper() + ".png")
                    img = pygame.transform.scale(img, (100, 100))
                    allPieces.append([img, [xpos, ypos], firstBoard.gameTiles[number].pieceOnTile])
                    #gameDisplay.blit(img, (xpos, ypos))

                xpos += 100

            #print(firstBoard.gameTiles[number].pieceOnTile.toString())


            color += 1
            number += 1


        color += 1
        xpos = 0
        ypos += 100



drawChessPieces()



print(allTiles)
print(allPieces)

#kimg = pygame.image.load("./ChessArt/BK.png")

selectedImage = None

quitGame = False

mx, my = pygame.mouse.get_pos()
prevx, prevy = [0,0]

while not quitGame:

    #mx,my = pygame.mouse.get_pos()
    #print(mx, my)

    for event in pygame.event.get():

        if event.type == pygame.QUIT:
            quitGame = True
            pygame.quit()
            quit()

        if event.type == pygame.MOUSEBUTTONDOWN:

            if selectedImage == None:
                mx, my = pygame.mouse.get_pos()
                for piece in range(len(allPieces)):
                    if allPieces[piece][1][0] < mx < allPieces[piece][1][0]+100:
                        if allPieces[piece][1][1] < my < allPieces[piece][1][1] + 100:
                            selectedImage = piece
                            prevx = allPieces[piece][1][0]
                            prevy = allPieces[piece][1][1]

        if event.type == pygame.MOUSEMOTION and not selectedImage == None:

            mx, my = pygame.mouse.get_pos()
            allPieces[selectedImage][1][0] = mx-50
            allPieces[selectedImage][1][1] = my-50


            #selectedImage = None
            #print("hi")

        if event.type == pygame.MOUSEBUTTONUP:

            try:
                pieceMoves = allPieces[selectedImage][2].calculateLegalMoves(firstBoard)
                print(pieceMoves)


                legal = False
                theMove = 0
                for moveDes in pieceMoves:
                    if allSqParams[moveDes][0] < allPieces[selectedImage][1][0]+50 < allSqParams[moveDes][1]:
                        if allSqParams[moveDes][2] < allPieces[selectedImage][1][1]+50 < allSqParams[moveDes][3]:
                            legal = True
                            theMove = moveDes

                if legal == False:
                    allPieces[selectedImage][1][0] = prevx
                    allPieces[selectedImage][1][1] = prevy
                else:
                    allPieces[selectedImage][1][0] = allSqParams[theMove][0]
                    allPieces[selectedImage][1][1] = allSqParams[theMove][2]
            except:
                pass

            prevy = 0
            prevx = 0
            selectedImage = None





        #print(event)



    gameDisplay.fill((255, 255, 255))

    for info in allTiles:
        pygame.draw.rect(gameDisplay, info[0], info[1])

    for img in allPieces:
        gameDisplay.blit(img[0], img[1])


    pygame.display.update()
    clock.tick(10)

