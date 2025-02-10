country = {

}

country["ko"] = "한국"
country["en"] = "영어"
country["jp"] = "일본"
country["eu"] = "유럽"

del country["eu"]

for i in country:
  print(country[i])