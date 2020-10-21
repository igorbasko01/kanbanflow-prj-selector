import requests
import logging

from ..constants import KFLOW_BASE_URL
from .column import Column
from .swimlane import Swimlane


class Board(object):

    def __init__(self, token):
        self.log = logging.getLogger()
        self.FULL_URL = f"{KFLOW_BASE_URL}board"
        (self.id, self.name, self.columns, self.swimlanes) = self.parse_board(self.fetch_board_json(token))
        self.tasks = []

    def fetch_board_json(self, token):
        self.log.info("Pulling token: %s", token)
        resp = requests.get(f"{self.FULL_URL}?apiToken={token}")
        self.log.info("Status code: %s", resp.status_code)
        return resp.json()

    def parse_board(self, board_dict):
        columns = [Column(col_dict) for col_dict in board_dict["columns"]]
        swimlanes = [Swimlane(lane_dict) for lane_dict in board_dict["swimlanes"]]
        return board_dict["_id"], board_dict['name'], columns, swimlanes

    def __str__(self):
        return f"{{ Id: {self.id}. Name: {self.name}. Columns: {self.columns}. Swimlanes: {self.swimlanes}. Tasks: {self.tasks} }}"

    def __repr__(self):
        return str(self)

