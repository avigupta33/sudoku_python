class Cage:
    def __init__(self, data, top_left, cage_size):
        self.data = data
        self.top_left = top_left
        self.cage_size = cage_size

    def display(self):
        print(self.top_left)
        for row in self.data:
            for val in row:
                print(val, end = " ")
            print()
        print()

    def verify(self):
        seen = set()
        for row in self.data:
            for val in row:
                if val not in seen:
                    seen.add(val)
                else:
                    return False

