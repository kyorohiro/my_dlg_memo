import sys
from go import Board,BoardState

def main():
    index:int = 0
    board:Board = Board(9,9)
    while True:
        sys.stdout.flush()
        sys.stdout.write(str(board))
        sys.stdout.write("Input A1 - I9 or ! \r\n")
        input:str = sys.stdin.readline()
        if(0 <= input.find("!")):
            break
        else:
            extracted = Board.extractRowCol(input)
            row:int = extracted[0]
            col:int = extracted[1]
            if (0<= row and row <=9) and (0<= col and col <=9):
              board.setState(row, col, BoardState.BLACK if index%2==0 else BoardState.WHITE)
              index+=1
    pass


if __name__ == "__main__":
    main()
