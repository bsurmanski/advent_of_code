def main():
    count = 0
    f = open('3.in')
    lines = f.read().split('\n')
    for i in range(0, len(lines)-1, 3):
        triplet = [lines[i].split(),
                   lines[i+1].split(),
                   lines[i+2].split()]
        for i in range(0, 3):
            triangle = [int(triplet[0][i]),
                        int(triplet[1][i]),
                        int(triplet[2][i])]
            triangle.sort()
            if (triangle[0] + triangle[1]) > triangle[2]:
                count += 1
    print count


if __name__ == "__main__":
    main()
