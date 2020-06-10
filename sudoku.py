from board import Board
from parser import Parser


def verify(board):
    pass

if __name__ == "__main__":
    parser = Parser()
    board = parser.parse("puzzles/s01a.txt")
    print(board.verify())
    for cage in board.cages:
        cage.display()
    #board.display()