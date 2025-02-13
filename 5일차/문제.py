# *문제
# =>아래 문자열을 사용하여 해시태그 처리할 것
input_text = "코딩 개발 파이썬 프로그래밍 언어 정환쌤 굳드 최고"

# 출력결과:
# 코딩
# 개발
# 파이썬
# 프로그래밍
# 언어
# 정환썜
# 굳드
# 최고

for word in input_text.split():
  print(f"#{word}")

def hash(text):
  hashtag = text.split()
  for word in hashtag:
    print(f"#{word}")

hash(input_text)

# => 반환된 값을 리스트로 만들기

# 출력결과:
# ["코딩", "개발", "파이썬", "프로그래밍", "언어", "정환쌤", "굳드", "최고"]

def hash(text):
  hashtag = text.split()
  list = []
  for word in hashtag:
    list.append(f"#{word}")
  return list

result = hash(input_text)
print(result)


