import json

from Crypto.Cipher import AES
import time
import re
from binascii import b2a_hex, a2b_hex, Error


def _pad(s):
    tail = (AES.block_size - len(s) % AES.block_size) * chr(AES.block_size - len(s) % AES.block_size)
    _s = s + tail
    print(tail)
    return _s.encode()


def _cipher():
    key = 'ss123123123423'.encode()
    iv = 'fd233423sdfs'.encode()
    return AES.new(key=key, mode=AES.MODE_CBC, IV=iv)


def aes_encrypt(data):
    return b2a_hex(_cipher().encrypt(_pad(data))).decode()


def aes_decrypt(data):
    try:
        _d = _cipher().decrypt(a2b_hex(data))
        for i in range(AES.block_size):
            _d = _d.rstrip(chr(i).encode())
        res = json.loads(re.search(r'({.*})', _d.decode()).group(1))
        return res
    except Error as e:
        return {"msg": e}


if __name__ == '__main__':
    t = int(time.time()) * 1000
    check_by = '17611158275'
    tp_id = 55
    tokens = "9e5600246d4d75212a00840411f60171e2370462b604ca104785735b8bdb858c46e0b740d7c3e228da4700accccc8535736efc8cc7e4e9ce2f975bcc335f761bcc7484f50882141ab2e361291ca7e03b"
    token = "adfaadfadfasdf"
    print('明文:', aes_decrypt(tokens))
