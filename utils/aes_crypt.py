import json

from Crypto.Cipher import AES
import time
import re
from binascii import b2a_hex,a2b_hex, Error


def _pad(s):
    tail = (AES.block_size - len(s) % AES.block_size) * chr(AES.block_size - len(s) % AES.block_size)
    _s = s + tail
    print(tail)
    return _s.encode()


def _cipher():
    key = '4321432143214321'.encode()
    iv = '1234123412341234'.encode()
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
    t= int(time.time())*1000
    check_by = '17611158275'
    tp_id = 55
    en_text = aes_encrypt('{"t": %d, "check_by": "%s", "channelId": "2", "tpAccountId": %d}'%(t,check_by,tp_id))
    print('密文:', en_text)
    tokens = "9e5600246d4d75212a00840411f60171e2370462b604ca104785735b8bdb858c46e0b740d7c3e228da4700accccc8535736efc8cc7e4e9ce2f975bcc335f761bcc7484f50882141ab2e361291ca7e03b"
    token = "6e1ca3eb225a4fa976423e30b90ef1a37629cd736cf9f9c8c540784777d4e1d5391cb62884d32e3c8a07ccdaa711a012f0b6ba3ef6c1648eaf1b566843902c18bc04156267cd72876e622fb33d2eb408246e69f56e57997070bb2acb22f6472a"
    print('明文:', aes_decrypt(tokens))