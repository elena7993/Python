program_lan = {
  "js": "자바스크립트",
  "py": "python",
  "reacte": "리액트",
  "html": "Hyper Text Markup Language"
}

program_lan["node"] = "Node Js"
program_lan["django"] = "장고!"
# =>딕셔너리에 값을 추가할 수 있음
# =>대괄호 안이 key, 그 다음에 value

# print(program_lan["node"])

for i in program_lan:
  print(program_lan[i])