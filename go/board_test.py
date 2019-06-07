import unittest
from go import Board, BoardState, FormatException

class TestBoard(unittest.TestCase):

    def test_Board_init_001(self):
        b:Board = Board(3,3)
        b.setState(1,1, BoardState.WHITE)
        print("\r\n"+str(b))
        self.assertTrue(True)

    def test_Board_extractRowCol_001(self):
        (row,col) = Board.extractRowCol("A1")
        self.assertEqual(0,row)
        self.assertEqual(0,col)

        (row,col) = Board.extractRowCol("B3")
        self.assertEqual(1,row)
        self.assertEqual(2,col)

        (row,col) = Board.extractRowCol("Z99")
        self.assertEqual(25,row)
        self.assertEqual(98,col)

        try:
            (row,col) = Board.extractRowCol("")
            self.fail()
        except FormatException:
            pass

if __name__ == "__main__":
    unittest.main()