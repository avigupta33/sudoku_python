import typing
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

    def incrementValue(self, board: Board) -> None:
        self.setValue(board, self.getValue(board) + 1)


    def solve(self, board: Board):
        while self.goToNext() is not None:
            set_val = False
            for i in range(1,10):
                if self.validValue(i):
                    self.setValue(i)
                    set_val = True
            if not set_val:
                self.goToPrev()
                self.incrementValue()



    def goToNext(self, board: Board) -> None:
        while self.getValue()!=0:
            if self.curr_col == board.size-1:
                if self.curr_row == board.size-1:
                    print("done traversing")
                    return None
                self.curr_row+=1
                self.curr_col = 0
            self.curr_col+=1

    def goToPrev(self, board: Board) -> None:
        while self.getValue()!=0:
            if self.curr_col == 0:
                if self.curr_row == 0:
                    print("done traversing")
                    return None
                self.curr_row-=1
                self.curr_col = board.size-1
            self.curr_col-=1




