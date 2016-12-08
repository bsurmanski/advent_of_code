import hashlib

input = "reyedfim"

def key_hash(key):
    return hashlib.md5(key).hexdigest()


def hash_is_special(hash):
    return hash.startswith('00000')


def main():
    door_id = list("-" * 8)
    i = 0
    while door_id.count('-') > 0:
        key_attempt = input + str(i)
        hash = key_hash(key_attempt)
        if hash_is_special(hash):
            if '0' <= hash[5] <= '7':
                index = ord(hash[5]) - ord('0')
                if door_id[index] == '-':
                    door_id[index] = hash[6]
                print "".join(door_id)
        i += 1

if __name__ == "__main__":
    main()
