# XOR 암호화 및 복호화
def xor_encrypt(input_file, key, output_file):
    with open(input_file, "rb") as f:
        data = f.read()

    encrypted = bytearray()
    for byte in data:
        encrypted.append(byte ^ key)

    with open(output_file, "wb") as f:
        f.write(encrypted)

    print(f"Complete : {output_file}")

# 입력 받기 (이미지에 나온 형식대로)
input_file = input("input file : ").strip()
output_file = input("output file : ").strip()
key = int(input("input XOR key(0~255) : ").strip())

xor_encrypt(input_file, key, output_file)
