def char_to_index(char):
    return ord(char) - ord('a')


def index_to_char(idx):
    return chr(idx + ord('a'))


def room_is_valid(letter_freq, checksum):
    sorted_freq_kv = zip(letter_freq, range(0, 26))
    # sort desc by freq (already sorted asc alphabetically)
    sorted_freq_kv.sort(lambda a, b: b[0] - a[0])
    sorted_freq_str = ""
    for i in range(0, 5):
        sorted_freq_str += index_to_char(sorted_freq_kv[i][1])
    return sorted_freq_str == checksum


# for part 2
def decrypt_name(name, sector_id):
    decrypted_name = ""
    for char in name:
        decrypted_name += index_to_char((char_to_index(char) + int(sector_id)) % 26)
    return decrypted_name


def main():
    input = open('4.in').read()
    count = 0
    for room_id in input.split():
        letter_freq = [0] * 26
        room_id_segments = room_id.split('-')

        # break row into room_id and checksum
        room_id_lst, room_metadata = room_id_segments[:-1], room_id_segments[-1]

        # join list of strings into one string
        room_id_str = ''.join(room_id_lst)

        # find all letter frequencies
        for char in room_id_str:
            letter_freq[char_to_index(char)] += 1

        sector_id, checksum = room_metadata[:-1].split('[')

        if room_is_valid(letter_freq, checksum):
            count += int(sector_id)
            print decrypt_name(room_id_str, sector_id), sector_id
    print count


if __name__ == "__main__":
    main()
