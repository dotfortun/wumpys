from src.room import Room

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

print('\n\n')

# map[0].add_neighbors([map[3], map[4], map[1]])
# map[2].add_neighbors([map[1], map[3], map[6]])
# map[5].add_neighbors([map[1], map[4], map[6]])
# map[7].add_neighbors([map[3], map[4], map[6]])

map[0].add_neighbors(map[3])

for room in map:
    print(room.id)
    for neighbor in room.neighbors:
        print(neighbor.id)
    print('---')
