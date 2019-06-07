import sys
from go import Board,BoardState

def main():
    while True:
        board:Board = Board(9,9)
        sys.stdout.flush()
        sys.stdout.write(str(board))
        sys.stdout.write("Input A1 - I9 or ! \r\n")
        input:str = sys.stdin.readline()
        if(0 <= input.find("!")):
            break
        else:
            
            pass
    pass

if __name__ == "__main__":
    main()

