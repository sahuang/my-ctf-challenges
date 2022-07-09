from base64 import b64decode

# Copied rc4 implementation online
def rc4(data, key, skip=1024):
    x = 0
    box = list(range(256))

    x = 0
    for i in range(256):
        x = (x + box[i] + ord(key[i % len(key)])) % 256
        tmp = box[i]
        box[i] = box[x]
        box[x] = tmp

    x = 0
    y = 0
    out = []
    if skip > 0:
        for i in range(skip):
            x = (x + 1) % 256
            y = (y + box[x]) % 256
            box[x], box[y] = box[y], box[x]
	
    for char in data:
        x = (x + 1) % 256
        y = (y + box[x]) % 256
        box[x], box[y] = box[y], box[x]
        k = box[(box[x] + box[y]) % 256]
        # print(k)
        out.append(chr(char ^ k))

    return ''.join(out)


data = [x for x in b64decode("nRYEZjDuqxtlL8L6EatC")]
print(rc4(data, "vsCTF is a capture the flag competition organized by Team View Source. vsCTF is meant for players of all skill levels and everyone is welcomed to participate and learn.", 0))

# vsctf4beginnerz