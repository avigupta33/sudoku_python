from typing import Tuple

from board import Board

class Solver:
    def __init__(self):
        pass

    def solve(self, board: Board):
        pass

class DFS_Solver(Solver):
    def __init__(self) -> None:
        pass

    @staticmethod
    def getFirstBlank(board: Board) -> Tuple[int, int]:
        for i in range(board.size):
            for j in range(board.size):
                if board.data[i][j] == 0:
                    return i,j

    def solve(self, board: Board) -> bool:
        unassigned = self.getFirstBlank(board)
        if not unassigned:
            return True
        if board.verify():
            return True
        for num in range(1, 10):
            if board.isValid(unassigned[0], unassigned[1], num):
                board.setData(unassigned[0],unassigned[1], num)
                if self.solve(board):
                    return True
                board.setData(unassigned[0],unassigned[1], 0)



