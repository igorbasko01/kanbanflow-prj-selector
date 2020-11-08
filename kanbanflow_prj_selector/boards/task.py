import logging


class Task(object):
    def __init__(self, task_dict):
        self.log = logging.getLogger()
        self.log.info("Task: %s", task_dict)
        self.id, self.name, self.desc, self.spent, self.est = self.parse(task_dict)

    def parse(self, task_dict):
        return task_dict.get("_id"), \
               task_dict.get("name"), \
               task_dict.get("description"), \
               task_dict.get("totalSecondsSpent"), \
               task_dict.get("totalSecondsEstimate")

    def get_spent_est_ratio(self):
        return self.spent / self.est

    def __str__(self):
        return f"{{ Name: {self.name}. Id: {self.id}. Spent: {self.spent}. Estimated: {self.est} }}"

    def __repr__(self):
        return str(self)
