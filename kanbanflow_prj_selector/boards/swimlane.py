class Swimlane(object):
    def __init__(self, lane_dict):
        self.name, self.uniqueId = self.parse(lane_dict)

    def parse(self, lane_dict):
        return lane_dict["name"], lane_dict["uniqueId"]
