import csv

class Parser(object):
    """docstring for Parser."""
    def __init__(self, _lang = 'en_us'):
        super(Parser, self).__init__()
        reader = []
        self.strings = {}
        with open(_lang + '.csv', 'rb') as localization:
            reader = csv.reader(localization)
        for row in reader:
            self.strings[row[0]] = row[1]

    def render(self, _player, _wumpus):
        return NotImplemented
