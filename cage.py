class Cage:
    def __init__(self, data):
        self.data = data

    def display(self):
        for row in self.data:
            for val in row:
                print(val, end = " ")
            print()

    def verify(self):
        seen = set()
        for row in self.data:
            for val in row:
                if val not in seen:
                    seen.add(val)
                else:
                    return False

