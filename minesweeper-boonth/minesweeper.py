"""
the minesweeper kata

"""

import numpy
import sys

class MineField:
    """
    A minesweeper field full of mines and counts of how many mines are
    adjacent to a location.
    
    """

    # value of location when it holds a mine
    mine = -1

    def __init__(self, nrows, ncols):
        self.nrows = nrows
        self.ncols = ncols

        # create a representation of the field as an array of ints,
        # where locations that have a mine have value of -1, and all
        # other locations have the minesweeper value
        # array index is [row][col]
        self.field = numpy.zeros((nrows, ncols), dtype='int')

    def addMine(self, row, col):
        """Add a mine at the given location"""

        # already a mine there, nothing to do
        if self.field[row][col] == MineField.mine:
            return

        self.field[row][col] = MineField.mine

        # increment the counters of all neighboring cells.
        # iterate over all possible displacments in each dimension, and add
        # displacements to make new location. if it is a valid location and no
        # mine is already present, increment counter.
        displacement = [-1, 0, 1]
        for i in displacement:
            for j in displacement:
                row2 = row + i
                col2 = col + j
                if row2 >= 0 and row2 < self.nrows:
                    if col2 >= 0 and col2 < self.ncols:
                        if self.field[row2][col2] != MineField.mine:
                            self.field[row2][col2] += 1

    def printField(self):
        """
        Print out the field. At each location, prints the number of mines
        neighboring it. If a location has a mine, a '*' is printed instead.
        
        """
        
        for row in range(self.nrows):
            s = ''    # string representing the row
            for col in range(self.ncols):
                if self.field[row][col] == MineField.mine:
                    s += '*'
                else:
                    s += str(self.field[row][col])
                s += ' '

            # make sure to remove the rightmost space before printing
            print s.rstrip()

def main(input):
    """Given a file with input fields, output the fields with numbers"""

    def getRowsCols(line):
        """Given a line, return the number of rows and columns it specifies"""
        return [int(x) for x in line.split()]

    # list of fields read from input file
    fields = []

    # read input file and create fields
    fin = open(input, 'r')
    nrows, ncols = getRowsCols(fin.readline())
    while nrows > 0 and ncols > 0:
        field = MineField(nrows, ncols)
        for row in range(nrows):
            line = fin.readline()
            line2 = line.split()
            for col, token in enumerate(line2):
                if token == '*':
                    # add a mine to the field
                    field.addMine(row, col)
                elif token != '.':
                    # error, no other characters are allowed
                    print 'illegal character at row: %i column: %i' % (row, col)

        fields.append(field)
        nrows, ncols = getRowsCols(fin.readline())
    fin.close()

    # print out all fields
    for i, field in enumerate(fields):
        print 'Field #%i:' % (i+1)
        field.printField()
        print ''


if __name__ == '__main__':
    if len(sys.argv) < 2:
        print 'usage: <input>'
    else:
        main(sys.argv[1])
