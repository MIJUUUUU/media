def split_binary_file(file_path, chunk_size=5 * 1024 * 1024):  
    part_num = 1  

    with open(file_path, "rb") as file:
        while True:
            chunk = file.read(chunk_size)  
            if not chunk:  
                break

            part_file_name = f"part_{part_num}.bin"  
            with open(part_file_name, "wb") as part_file:
                part_file.write(chunk)

            print(f"Saved: {part_file_name}")  
            part_num += 1 


split_binary_file("large_data.bin")
