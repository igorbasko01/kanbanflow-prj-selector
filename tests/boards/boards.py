import unittest
import tempfile
from kanbanflow_prj_selector.boards.boards import Boards


class MyTestCase(unittest.TestCase):
    def test_read_tokens(self):
        with tempfile.NamedTemporaryFile("w+b") as f:
            f.write(b"test_board,test\n")
            f.write(b"test_board1,test1\n")
            f.seek(0)
            tokens = Boards(f.name)._read_board_tokens(f.name)
            self.assertListEqual(tokens, ["test", "test1"])


if __name__ == '__main__':
    unittest.main()
