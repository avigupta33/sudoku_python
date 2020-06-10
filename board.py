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
        for x in range(0, cage_size):
            for y in range(0, cage_size):
                cage = Cage(self.data[x:x+cage_size][y:y+cage_size])
                cages.append(cage)

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




