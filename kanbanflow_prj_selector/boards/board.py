import requests
import logging

from ..constants import KFLOW_BASE_URL
from .column import Column
from .swimlane import Swimlane
from .task import Task


class Board(object):
    def __init__(self, token):
        self.log = logging.getLogger()
        self.FULL_BOARD_URL = f"{KFLOW_BASE_URL}/board"
        self.FULL_TASKS_URL = f"{KFLOW_BASE_URL}/tasks"
        (self.id, self.name, self.columns, self.swimlanes) = self.parse_board(self.fetch_board_json(token))
        tasks_by_column = [self.fetch_tasks_by_column(column, self.name, token) for column in self.columns]
        self.tasks = self.flatten_tasks(tasks_by_column)

    def fetch_board_json(self, token):
        self.log.info("Pulling token: %s", token)
        resp = requests.get(f"{self.FULL_BOARD_URL}?apiToken={token}")
        self.log.info("Status code: %s", resp.status_code)
        return resp.json()

    def parse_board(self, board_dict):
        columns = [Column(col_dict) for col_dict in board_dict["columns"]]
        swimlanes = [Swimlane(lane_dict) for lane_dict in board_dict["swimlanes"]]
        return board_dict["_id"], board_dict['name'], columns, swimlanes

    def flatten_tasks(self, lists_of_tasks):
        return [task for sublist in lists_of_tasks for task in sublist]

    def fetch_tasks_by_column(self, column, board_name, token):
        self.log.info("Pulling tasks for %s column in %s board", column.name, board_name)

        def fetch_tasks(column_id, next_task=None):
            base_url = f"{self.FULL_TASKS_URL}?apiToken={token}&columnId={column_id}"
            final_url = f"{base_url}&startTaskId={next_task}" if next_task else f"{base_url}"
            resp = requests.get(final_url)
            self.log.info("Status code: %s", resp.status_code)
            resp_dict = resp.json()
            tasks = [Task(t_dict) for t_dict in resp_dict[0]["tasks"]]
            if resp_dict[0].get("tasksLimited"):
                tasks.extend(fetch_tasks(column_id, resp_dict[0]["nextTaskId"]))
            return tasks

        return fetch_tasks(column.uniqueId)

    def get_spent_time(self):
        return sum([task.spent for task in self.tasks])

    def __str__(self):
        return f"{{ Id: {self.id}. Name: {self.name}. Columns: {self.columns}. Swimlanes: {self.swimlanes}. Tasks: {self.tasks} }}"

    def __repr__(self):
        return str(self)

