class Wumpus(object):
    """docstring for Wumpus."""
    def __init__(self, _location, _state = "SLEEP"):
        super(Wumpus, self).__init__()
        self.location = _location
        self.state = _state

    def update(self):

        if self.state == "SLEEP":
            print('The Wumpus sleeps.')
