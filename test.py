# test.py

from main import hash_password

if __name__ == "__main__":
    password = "MySecret123"
    hashed, key_used = hash_password(password)
    
    print(f"Original Password: {password}")
    print(f"Generated Key: {key_used}")
    print(f"Hash (base64): {hashed}")
