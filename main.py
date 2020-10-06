import pygame
from checkers_game.constants import WIDTH, HEIGHT, SQUARE_SIZE, RED
from checkers_game.board import Board
from checkers_game.game import Game

FPS = 60
WIN = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Checkers")

def get_row_col(pos):
    x, y = pos
    row = y // SQUARE_SIZE
    col = x // SQUARE_SIZE
    return row, col

def main():

    run = True
    clock = pygame.time.Clock()
    game = Game(WIN)

    #piece = board.get_piece(0, 1)
    #board.move(4, 3, piece)

    while run:
        clock.tick(FPS)

        if game.winner() != None:
            print(game.winner())
            break
        
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
            if event.type == pygame.MOUSEBUTTONDOWN:
                row, col = get_row_col(pygame.mouse.get_pos())
                game.select(row, col)
        
        game.game_update()
        
    pygame.quit()

main()