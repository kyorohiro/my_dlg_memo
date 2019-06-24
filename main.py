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
    @typechecked
    def __init__(self, row_size:int, col_size:int):
        self.row_size = row_size
        self.col_size = col_size
        self.cont = [None] * (row_size * col_size)

    def getState(self, row:int, col:int):
        return self.col_size * row + col

    def getStateFromValue(self, value:str):
        buffer:bytes = value.encode("utf-8")
        col = buffer[0] - 65
        row = buffer[1] - 48
        if(len(buffer)>=2):
            row = row * 10 + (buffer[1] - 48)
        return self.getState(row, col)




#print("\014")#os.system("clear")

@typechecked
def main(message:str):
    sys.stdout.write(message)
    sys.stdout.write("\26")#clear()
    sys.stdout.write(message)

if __name__ == "__main__":
    main("Hello World!!")
    pass

'''
import sys, time
for num, i in enumerate(range(100)):
    sys.stdout.write("\r%d" % num)
    sys.stdout.flush()
    time.sleep(0.01)
'''