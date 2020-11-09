import unittest
from unittest import mock

from kanbanflow_prj_selector.constants import KFLOW_BASE_URL
from kanbanflow_prj_selector.boards.board import Board


# Used the following solution for mocking the requests library: https://stackoverflow.com/a/28507806/6926045
# This method will be used by the mock to replace requests.get
def mocked_requests_get(*args, **kwargs):
    class MockResponse:
        def __init__(self, json_data, status_code):
            self.json_data = json_data
            self.status_code = status_code

        def json(self):
            return self.json_data

    if args[0] == f"{KFLOW_BASE_URL}/board?apiToken=test":
        return MockResponse(board_sample_response(), 200)
    elif args[0] == f"{KFLOW_BASE_URL}/tasks?apiToken=test&columnId=todo":
        return MockResponse(tasks1_sample_response(), 200)
    elif args[0] == f"{KFLOW_BASE_URL}/tasks?apiToken=test&columnId=todo&startTaskId=124":
        return MockResponse(tasks2_sample_response(), 200)
    elif args[0].startswith(f"{KFLOW_BASE_URL}/tasks?apiToken=test&columnId="):
        return MockResponse([{"tasks": []}], 200)

    return MockResponse(None, 404)


class MyTestCase(unittest.TestCase):
    @mock.patch('kanbanflow_prj_selector.boards.board.requests.get', side_effect=mocked_requests_get)
    def test_fetch_board_json(self, mock_get):
        board = Board('test')
        json_board = board.fetch_board_json('test')
        self.assertEqual(json_board, board_sample_response())

    @mock.patch('kanbanflow_prj_selector.boards.board.requests.get', side_effect=mocked_requests_get)
    def test_parse_board(self, mock_get):
        board = Board('test')
        self.assertEqual(board.name, 'My first board')
        self.assertEqual(board.id, '4ce35948f9ddf9b8c8d11e273f05bd43')
        self.assertEqual(len(board.columns), len(board_sample_response()["columns"]))
        self.assertEqual(len(board.swimlanes), len(board_sample_response()["swimlanes"]))
        self.assertEqual(len(tasks1_sample_response()[0]["tasks"]) + len(tasks2_sample_response()[0]["tasks"]),
                         len(board.tasks))
        self.assertEqual(7000, board.get_spent_time())


def tasks1_sample_response():
    return [
        {
            "columnId": "todo",
            "columnName": "ToDo",
            "tasksLimited": True,
            "nextTaskId": "124",
            "tasks": [
                {
                    "_id": "123",
                    "name": "Write report",
                    "description": "",
                    "color": "red",
                    "columnId": "todo",
                    "totalSecondsSpent": 4000,
                    "totalSecondsEstimate": 3600
                }
            ]
        }
    ]


def tasks2_sample_response():
    return [
        {
            "columnId": "todo",
            "columnName": "ToDo",
            "tasksLimited": False,
            "tasks": [
                {
                    "_id": "124",
                    "name": "Write report",
                    "description": "",
                    "color": "red",
                    "columnId": "todo",
                    "totalSecondsSpent": 3000,
                    "totalSecondsEstimate": 3600
                }
            ]
        }
    ]


def board_sample_response():
    return {
        "_id": "4ce35948f9ddf9b8c8d11e273f05bd43",
        "name": "My first board",
        "columns": [
            {
                "name": "To-do",
                "uniqueId": "todo"
            },
            {
                "name": "Do today",
                "uniqueId": "today"
            },
            {
                "name": "In progress",
                "uniqueId": "progress"
            },
            {
                "name": "Done",
                "uniqueId": "done"
            }
        ],
        "swimlanes": [
            {
                "name": "Team Alpha",
                "uniqueId": "167d908046cb11e391de452f6829aed3"
            },
            {
                "name": "Team Beta",
                "uniqueId": "31133230703711e29a57f90ce31cf483"
            }
        ],
        "colors": [
            {
                "name": "Bug",
                "value": "red",
                "description": "This is a bug."
            },
            {
                "name": "Feature",
                "value": "green",
                "description": "This is a feature."
            }
        ]
    }


if __name__ == '__main__':
    unittest.main()
