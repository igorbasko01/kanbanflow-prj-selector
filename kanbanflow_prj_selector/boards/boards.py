import csv
from ..boards.board import Board


class Boards(object):

    def __init__(self, path):
        self.path = path
        self.tokens = None
        self.boards = None

    def fetch(self):
        self.tokens = self._read_board_tokens(self.path)
        self.boards = self._pull_boards(self.tokens)
        return self

    def _read_board_tokens(self, path):
        with open(path, 'rt') as f:
            tokens = [line["token"] for line in csv.DictReader(f, fieldnames=["board_name", "token"])]
            return tokens

    def _pull_boards(self, tokens):
        return [Board(token) for token in tokens]

    def __str__(self):
        return f"{{ File path: {self.path}. Tokens: {self.tokens}. Boards: {self.boards} }}"
