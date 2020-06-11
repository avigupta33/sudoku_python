class Cage:
    def __init__(self, data, top_left, cage_size) -> None:
        self.data = data
        self.top_left = top_left
        self.cage_size = cage_size

    def display(self) -> None:
        print(self.top_left)
        for row in self.data:
            for val in row:
                print(val, end = " ")
            print()
        print()

    def verify(self) -> bool:
        seen = set()
        for row in self.data:
            for val in row:
                if val not in seen:
                    seen.add(val)
                else:
                    return False
        return True

    def verifyValue(self, value: int) -> bool:
        for row in self.data:
            for val in row:
                if val == value:
                    return False
        return True

    def isInCage(self, row_i: int, col_i: int) -> bool:
        if self.top_left[0]<=row_i<self.top_left[0]+self.cage_size:
            if self.top_left[1]<=col_i<self.top_left[1]+self.cage_size:
                return True
        return False

    def setFromAbsolute(self, row_i: int, col_i: int, val: int) -> None:
        self.data[row_i - self.top_left[0]][col_i - self.top_left[1]] = val

