import requests
from ..constants import KFLOW_BASE_URL
from .column import Column
from .swimlane import Swimlane


class Board(object):

    def __init__(self, token):
        self.FULL_URL = f"{KFLOW_BASE_URL}/board"
        (self.id, self.name, self.columns, self.swimlanes) = self.parse_board(self.fetch_board_json(token))
        self.tasks = []

    def fetch_board_json(self, token):
        return requests.get(f"{self.FULL_URL}?apiToken={token}").json()

    def parse_board(self, board_dict):
        columns = [Column(col_dict) for col_dict in board_dict["columns"]]
        swimlanes = [Swimlane(lane_dict) for lane_dict in board_dict["swimlanes"]]
        return board_dict["_id"], board_dict['name'], columns, swimlanes

