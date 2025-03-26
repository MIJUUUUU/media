import pickle
import os


filename = "media_data.pkl"


if os.path.exists(filename):
    with open(filename, "rb") as f:
        me_data = pickle.load(f)
else:
    me_data = {}

print("멀티미디어 태그 관리 시스템")
print("1. 콘텐츠 등록")
print("2. 종료")

choose = input("메뉴 선택 (1~2): ")

if choose == "1":
    try:
        id = input("콘텐츠 ID 입력: ").strip()
        if not id:
            raise ValueError("ID는 비어 있을 수 없습니다.")
        if id in me_data:
            raise ValueError("이미 존재하는 ID입니다.")

        title = input("제목 입력: ").strip()
        if not title:
            raise ValueError("제목은 비어 있을 수 없습니다.")

        type = input("타입 (image/video/audio): ").strip().lower()
        if type not in ["image", "video", "audio"]:
            raise ValueError("타입은 image, video, audio 중 하나여야 합니다.")

        tags = input("태그 입력 (쉼표 구분): ").strip()
        if not tags:
            raise ValueError("태그는 비어 있을 수 없습니다.")
        
        
        me_data[id] = {
            "title": title,
            "type": type,
            "tags": tags
        }

      
        with open(filename, "wb") as f:
            pickle.dump(me_data, f)

        print("데이터가 저장되었습니다.")

    except Exception as e:
        print(f"입력 오류: {e}")

elif choose == "2":
    print("프로그램 종료")
else:
    print("잘못된 메뉴 선택입니다.")
