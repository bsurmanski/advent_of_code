def main():
    count = 0
    for line in open('3.in'):
        sides = [int(side) for side in line.split()]
        sides.sort()
        print sides
        if (sides[0] + sides[1]) > sides[2]:
            count += 1
    print count


if __name__ == "__main__":
    main()
