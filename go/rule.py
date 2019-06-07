from go import Board, BoardState

class Rule:
    #
    def check(self, board:Board, row:int, col:int):
        pass

    #
    def checkSettable(self, board:Board, row:int, col:int):
        return board.getState(row, col) == BoardState.NONE

  

