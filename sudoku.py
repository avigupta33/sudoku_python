from board import Board
from parser import Parser
from solver import DFS_Solver

if __name__ == "__main__":
    parser = Parser()
    board = parser.parse("puzzles/s01b.txt")
    dfs_solver = DFS_Solver()
    dfs_solver.solve(board)
    board.display()
    print(board.verify())

    # for cage in board.cages:
    #     cage.display()

    #board.display()