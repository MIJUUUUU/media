# 📄 comp.py

def compare_lowdata(samples):
    # 🎯 실제 정답 샘플 (예시 일부만 작성 – 실제로는 훨씬 길어야 함!)
    correct_samples = [
        -2, 1, 4, -3, 0, 3, 2, -1, 0, 0
        # 실제 정답 데이터는 실습에서 제공되는 파일 기준으로 채워야 함!
    ]

    if len(samples) != len(correct_samples):
        return False

    for i in range(len(samples)):
        if samples[i] != correct_samples[i]:
            return False

    return True
