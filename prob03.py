def split_binary_file(file_path, chunk_size=5 * 1024 * 1024):  # 5MB
    part_num = 1  # 분할 파일 번호 시작

    with open(file_path, "rb") as file:
        while True:
            chunk = file.read(chunk_size)  # 5MB만큼 읽기
            if not chunk:  # 더 이상 읽을 게 없으면 끝
                break

            part_file_name = f"part_{part_num}.bin"  # 저장할 파일 이름
            with open(part_file_name, "wb") as part_file:
                part_file.write(chunk)

            print(f"Saved: {part_file_name}")  # 저장 완료 메시지
            part_num += 1  # 다음 번호로 증가

# 실행 예시
split_binary_file("large_data.bin")
