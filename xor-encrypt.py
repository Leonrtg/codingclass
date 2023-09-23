"""
XOR is not recommended as encrypt method for real use cases.
This is just an example of a simple symmetric cypher
"""

def xor_encrypt_decrypt(input_str, key):
    # Convert input string and key to bytes
    input_bytes = input_str.encode('utf-8')
    key_bytes = key.encode('utf-8')
    
    # Make sure key is long enough by repeating it
    key_long = bytearray()
    for i in range(len(input_bytes)):
        key_long.append(key_bytes[i % len(key_bytes)])
    
    # Perform XOR encryption/decryption
    encrypted_bytes = bytearray()
    for i in range(len(input_bytes)):
        encrypted_bytes.append(input_bytes[i] ^ key_long[i])
    
    # Convert the bytes back to a string
    encrypted_str = encrypted_bytes.decode('utf-8', errors='replace')
    
    return encrypted_str


user_input = input("""Hello. 
If you want to encrypt a message, type 1. 
If you want to decrypt a message, type 2.
""")


if user_input == "1":
    user_input = input("Enter your message you want to encrypt: ")
    message = user_input
    user_input = input("Enter they key you want to encrypt with: ")
    key = user_input

    encrypted_message = xor_encrypt_decrypt(message, key)
    print(f"Encrypted Message: {encrypted_message}")
    
if user_input == "2":
    user_input = input("Enter your message you want to decrypt: ")
    message = user_input
    user_input = input("Enter they key you want to decrypt with: ")
    key = user_input

    decrypted_message = xor_encrypt_decrypt(message, key)
    print(f"Decrypted Message: {decrypted_message}")
    
