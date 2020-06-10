from board import Board
from parser import Parser
from solver import DFS_Solver


def verify(board):
    pass

if __name__ == "__main__":
    parser = Parser()
    board = parser.parse("puzzles/s01b.txt")
    dfs_solver = DFS_Solver()
    print(board.verify())

    dfs_solver.solve(board)
    # for cage in board.cages:
    #     cage.display()

    #board.display()