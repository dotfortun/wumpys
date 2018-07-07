import random

class Wumpus(object):
    """docstring for Wumpus."""
    def __init__(self, _location, _state = "SLEEP"):
        super(Wumpus, self).__init__()
        self.location = _location
        self.state = _state

    def update(self):
        if self.location.hit is True:
            self.state = "DEAD"
        elif self.location.last_arrows is True:
            self.state = "STARTLED"
        else:
            self.state = "SLEEP"

        if self.state == "SLEEP":
            return
        elif self.state == "STARTLED":
            self.location = random.choice(self.location.neighbors)
            self.state = "SLEEP"
        else:
            return
