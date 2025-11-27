
if __name__ == "__main__":
    # 텍스트 파일 쓰기
    f = open("../../../OneDrive/바탕 화면/fastcampus/Part 1. 파이썬 라이브러리를 활용한 기초 프로젝트/ch02. [텍스트] 뉴스 기사 3줄 요약하기/새파일.txt", 'w')
    for i in range(1, 11):
        data = "%d번째 줄입니다.\n" % i
        f.write(data)
    f.close()

    # 모든 줄 읽기
    f = open("../../../OneDrive/바탕 화면/fastcampus/Part 1. 파이썬 라이브러리를 활용한 기초 프로젝트/ch02. [텍스트] 뉴스 기사 3줄 요약하기/새파일.txt", 'r')
    lines = f.readlines()
    for line in lines:
        print(line)
    f.close()