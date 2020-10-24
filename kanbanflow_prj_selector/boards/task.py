import logging


class Task(object):
    def __init__(self, task_dict):
        self.log = logging.getLogger()
        self.log.info("Task: %s", task_dict)
        pass
