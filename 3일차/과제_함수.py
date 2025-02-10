# *문제
# =>교통카드 프로그램 제작
# =>어린이, 일반 카드로 분류
# =>어린이 요금은 500원, 어른 요금은 1300dnjs
# =>매개변수에 어린이 또는 일반, 10000원(카드요금)
# =>잔액추가가

# 예시)
# =>어린이를 매개변수로 입력시 출력결과
# =>어린이입니다, 500원 차감되었습니다

def transit_card(card_type, balance=10000):
  child_fee = 500
  adult_fee = 1300

  if card_type == "어린이":
    balance -= child_fee
    print(f"어린이군요! {child_fee}원 차감되었습니다🧸")
  elif card_type == "일반":
    balance -= adult_fee
    print(f"일반이군요! {adult_fee}원 차감되었습니다😁")
  else:
    print("해당 카드 유형은 존재하지 않습니다. 다시 입력하세요😵")
    return balance

  print(f"남은 잔액: {balance}원")
  return balance

# transit_card("일반")
# transit_card("어린이")

balance = 10000
# =>기본값은 첫 함수 호출시에만 사용되므로 balance를 함수외부에 따로 설정해줘야 함

balance = transit_card("어린이", balance)
balance = transit_card("일반", balance)
balance = transit_card("일반", balance)

