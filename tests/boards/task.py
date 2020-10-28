import unittest

from kanbanflow_prj_selector.boards.task import Task


class MyTestCase(unittest.TestCase):
    def test_parse_full_task(self):
        task = Task(full_task_sample())
        assert task.id == "123"
        assert task.name == "Write report"
        assert task.desc == ""
        assert task.spent == 0
        assert task.est == 3600

    def test_parse_partial_task(self):
        task = Task(partial_task_sample())
        assert task.id == "123"
        assert task.name == "Write report"
        assert task.desc == ""
        assert task.spent is None
        assert task.est is None


def full_task_sample():
    return {
        "_id": "123",
        "name": "Write report",
        "description": "",
        "color": "red",
        "columnId": "todo",
        "totalSecondsSpent": 0,
        "totalSecondsEstimate": 3600
    }

def partial_task_sample():
    return {
        "_id": "123",
        "name": "Write report",
        "description": "",
        "color": "red",
        "columnId": "todo",
    }


if __name__ == '__main__':
    unittest.main()
