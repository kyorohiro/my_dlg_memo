
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

    @classmethod
    def extractRowCol(self, value:str)->tuple:
        buffer:bytes = value.encode("utf-8")
        col = buffer[0] - 65
        row = buffer[1] - 48
        if(len(buffer)>=2):
            row = row * 10 + (buffer[1] - 48)
        return (row, col)

    def __str__(self):
        buffer:list = []
        switcher = { 
            BoardState.NONE: "-",
            BoardState.BLACK:"b",
            BoardState.WHITE:"w",
        }

        for y in range(0,self.col_size):
            for x in range(0,self.row_size):
                if x > 0:
                    buffer.append(" ")
                n = self.getState(x,y)
                buffer.append(switcher.get(n, "?"))
            buffer.append('\r\n')
        return "".join(buffer)


