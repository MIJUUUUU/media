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
print("2. 태그로 검색")
print("3. 콘텐츠 태그 수정")
print("4. 종료")

menu = input("메뉴 선택 (1~4): ")


if menu == "1":
    id = input("콘텐츠 ID 입력: ").strip()
    if id in me_data:
        print("이미 존재하는 ID입니다.")
    else:
        title = input("제목 입력: ").strip()
        content_type = input("타입 (image/video/audio): ").strip().lower()
        tags_input = input("태그 입력 (쉼표로 구분): ").strip()
        tags = [tag.strip() for tag in tags_input.split(",")]

        me_data[id] = {
            "title": title,
            "type": content_type,
            "tags": tags
        }

        with open(filename, "wb") as f:
            pickle.dump(me_data, f)

        print(f"{id} 콘텐츠가 저장되었습니다.")


elif menu == "2":
    keyword = input("검색할 태그 입력: ").lower()
    found = False

    for id, content in me_data.items():
        for tag in content["tags"]:
            if keyword in tag.lower():
                print(f"\n- ID: {id}, 제목: {content['title']}, 타입: {content['type']}, 태그: {content['tags']}")
                found = True
                break

    if not found:
        print("해당 태그를 가진 콘텐츠가 없습니다.")


elif menu == "3":
    id = input("수정할 콘텐츠 ID 입력: ").strip()

    if id in me_data:
        print(f"현재 태그: {me_data[id]['tags']}")
        new_tags_input = input("새로운 태그 입력 (쉼표로 구분): ").strip()
        new_tags = [tag.strip() for tag in new_tags_input.split(",")]

        me_data[id]['tags'] = new_tags

        with open(filename, "wb") as f:
            pickle.dump(me_data, f)

        print(f"{id}의 태그가 수정되었습니다.")
    else:
        print("해당 ID의 콘텐츠가 없습니다.")


elif menu == "4":
    print("프로그램을 종료합니다.")

else:
    print("올바른 메뉴를 선택하세요.")
