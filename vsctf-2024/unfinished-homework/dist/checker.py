from Crypto.Cipher import AES
from Crypto.Util.Padding import pad
from hashlib import sha256
from secret import answer, flag # answer is the program output

key = sha256(str(answer).encode()).digest()
cipher = AES.new(key, AES.MODE_ECB)
print(cipher.encrypt(pad(flag.encode(), AES.block_size)).hex())
# 0466ad08f5ec06289f168e80f88ae7c727c09253e6b5d1386f60a8fd272e5676409634cd96702b91c3b93f9880dc16971cba684dc97d1c15efbef22c41ee363407e603413c6ea8cd2bf734f1759bd4b492c5f182f53667f19c9aa2259e0ee620