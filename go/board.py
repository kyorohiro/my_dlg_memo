
from typeguard import typechecked
from enum import Enum
import os
import sys

clear = lambda: sys.stdout.flush()

# [memo]
#        1Col列(A) 2Col列(B) 3Col列(C)
# 1Row行
# 2Row行

class BoardState(Enum):
    WHITE = 1
    BLACK = 2
    NONE = 0

class FormatException(Exception):
    pass

class Board:

    def __init__(self, row_size:int, col_size:int):
        self.row_size = row_size
        self.col_size = col_size
        self.cont = [BoardState.NONE] * (row_size * col_size)
        self.index = 0

    def calcIndex(self, row:int, col:int)->int:
        return self.col_size * row + col

    def getState(self, row:int, col:int)->BoardState:
        return self.cont[self.calcIndex(row,col)]

    def setState(self, row:int, col:int, v:BoardState):
        self.cont[self.calcIndex(row,col)] = v

    def checkSettable(self, row:int, col:int):
        return self.getState(row, col) == BoardState.NONE

    def __str__(self):
        buffer:list = []
        switcher = { 
            BoardState.NONE: "-",
            BoardState.BLACK:"b",
            BoardState.WHITE:"w",
        }

        for y in reversed(range(0,self.col_size)):
            for x in range(0,self.row_size):
                if x == 0:
                    buffer.append(str(y+1).zfill(2)+" ")
                elif x > 0:
                    buffer.append(" ")
                n = self.getState(x,y)
                buffer.append(switcher.get(n, "?"))
            buffer.append('\r\n')
        
        buffer.append("   ")
        for x in range(0,self.row_size):
            if x > 0:
                buffer.append(" ")
            n = self.getState(x,y)
            buffer.append(chr(x+ord('A')))
        buffer.append('\r\n')
        return "".join(buffer)


    @classmethod
    def extractRowCol(self, value:str)->tuple:
        if  not (len(value) >= 2):
            raise FormatException()
        buffer:bytes = value.strip().encode("utf-8")
        row= buffer[0] - ord('A')
        col = buffer[1] - ord('0') #chr()
        if(len(buffer)>2):
            col = col * 10 + (buffer[2] - 48)

        # go start from 1 and A:
        return (row, col-1)
