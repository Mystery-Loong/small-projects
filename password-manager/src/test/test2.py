from cryptography.fernet import Fernet
import os

# ---------- 第一次运行：加密 ----------
def encrypt_and_save(data: bytes, key_path: str, output_path: str):
    # 生成密钥并保存
    key = Fernet.generate_key()
    with open(key_path, 'wb') as f:
        f.write(key)
    
    # 加密数据
    cipher = Fernet(key)
    token = cipher.encrypt(data)
    with open(output_path, 'wb') as f:
        f.write(token)
    print("加密完成，密钥和密文已保存。")

# ---------- 重新运行：解密 ----------
def decrypt_from_saved(key_path: str, input_path: str) -> bytes:
    # 加载密钥
    with open(key_path, 'rb') as f:
        key = f.read()
    
    # 加载密文
    with open(input_path, 'rb') as f:
        token = f.read()
    
    # 解密
    cipher = Fernet(key)
    plain = cipher.decrypt(token)
    print(plain)
    return plain

# 使用示例
# if not os.path.exists('secret.key'):   # 首次运行
#     encrypt_and_save(b'Hello, World!', 'secret.key', 'data.enc')
# else:                                  # 后续运行
#     decrypted = decrypt_from_saved('secret.key', 'data.enc')
#     print('解密结果:', decrypted.decode())

try:
    with open("key_path", "rb") as f:
        key = f.read()
    print(f"Old key is: {key}")
except FileNotFoundError:
    key = Fernet.generate_key()
    with open("key_path", "wb") as f:
        f.write(key)
    print(f"New key is: {key}")