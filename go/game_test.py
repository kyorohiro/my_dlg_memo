import unittest
from go import Game,BoardState,StoneState,GameException


class GameTest(unittest.TestCase):

    def test_error_alreadt_exists_stone(self):
        game:Game = Game(9)
        game.putStone(1,1,StoneState.BLACK)
        state:BoardState = game.board.getState(1,1)
        self.assertEqual(state, BoardState.BLACK)
        self.assertEqual(game.existsStone(1,1), True)

        try:
            game.putStone(1,1,StoneState.BLACK)
            self.assertTrue(False)
        except GameException:# as e:
            self.assertTrue(True)

        

  #  def test_002(self):
  #      self.assertTrue(True)

if __name__ == "__main__":
    unittest.main()

