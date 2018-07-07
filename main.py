from src.room import Room
from src.player import Player
from src.wumpus import Wumpus
import random
import time

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

player = Player(random.choice(map))
wumpus = Wumpus(random.choice(map))

while wumpus.location is player.location:
    wumpus.location = random.choice(map)

while player.state != 'DEAD':
# text parser block will go here.
    print("Player is in room", player.location.id)
    for room in player.location.neighbors:
        if room.id != wumpus.location.id:
            print(room.id, "safe.")
        else:
            print(room.id, "dangerous.")

    player.move(random.choice(player.location.neighbors))
# text parser block ends here.
    wumpus.location.last_arrows = True
    print("The wumpus was in room", wumpus.location.id)
    if player.location.id == wumpus.location.id:
        player.state = "DEAD"
    print("Player moved to", player.location.id, "\n\n---\n")
    wumpus.update()
    for room in map:
        room.update()
    time.sleep(1)
print('YOU DIED.')
