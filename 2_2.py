input = """
RRLLRLLRULLRUUUDRDLDDLLLDDDDDUUURRRRUUDLRULURRRDRUDRUUDDRUDLLLRLDDDUDRDDRRLLLLRLRLULUURDRURRUULDRRDUDURRUURURDLURULLDUDRDLUUUUDDURRLLLUDLDLRDRRRDULLDLDULLDRLDLDURDLRRULLDDLDRLLLUDDLLRDURULLDDDDDUURURLRLRRDUURUULRLLLULLRLULLUUDRRLLDURLDDDDULUUDLUDDDULRLDURDDRUUDRRUUURLLLULURUDRULDRDUDUDRRDDULRURLLRRLRRLLDLULURDRDRULDRDRURUDLLRRDUUULDDDUURDLULDLRLLURRURLLUDURDDRUDRDLLLLDLRLDLDDRDRRDUUULLUULRRDLURLDULLDLDUUUULLLDRURLRULLULRLULUURLLRDDRULDULRLDRRURLURUDLRRRLUDLDUULULLURLDDUDDLLUDRUDRLDUDURRRRLRUUURLUDDUDURDUDDDLLRLRDDURDRUUDUDRULURLRLDRULDRRLRLDDDRDDDRLDUDRLULDLUDLRLRRRLRDULDDLRRDDLDDULDLLDU
RULLUDDUDLULRRDLLDRUDLLLDURLLLURDURLRDRRDLRDRDLLURRULUULUDUDDLLRRULLURDRLDURDLDDUURLUURLDLDLRLDRLRUULDRLRLDRLRLUDULURDULLLDRUDULDURURRRUDURDUDLRDRRURULRRLRLRRRRRRDRUDLDRULDRUDLRDLRRUDULDLRLURRRLLDRULULRUDULRLULLRLULDRUDUULLRUULDULDUDDUUULLLDRDDRRDLURUUDRRLRRRDLRRLULLLLDLRUULDLLULURUURURDRURLLDUDRRURRURRUUDDRRDDRRRRUDULULRLUULRRDDRDDLLUDLDLULLRLDRLLUULDURLDRULDDUDRUUUURRLDDUDRUURUDLLDLDLURDLULDRLLLULLLUDLLDLD
RDLDULURDLULRRDLRLLLULRUULURULLLDLLDDRLLURUUUURDRLURLLRLRLLLULRDLURDURULULDDUDDUDRLRLDLULLURRRUULUDRDURRRUDDDLUDLDLRLRRLLLRUULLLLURRDDDRRRUURULRLDRRRLRLUDDRRULDDDRUUDDRLLDULRLUDUDLDLDDDUDDLLDDRDRDUDULDRRUDRDRRDRLUURDLRDDDULLDRRRRRUDRLURDUURRDDRLUDLURRRLRDDDLRRLUULRLURDUUURRDLDDULLLRURRRUDRLUDLLDDDDDUDDRDULLUUDDURRLULLUDULUUDRLDRRRLLURLRRLLDLLLLUDRUUUDDULLRDLLDUDUDUURRUUUDRUURDRDLLDLDDULLDDRRULDLDDUUURLDLULLLRRLLRDDULLDLDLDDLDLDULURRDURURDRDRRDLR
RDRLRRUUDRLDUDLLDLUDLUUDUDLRRUUDRDDDLDDLLLRRRUDULLRRRRRURRRLUDDDLRRRRUUULDURDRULLDLRURRUULUDRURRRRLRURLRDUUDUDUDRDDURRURUDLLLLLRURUULRUURLLURDRUURLUDDDRLDDURDLDUDRURDRLRRRRUURDDRRRRURDLUUDRLDRDUULURUDDULLURRDUDLUULLDURRURLUDUUDRDDDUUDDUUUULDLDUDDLUDUUDRURLLULRUUULLRRDDUDDLULDDUUUDLUDDLDDLLRUUDRULLRRDRLLDLLRRLULLRRDDRLRDUULLLUULLDLLUDUDDLRDULUDLDLUDDRRRRDUDLUULLULDLRRDLULRLRRRULRURRDRLULDDUDLDLDULLURLLRDLURRULURDLURLUDRDRRUUDRLLUDDRLRDDUURLRRDUDLDRURDUUUDRRLLRDLDLLDRRURLUDURUULDUDLDDDDRUULLDDRLRURRDURLURRLDDRRRRLRLRDRURUDDRDLDRURLULDDL
RULRDLDDLRURDDDDDDRURLLLDDDUUULLRRDLDLURUURLUDLURRLUDUURDULDRUULDDURULDUULDDULLLUDLRULDRLDLRDDRRDLDDLLDRRUDDUDRDUULUDLLLDDLUUULDDUUULRRDULLURLULDLRLLLRLURLLRLRLDRDURRDUUDDURRULDDURRULRDRDUDLRRDRLDULULDRDURDURLLLDRDRLULRDUURRUUDURRDRLUDDRRLDLDLULRLLRRUUUDDULURRDRLLDLRRLDRLLLLRRDRRDDLDUULRLRRULURLDRLRDULUDRDLRUUDDDURUDLRLDRRUDURDDLLLUDLRLURDUDUDULRURRDLLURLLRRRUDLRRRLUDURDDDDRRDLDDLLDLRDRDDRLLLURDDRDRLRULDDRRLUURDURDLLDRRRDDURUDLDRRDRUUDDDLUDULRUUUUDRLDDD
"""


def position_to_key(position):
    if (position[0] < 0 or position[0] >= 5 or
        position[1] < 0 or position[1] >= 5):
        return '-'

    map = [['-', '-', '1', '-', '-'],
           ['-', '2', '3', '4', '-'],
           ['5', '6', '7', '8', '9'],
           ['-', 'A', 'B', 'C', '-'],
           ['-', '-', 'D', '-', '-']]
    return map[position[1]][position[0]]


def next_position(position, move):
    next = position[:]
    if move == "U":
        next[1] -= 1
    if move == "D":
        next[1] += 1
    if move == "L":
        next[0] -= 1
    if move == "R":
        next[0] += 1
    return next


def main():
    position = [1, 1]
    for key_sequence in input.split():
        for move in key_sequence:
            next = next_position(position, move)
            if position_to_key(next) != '-':
                position = next
        print position_to_key(position)

if __name__ == "__main__":
    main()
