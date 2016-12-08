import hashlib

input = "reyedfim"

def key_character(key):
    print key, hashlib.md5(key).hexdigest()
    return hashlib.md5(key).hexdigest()[5]

def key_is_special(key):
    return hashlib.md5(key).hexdigest().startswith('00000')

def main():
    door_id = ""
    i = 0
    while len(door_id) < 8:
        key_attempt = input + str(i)
        i += 1
        if key_is_special(key_attempt):
            door_id += key_character(key_attempt)
    print door_id

if __name__ == "__main__":
    main()
