def find_binary_pattern(file_path, pattern):
    print(f"패턴 {pattern} 찾기...")
    positions = []     
    offset = 0         

    with open(file_path, "rb") as file:
        data = file.read()  # 전체 파일 읽기

        while True:
            index = data.find(pattern, offset)  # pattern 찾기
            if index == -1:  # 없으면 끝내기
                break
            positions.append(index)  # 위치 저장
            offset = index + 1       # 다음 위치부터 다시 검색

    # 결과 출력
    print(f"총 {len(positions)}회 발견됨.")
    print("위치:", positions)

# 사용 예시
find_binary_pattern("large_data.bin", b'\xDE\xAD\xBE\xEF')
