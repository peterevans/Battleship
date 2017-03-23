class Ship(object):

    def __init__(self, name, length):
        self.name = name
        self.length = length
        self.location = []
        self.hits = 0
        self.orientation = ""
