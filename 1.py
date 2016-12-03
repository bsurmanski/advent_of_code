input = "L1, R3, R1, L5, L2, L5, R4, L2, R2, R2, L2, R1, L5, R3, L4, L1, L2, R3, R5, L2, R5, L1, R2, L5, R4, R2, R2, L1, L1, R1, L3, L1, R1, L3, R5, R3, R3, L4, R4, L2, L4, R1, R1, L193, R2, L1, R54, R1, L1, R71, L4, R3, R191, R3, R2, L4, R3, R2, L2, L4, L5, R4, R1, L2, L2, L3, L2, L1, R4, R1, R5, R3, L5, R3, R4, L2, R3, L1, L3, L3, L5, L1, L3, L3, L1, R3, L3, L2, R1, L3, L1, R5, R4, R3, R2, R3, L1, L2, R4, L3, R1, L1, L1, R5, R2, R4, R5, L1, L1, R1, L2, L4, R3, L1, L3, R5, R4, R3, R3, L2, R2, L1, R4, R2, L3, L4, L2, R2, R2, L4, R3, R5, L2, R2, R4, R5, L2, L3, L2, R5, L4, L2, R3, L5, R2, L1, R1, R3, R3, L5, L2, L2, R5"


def next_direction(current, turn):
    if current == "NORTH":
        if turn == "L":
            return "WEST"
        elif turn == "R":
            return "EAST"

    if current == "EAST":
        if turn == "L":
            return "NORTH"
        elif turn == "R":
            return "SOUTH"

    if current == "SOUTH":
        if turn == "L":
            return "EAST"
        elif turn == "R":
            return "WEST"

    if current == "WEST":
        if turn == "L":
            return "SOUTH"
        elif turn == "R":
            return "NORTH"


def step_vector(direction):
    if direction == "NORTH":
        return (0, 1)
    elif direction == "EAST":
        return (1, 0)
    elif direction == "WEST":
        return (-1, 0)
    elif direction == "SOUTH":
        return (0, -1)


def scale(vector, v):
    return (vector[0] * v, vector[1] * v)


def add_vector(a, b):
    return (a[0] + b[0], a[1] + b[1])


def main():
    direction = "NORTH"
    location = (0, 0)
    for instruction in input.split(", "):
        turn = instruction[0]
        dist = int(instruction[1:])
        direction = next_direction(direction, turn)
        print direction, dist
        location = add_vector(location, scale(step_vector(direction), dist))
    print location


if __name__ == "__main__":
    main()
