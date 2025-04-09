def find_binary_pattern(file_path, pattern):
    print(f"패턴 {pattern} 찾기...")
    positions = []     
    offset = 0         

    with open(file_path, "rb") as file:
        data = file.read()  

        while True:
            index = data.find(pattern, offset)  
            if index == -1: 
                break
            positions.append(index) 
            offset = index + 1      

  
    print(f"총 {len(positions)}회 발견됨.")
    print("위치:", positions)

find_binary_pattern("large_data.bin", b'\xDE\xAD\xBE\xEF')
