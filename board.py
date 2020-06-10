from typing import List
from cage import Cage

class Board:
    def __init__(self, data, size):
        self.data = data
        self.size = size
        self.cage_size = int(size**0.5)
        self.cages = self.splitIntoCages()

    def splitIntoCages(self) -> List[List[int]]:
        cages = []
        cage_size = int(self.size**0.5)
        for i in range(0, cage_size):
            for j in range(0, cage_size):
                cage = []
                rows = self.data[i*cage_size:(i+1)*cage_size]
                for row in rows:
                    cage.append(row[j*cage_size:(j+1)*cage_size])
                cages.append(Cage(cage, (i*cage_size,j*cage_size), cage_size))

        return cages

    def display(self) -> None:
        for i in range(0, self.size):
            if i % self.cage_size == 0:
                print("-" * 25)
            for j in range(0, self.size):
                if j % self.cage_size == 0:
                    print("|", end=" ")
                print(self.data[i][j], end=" ")

            print("|")
        print("-" * 25)

    def verify(self) -> bool:
        for row in self.data:
            if len(set(row)) != len(row):
                return False

        for col_ind in range(self.size):
            if len(set(self.data[:][col_ind])) != len(self.data[:][col_ind]):
                return False

        for cage in self.cages:
            if not cage.verify():
                return False

        return True

    def isValid(self, row_i: int, col_i: int, value: int) -> bool:
        if row_i < 0 or col_i <0 or row_i >= self.size or col_i >= self.size:
            return False

        if value in self.data[row_i]:
            return False

        for i in range(0, self.size):
            if self.data[i][col_i] == value:
                return False

        curr_cage = None
        for cage in self.cages:
            if cage.isInCage(row_i, col_i):
                curr_cage = cage
                break

        if curr_cage is None:
            print("Error in isValid -- curr_cage")
            return False

        if not curr_cage.verifyValue(row_i, col_i, value):
            return False

        return True






