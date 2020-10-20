class Column(object):
    def __init__(self, col_dict):
        (self.name, self.uniqueId) = self.parse_dict(col_dict)

    def parse_dict(self, col_dict):
        return col_dict["name"], col_dict["uniqueId"]
