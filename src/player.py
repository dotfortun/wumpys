import random

class Player(object):
    """docstring for Player."""
    def __init__(self, _location, _arrows = 5):
        super(Player, self).__init__()
        self.location = _location
        self.arrows = _arrows

    def attack(self):
        if self.arrows == 0:
            return False
        if len(self.location.neighbors) == 0:
            return False
        else:
            print("Adjacent rooms:")
            for room in self.location.neighbors:
                print(room.id)
            print("---")
            while True:
                try:
                    target = int(input("Type in a room number to fire your arrow:"))
                    break
                except ValueError:
                    print("That wasn't a room number.")
            for room in self.location.neighbors:
                if room.id ==
