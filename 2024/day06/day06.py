def get_next_direction(direction):
    if direction == "up":
        next_direction = "right"
    elif direction == "right":
        next_direction = "down"
    elif direction == "down":
        next_direction = "left"
    elif direction == "left":
        next_direction = "up"
    return next_direction

def guard_move(curr_coords, direction):
    if direction == "up":
        next_coords = (curr_coords[0] - 1, curr_coords[1])
    elif direction == "down":
        next_coords = (curr_coords[0] + 1, curr_coords[1])
    elif direction == "left":
        next_coords = (curr_coords[0], curr_coords[1] - 1)
    elif direction == "right":
        next_coords = (curr_coords[0], curr_coords[1] + 1)
    return next_coords

patrol_map = []
curr_coords = None
with open('input.txt') as input_fd:
    for i, line in enumerate(input_fd):
        positions = [pos for pos in line.strip()]
        patrol_map.append(positions)
        if '^' in positions:
            curr_coords = (i, positions.index('^'))
curr_location = patrol_map[curr_coords[0]][curr_coords[1]]
#print(curr_coords)
#print(curr_location)

direction = "up"
patrol_active = True
visited_positions = {curr_coords}
while patrol_active:
    searching_next_location = True
    while searching_next_location:
        next_coords = guard_move(curr_coords, direction)
        if (next_coords[0] >= 0 and next_coords[0] < len(patrol_map)) and (next_coords[1] >= 0 and next_coords[1] < len(patrol_map[0])):
            next_location = patrol_map[next_coords[0]][next_coords[1]]
            if next_location == '#':
                direction = get_next_direction(direction)
            else:
                searching_next_location = False
                curr_coords = (next_coords[0], next_coords[1])
                visited_positions.add(curr_coords)
                #print(curr_coords)
                #print(next_location)
        else:
            searching_next_location = False
            patrol_active = False

print(len(visited_positions))
