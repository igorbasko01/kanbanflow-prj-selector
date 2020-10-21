import logging

from .boards.boards import Boards

"""Main module."""


def start(board_token_path):
    logging.basicConfig(level=logging.INFO, format='%(asctime)s [%(name)s] %(levelname)s: %(message)s')
    log = logging.getLogger()
    log.info("Going to read the following boards file %s", board_token_path)
    boards = Boards(board_token_path).fetch()
    log.info(boards)
