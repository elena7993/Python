program_lan = {
  "js": "자바스크립트",
  "py": "python",
  "reacte": "리액트",
  "html": "Hyper Text Markup Language"
}

del program_lan["html"]
# =>딕셔너리 값을 삭제할 때
for i in program_lan:
  print(program_lan[i])