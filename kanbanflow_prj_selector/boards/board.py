import requests
from ..constants import KFLOW_BASE_URL


class Board(object):

    def __init__(self, token):
        self.FULL_URL = f"{KFLOW_BASE_URL}/board"
        (self.id, self.name) = self.parse_board(self.fetch_board_json(token))
        self.tasks = []
        self.columns =[]
        self.swimlanes = []

    def fetch_board_json(self, token):
        return requests.get(f"{self.FULL_URL}?apiToken={token}").json()

    def parse_board(self, board_dict):
        return board_dict["_id"], board_dict['name']

