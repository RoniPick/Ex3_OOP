from Location import Location


class Node:

    def __init__(self, id, location):  # data constructor
        self.id = id
        self.weight = 0.0
        self.tag = 0
        self.location = location  # x: location[0], y: location[1], z: location[2]

    def __repr__(self):
        return f"id:{self.id}"

