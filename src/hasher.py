import hashlib
from cryptography.hazmat.primitives import hashes
from Crypto.Hash import SHA512

# 1. Стандартна бібліотека (вже була)
def calculate_sha512(data: str) -> str:
    return hashlib.sha512(data.encode('utf-8')).hexdigest()

# 2. Бібліотека 'cryptography'
def calculate_sha512_cryptography(data: str) -> str:
    digest = hashes.Hash(hashes.SHA512())
    digest.update(data.encode('utf-8'))
    return digest.finalize().hex()

# 3. Бібліотека 'pycryptodome'
def calculate_sha512_pycryptodome(data: str) -> str:
    h_obj = SHA512.new(data.encode('utf-8'))
    return h_obj.hexdigest()