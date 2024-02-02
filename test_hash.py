from passlib.hash import pbkdf2_sha256

salt = '암호화'

data_raw = '1234'

# 인코딩
data_hash = pbkdf2_sha256.hash(data_raw + salt)
print(data_hash)

# 디코딩 및 확인
print(pbkdf2_sha256.verify(data_raw + salt, data_hash))