import unittest
from go import Board, BoardState

class TestBoard(unittest.TestCase):

    def test_Board_init_001(self):
        b:Board = Board(3,3)
        b.setState(1,1, BoardState.WHITE)
        print("\r\n"+str(b))
        self.assertTrue(True)

if __name__ == "__main__":
    unittest.main()