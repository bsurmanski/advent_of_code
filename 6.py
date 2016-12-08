def main():
    columns = []
    for line in open("6.in"):
        for i in range(len(line)):
            if len(columns) <= i:
                columns.append(dict())
            count = columns[i].setdefault(line[i], 0)
            columns[i][line[i]] = count + 1

    for column in columns:
        # for part two, use "lambda a, b: a[1] - b[1]"
        items = sorted(column.items(), lambda a, b: b[1] - a[1])
        print items[0]
    print columns


if __name__ == "__main__":
    main()
