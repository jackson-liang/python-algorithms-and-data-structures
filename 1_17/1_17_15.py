# Exercise 15 from
# https://interactivepython.org/runestone/static/pythonds/Introduction/ProgrammingExercises.html

class Block:
    def __init__(self):
        self.boxes = []
        for i in range(3):
            row = []
            for j in range(3):
                row.append(" ")
            self.boxes.append(row)

    def add_number(self, num, r, c):
        self.boxes[r][c] = num

    def __str__(self):
        printed_block = ""
        for i in range(3):
            for j in range(3):
                printed_block += str(self.boxes[i][j]) + " | "
            printed_block = printed_block + "\n"
            printed_block = printed_block + "-----------" + "\n"
        return printed_block


class Grid(Block):
    def __init__(self):
        self.boxes = []
        for i in range(9):
            row = []
            for j in range(9):
                row.append(" ")
            self.boxes.append(row)

    def __str__(self):
        printed_block = ""
        for i in range(9):
            for j in range(9):
                printed_block += str(self.boxes[i][j]) + " | "
            printed_block = printed_block + "\n"
            printed_block = printed_block + "-----------------------------------" + "\n"
        return printed_block


myGrid = Grid()
myGrid.add_number(5, 0, 0)
myGrid.add_number(3, 2, 2)
print(myGrid)
