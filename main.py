from src.room import Room
from src.player import Player
from src.wumpus import Wumpus

map = [
Room(0),
Room(1),
Room(2),
Room(3),
Room(4),
Room(5),
Room(6),
Room(7)
]

map[0].add_neighbors([map[3], map[4], map[1]])
map[2].add_neighbors([map[1], map[3], map[6]])
map[5].add_neighbors([map[1], map[4], map[6]])
map[7].add_neighbors([map[3], map[4], map[6]])

while True:
    # text parser block will go here.
    # text parser block ends here.
    player.update()
    wumpus.update()
    for room in map:
        room.update()
