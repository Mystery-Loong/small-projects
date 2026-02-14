from cryptography.fernet import Fernet

import random
import string

try:
    with open("key_path", "rb") as f:
        key = f.read()
    print(f"Old key is: {key}")
except FileNotFoundError:
    key = Fernet.generate_key()
    with open("key_path", "wb") as f:
        f.write(key)
    print(f"New key is: {key}")

cipher = Fernet(key)

data = random.choices(string.ascii_letters, k=9)
print(f"Data is: {data}")
data = ''.join(data)
data_byte = data.encode("utf-8")

encrypted_data = cipher.encrypt(data_byte)
with open("test.txt", "wb") as f:
    f.write(encrypted_data)
    print(f"Encrypted data is: {encrypted_data}")

with open("test.txt", "rb") as f:
    line = f.read()
    decrypted_data = cipher.decrypt(line)
    print(decrypted_data)
