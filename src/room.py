class Room():
    """Rooms contain stuff."""
    id = None
    neighbors = []
    contents = ''


    def __init__(self, _id):
        self.id = _id
        self.neighbors = []
        self.contents = ''

    def add_neighbors(self, _neighbors):
        if type(_neighbors) is not list:
            print('Adding', _neighbors.id, 'to', self.id)
            self.neighbors.append(_neighbors)
            _neighbors.neighbors.append(self)
        else:
            for room in _neighbors:
                if room not in self.neighbors:
                    self.add_neighbors(room)
