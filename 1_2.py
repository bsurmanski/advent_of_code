input = "L1, R3, R1, L5, L2, L5, R4, L2, R2, R2, L2, R1, L5, R3, L4, L1, L2, R3, R5, L2, R5, L1, R2, L5, R4, R2, R2, L1, L1, R1, L3, L1, R1, L3, R5, R3, R3, L4, R4, L2, L4, R1, R1, L193, R2, L1, R54, R1, L1, R71, L4, R3, R191, R3, R2, L4, R3, R2, L2, L4, L5, R4, R1, L2, L2, L3, L2, L1, R4, R1, R5, R3, L5, R3, R4, L2, R3, L1, L3, L3, L5, L1, L3, L3, L1, R3, L3, L2, R1, L3, L1, R5, R4, R3, R2, R3, L1, L2, R4, L3, R1, L1, L1, R5, R2, R4, R5, L1, L1, R1, L2, L4, R3, L1, L3, R5, R4, R3, R3, L2, R2, L1, R4, R2, L3, L4, L2, R2, R2, L4, R3, R5, L2, R2, R4, R5, L2, L3, L2, R5, L4, L2, R3, L5, R2, L1, R1, R3, R3, L5, L2, L2, R5"

class Vector:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __add__(self, o):
        return Vector(self.x + o.x, self.y + o.y)

    def asTuple(self):
        return (self.x, self.y)


def next_direction(current, turn):
    if current == "N":
        return {"L": "W", "R": "E"}[turn]
    if current == "E":
        return {"L": "N", "R": "S"}[turn]
    if current == "S":
        return {"L": "E", "R": "W"}[turn]
    if current == "W":
        return {"L": "S", "R": "N"}[turn]


def direction_vector(direction):
    if direction == "N":
        return Vector(0, 1)
    if direction == "E":
        return Vector(1, 0)
    if direction == "S":
        return Vector(0, -1)
    if direction == "W":
        return Vector(-1, 0)


def main():
    visited = {(0,0) : True}
    location = Vector(0, 0)
    direction = "N"
    for instruction in input.split(", "):
        turn, step = instruction[0], int(instruction[1:])
        direction = next_direction(direction, turn)
        for i in range(step):
            location += direction_vector(direction)
            if location.asTuple() in visited:
                print location.asTuple()
                return
            visited[location.asTuple()] = True

if __name__ == "__main__":
    main()
