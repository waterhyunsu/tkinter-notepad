# 다양한 기능이 요구되는 프로그램을 작성할 때

# 1. 바로 코드부터 작성하고보는건 좋지 않음
# 2. 논리 흐름을 정리한다.
#     - 종이에 작성하던, 텍스트 문서로 작성해보던, 도식화를 하던
# 3. 정리된 내용을 코드로 옮긴다.




# ## 실습 과제 3: 파이썬 클래스 도전문제

# 다음과 같은 실행 결과가 나타나는 파이썬 프로그램을 만듭니다. 
# 다음 사항을 반드시 적용하여 코드를 작성해주세요.

# - 클래스 하나 이상 정의하기
# - 입력 함수 사용하기
# - 예외 처리 구문 하나 이상 사용하기

# 계좌개설, 입금, 출금, 계좌번호 전체 출력, 프로그램 종료… 총 다섯 개의 기능 항목이 있습니다. 
# 기능을 하나 완성할 때마다 커밋을 추가할 것을 권장합니다.


# class Account :
#     def __init__(self, acc_id, name, balance)
#         self.acc_id = acc_id    # 계좌번호
#         self.name = name        # 이름
#         self.balance = balance  # 잔액

#     def deposit(self, amount)
#         self.balance += amount









while True :
    print("-----Menu-----")
    print("1. 계좌 개설")
    print("2. 입금")
    print("3. 출금")
    print("4. 계좌번호 전체 출력")
    print("5. 프로그램 종료")

    choice = input("선택 > ")

    if choice == "1" :
        print("1번 계좌개설 선택")
    elif choice == "2" :
        print("2번 입금 선택")
    elif choice == "3" :
        print("3번 출금 선택")
    elif choice == "4" :
        print("4번 계좌번호 전체 출력 선택")
    elif choice == "5" :
        print("프로그램을 종료합니다.")
        break
    else :
        print("잘못 입력하셨습니다. 1~5 사이의 숫자를 입력해주세요.")