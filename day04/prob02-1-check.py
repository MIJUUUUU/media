def print_binary_preview(file_path, num_bytes=64):
    with open(file_path, "rb") as f:
        data = f.read(num_bytes)
        print(f"[{file_path}] {num_bytes} Bytes:")
        print(data.hex(" "))
        print()
    return data

data_secret = print_binary_preview("secret_data.bin")
data_encrypted = print_binary_preview("encrypted_data.bin")
data_decrypted = print_binary_preview("decrypted_data.bin")
