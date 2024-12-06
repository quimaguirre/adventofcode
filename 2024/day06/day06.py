import copy

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

def get_patrol_positions(patrol_map, start_coords, start_direction = "up", no_new_positions_limit = 1000):
    direction = start_direction
    patrol_active = True
    visited_positions = {start_coords}
    curr_coords = (start_coords[0], start_coords[1])
    no_new_positions_count = 0
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
                    if curr_coords in visited_positions:
                        no_new_positions_count += 1
                    else:
                        no_new_positions_count = 0
                        visited_positions.add(curr_coords)
            else:
                searching_next_location = False
                patrol_active = False
        if no_new_positions_count >= no_new_positions_limit:
            return {}
    return visited_positions

# Read input data and save starting position
patrol_map = []
start_coords = None
with open('input.txt') as input_fd:
    for i, line in enumerate(input_fd):
        positions = [pos for pos in line.strip()]
        patrol_map.append(positions)
        if '^' in positions:
            start_coords = (i, positions.index('^'))
start_location = patrol_map[start_coords[0]][start_coords[1]]
#print(start_coords)
#print(start_location)

# Part 1: Determine all unique positions visited by the guard until she falls
# off the grid
visited_positions = get_patrol_positions(patrol_map, start_coords)
print(len(visited_positions))

# Part 2: Check all possible positions in which an object creates a loop
loop_positions = set()
for i, positions in enumerate(patrol_map):
    for j, location in enumerate(patrol_map[i]):
        if (i, j) != start_coords and location != "#":
            new_patrol_map = copy.deepcopy(patrol_map)
            new_patrol_map[i][j] = "#"
            visited_positions = get_patrol_positions(new_patrol_map, start_coords)
            if len(visited_positions) == 0:
                loop_positions.add((i, j))
print(len(loop_positions))
