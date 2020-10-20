import csv


class Boards(object):

    def __init__(self, path):
        tokens = self._read_boards_list(path)
        boards = self._pull_boards(tokens)

    def _read_boards_list(self, path):
        with open(path, 'r') as f:
            return csv.DictReader(f)

    def _pull_boards(self, tokens):
        raise NotImplementedError

    def _pull_board(self, board_token):
        raise NotImplementedError
