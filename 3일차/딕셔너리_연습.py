students = {
  "Rosy": 85,
  "Rebecca": 90,
  "Kal": 78,
}

def get_score(name):
  return students.get(name, "찾으시는 학생이 없습니다.")

def add_students(name, score):
  students[name] = score
  print(f"{name} 학생이 추가되었습니다.")

def remove_students(name):
  if name in students:
    del students[name]
    print(f"{name} 학생이 삭제되었습니다.")

add_students("Sam", 88)
remove_students("Kal")
print(get_score("Rebecca"))

