import unittest

from kanbanflow_prj_selector.boards.task import Task


class MyTestCase(unittest.TestCase):
    def test_parse_full_task(self):
        task = Task(full_task_sample())
        self.assertEqual("123", task.id)
        self.assertEqual("Write report", task.name)
        self.assertEqual("", task.desc)
        self.assertEqual(0, task.spent)
        self.assertEqual(3600, task.est)

    def test_parse_partial_task(self):
        task = Task(partial_task_sample())
        self.assertEqual("123", task.id)
        self.assertEqual("Write report", task.name)
        self.assertEqual("", task.desc)
        self.assertEqual(None, task.spent)
        self.assertEqual(None, task.est)

    def test_task_time_ratio_zero(self):
        task = Task(full_task_sample())
        self.assertEqual(0, task.get_spent_est_ratio())

    def test_task_time_ratio_some(self):
        task = Task(spent_task_sample())
        self.assertEqual(0.083, round(task.get_spent_est_ratio(), 3))


def spent_task_sample():
    return {
        "_id": "123",
        "name": "Write report",
        "description": "",
        "color": "red",
        "columnId": "todo",
        "totalSecondsSpent": 300,
        "totalSecondsEstimate": 3600
    }

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
