import typing
from board import Board

class Parser:
    def __init__(self):
        pass

    def parse(self, filename: str) -> Board:
        with open(filename) as fil:
            data = []
            line = fil.readline()
            while line:
                row = line.split()
                for i in range(len(row)):
                    row[i] = int(row[i])

                if len(row) != 0:
                    size = len(row)

                data.append(row)
                line = fil.readline()

            board = Board(data, size)

            return board