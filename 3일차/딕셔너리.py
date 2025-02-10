# *딕셔너리
# => 리스트처럼 요소를 저장하지만 키와 값으로 구분되어 사용됨
# => 값을 불러올 땐 대괄호를 이용하여 불러옴

# dict = {
#   "num_1": 10,
#   "num_2": 20,
#   "num_3": 30
# }

# print(dict["num_1"])
# print(dict["num_3"])
# print(dict["num_2"] + dict["num_3"])

user = {
  "username": "Elena",
  "prifile_img": "my_face.jpg",
  "name": "hyunah Lee",
  "email": "elena@gmail.com",
  "follow": ["front_end", "back_end", "date_base"]
}

print(f"아이디: {user["username"]}")
print(f"팔로우: {user["follow"]}")
print(f"팔로우: {user["follow"][1]}")

for followers in user["follow"]:
  print(f"팔로우 유저: {followers}")
