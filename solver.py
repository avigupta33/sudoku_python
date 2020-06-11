import typing
from typing import Tuple

from board import Board

class Solver:
    def __init__(self):
        pass

    def solve(self, board: Board):
        pass

class DFS_Solver(Solver):
    def __init__(self):
        self.curr_row = 0
        self.curr_col = 0

    def getValue(self, board: Board) -> int:
        return board.data[ self.curr_row][self.curr_col]

    def setValue(self, board: Board, value: int) -> None:
        board.data[self.curr_row][self.curr_col] = value

    def validValue(self, board: Board, value: int):
        return board.isValid(self.curr_row, self.curr_col, value)

    def incrementValue(self, board: Board) -> bool:
        if self.getValue(board) + 1 > 9:
            print("cannot increment")
            return False
        print(f"Changing ({self.curr_row}, {self.curr_col}) from {self.getValue(board)} to {self.getValue(board)+1}")
        self.setValue(board, self.getValue(board) + 1)
        return True

    def getFirstBlank(self, board: Board) -> Tuple[int, int]:
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




    # def solve(self, board: Board):
    #     while self.goToNext(board):
    #         set_val = False
    #         for i in range(1,10):
    #             if self.validValue(board, i):
    #                 self.setValue(board, i)
    #                 set_val = True
    #                 print(f"Setting value at ({self.curr_row}, {self.curr_col}) to {i}")
    #                 break
    #
    #         if not set_val: #if we couldn't find a value to set
    #             print(f"Could not set ({self.curr_row}, {self.curr_col})")
    #             board.display()
    #             self.setValue(board, 0)
    #             self.goToPrev(board)
    #             while not self.incrementValue(board):
    #                 self.setValue(board, 0)
    #                 self.goToPrev(board)
    #
    #     print("Solve finished")
    #

    # def goToNext(self, board: Board) -> bool:
    #     while self.getValue(board)!=0:
    #         if self.curr_col == board.size-1:
    #             if self.curr_row == board.size-1:
    #                 print("done traversing")
    #                 return False
    #             self.curr_row+=1
    #             self.curr_col = 0
    #         else:
    #             self.curr_col+=1
    #     # print(f"Curr row: {self.curr_row} Curr col: {self.curr_col}")
    #     return True
    #
    # def goToPrev(self, board: Board) -> bool:
    #     print(f"goToPrev start: ({self.curr_row}, {self.curr_col})")
    #
    #     if self.curr_col == 0:
    #         if self.curr_row == 0:
    #             print("done traversing")
    #             return False
    #         self.curr_row-=1
    #         self.curr_col = board.size-1
    #     else:
    #         self.curr_col-=1
    #     print(f"goToPrev end: ({self.curr_row}, {self.curr_col})")
    #
    #     # print(f"Curr row: {self.curr_row} Curr col: {self.curr_col}")
    #     return True




