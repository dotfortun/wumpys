import random

class Player(object):
    """docstring for Player."""
    def __init__(self, _location, _arrows = 5):
        super(Player, self).__init__()
        self.location = _location
        self.arrows = _arrows

    def attack(self, _room):
        if self.arrows < 1:
            print('You are out of arrows.')
            return
        else:
            self.arrows -= 1
            _room.arrows += 1
            if random.randint(0,9) < 4:
                _room.hit = True
            else:
                return
    def move(self, _room):
        self.location = _room
