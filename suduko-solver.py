from itertools import product

class Board:
    def __init__(self):
        self.grid = []
        for i in range(9):
            self.grid.append([0,0,0,0,0,0,0,0,0])
     
    def load(self,filename):
        filedata = open(filename,"r").read()
        for i in range(9):
            for j in range(9):
                index = i*9 + j
                self.grid[i][j] = filedata[i*9 + j]

    def loadFromStr(self,string):
        for i in range(9):
            for j in range(9):
                index = i*9 + j
                self.grid[i][j] = string[i*9 + j]

    def getBox(self,x,y):
        box = []
        for row in range(3):
            box.append(self.grid[y*3 + row][3*x:3*x+3])
        return box

    def missingNumbers(self,box):
        presentNumbers = []
        for row in box:
            for column in row:
                if(column != 0):
                    presentNumbers.append(column)
        absentNumbers = []
        for i in range(1,10):
            if i not in presentNumbers: absentNumbers.append(i)
        return absentNumbers

    def boxContains(self,box,n):
        for row in box:
            #print(row)
            if(str(n) in row):
                return True
        return False

    def countEmptyCells(self,box):
        emptyCellCount = 0
        
        for row in box:
            emptyCellCount += row.count("0")

        return emptyCellCount 

    
    def boxFull(self,box):
        return self.countEmptyCells(box) == 0

    def findGridPosOfLastEmptyCell(self,boxX,boxY):
        for row in range(3):
            for column in range(3):
                x = boxX*3 + column
                y = boxY*3 + row
                if(self.grid[y][x] == "0"):
                    return [x , y]
    def areThereVisibleAlignments(self, boxGridX, boxGridY, n):
        for x in range(9):
            #TODO skip checking elements of own box for optimization
            if(x != boxGridX):
                if(self.grid[boxGridY][x] == str(n)):
                    return True
        for y in range(9):
            #TODO skip checking elements of own box for optimization
            if(y != boxGridY):
                if(self.grid[y][boxGridX] == str(n)):
                    return True
        return False
            
    def tryOnlyOneNotAlignedThing(self,boxY, boxX, n):
        thereIsOneCandidate = False
        candidatePos = []
        for row in range(3):
            for column in range(3):
                x = boxX*3 + column
                y = boxY*3 + row
                if(self.grid[y][x] == "0"):
                    itCanFitHere = not self.areThereVisibleAlignments(x,y,n)
                    if(itCanFitHere):
                        if(thereIsOneCandidate):
                            return False
                        thereIsOneCandidate = True
                        candidatePos = [x,y]

        if(thereIsOneCandidate):
            self.setGridCell(candidatePos[0],candidatePos[1],n,"try onlt not aligned")
            return True
        return False
                                                       
    def setGridCell(self,cellX,cellY,n,method):
        self.grid[cellY][cellX] = n
        print("Found cell at ",cellX,cellY," - ",n," by",method)
        #self.print()

    def solve(self):
        solved = False
        while(not solved):
            solved = True    
            for  boxY, boxX in product(range(3), range(3)):
                box = self.getBox(boxX,boxY)
                for n in range(1,10):
                    n = str(n)
                    if(not self.boxFull(box)):
                       solved = False
                       
                    if(not self.boxContains(box,n)):
                       solved = False
                       self.tryOnlyOneNotAlignedThing(boxY, boxX, n)
                    
                    if(self.countEmptyCells(box) == 1):
                        cellPosOnGrid = self.findGridPosOfLastEmptyCell(boxX,boxY)
                        cellX = cellPosOnGrid[0]
                        cellY = cellPosOnGrid[1]
                        self.setGridCell(cellX,cellY,n,"LAST ONE")
                        break
                    
                    
                            
        
    def printArray2d(self,array):
        for row in array:
            line = ""
            for column in row:
                line+=str(column)+" "
            print(line)

    def print(self):
        self.printArray2d(self.grid)
        print("========================")
    

#b = Board()
#b.load("b2" )
#b.print()
#b.solve()

#b.getBox(0,1)
#print(b.findGridPosOfLastEmptyCell(0,2))
#print("========================")
#b.print()
#print(b.areThereVisibleAlignments(2, 0, 1))


#lines of 81 numbers, 0s mean blank cells
data = open("s2","r").read().split("\n")
b = Board()
for i in range(23,len(data)):
    sudoku = data[i]
    b.loadFromStr(sudoku)
    b.print()
    b.solve()
    b.print()
