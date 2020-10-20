import csv


class Boards(object):

    def __init__(self, path):
        self.path = path
        self.tokens = None
        self.boards = None

    def fetch(self):
        self.tokens = self._read_board_tokens(self.path)
        self.boards = self._pull_boards(self.tokens)

    def _read_board_tokens(self, path):
        with open(path, 'rt') as f:
            tokens = [line["token"] for line in csv.DictReader(f, fieldnames=["board_name", "token"])]
            return tokens

    def _pull_boards(self, tokens):
        raise NotImplementedError

    def _pull_board(self, board_token):
        raise NotImplementedError
