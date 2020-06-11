from board import Board
from parser import Parser
from solver import DFS_Solver

if __name__ == "__main__":
    parser = Parser()
    dfs_solver = DFS_Solver()

    board = parser.parse("puzzles/s01b.txt")
    board.display()
    dfs_solver.solve(board)
    board.display()
    print(board.verify())

