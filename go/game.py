from go import Board,BoardState
from enum import Enum

class StoneState(Enum):
    WHITE = 1
    BLACK = 2
    NONE = 0

    def toBoardState(self):
        return BoardState.WHITE if self.value == StoneState.WHITE else BoardState.BLACK

class GameException(RuntimeError):
    pass

class Game:

    def __init__(self, size:int):
        self.board = Board(size,size)

    # (a,a)            (s,a)   
    #          (x,y)
    # (a,s)             (s,s)
    def putStone(self, x:int, y:int, stone:StoneState):
        if self.existsStone(x,y):
            raise GameException()

        self.board.setState(y,x, stone.toBoardState())
        pass

    def existsStone(self, x:int, y:int):
        return BoardState.NONE != self.board.getState(y,x)

