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



#     def deposit(self, amount)
#         self.balance += amount






class Account :
    def __init__(self, acc_id, name, balance) :
        self.acc_id = acc_id    # 계좌번호
        self.name = name        # 이름
        self.balance = balance  # 잔액

accounts = []

while True :
    print("-----Menu-----")
    print("1. 계좌 개설")
    print("2. 입금")
    print("3. 출금")
    print("4. 계좌번호 전체 출력")
    print("5. 프로그램 종료")

    choice = input("선택 > ")

    if choice == "1":
        print("\n--- 계좌 개설 ---")
        acc_id = input("계좌번호 입력: ")
        name = input("이름 입력: ")
        try:
            balance = int(input("초기 입금액 입력: "))
            new_acc = Account(acc_id, name, balance)
            accounts.append(new_acc)
            print(f"{name}님의 계좌가 성공적으로 개설되었습니다!")
        except ValueError:
            print("[오류] 초기 입금액은 숫자로만 입력해 주세요.")

    elif choice == "2":
        print("\n--- 입금 ---")
        acc_id = input("입금할 계좌번호: ")
        
        # 입력한 계좌번호와 일치하는 계좌 찾기
        target_acc = None
        for acc in accounts:
            if acc.acc_id == acc_id:
                target_acc = acc
                break

        if target_acc:
            try:
                amount = int(input("입금할 금액: "))
                if amount <= 0:
                    print("[오류] 입금 금액은 0원보다 커야 합니다.")
                else:
                    target_acc.balance += amount
                    print(f"[성공] {target_acc.name}님의 계좌에 {amount}원이 입금되었습니다. (현재 잔액: {target_acc.balance}원)")
            except ValueError:
                print("[오류] 금액은 숫자로만 입력해 주세요.")
        else:
            print("[오류] 존재하지 않는 계좌번호입니다.")

    elif choice == "3":
        print("\n--- 출금 ---")
        acc_id = input("출금할 계좌번호: ")
        
        target_acc = None
        for acc in accounts:
            if acc.acc_id == acc_id:
                target_acc = acc
                break

        if target_acc:
            try:
                amount = int(input("출금할 금액: "))
                if amount <= 0:
                    print("[오류] 출금 금액은 0원보다 커야 합니다.")
                elif amount > target_acc.balance:
                    print(f"[오류] 잔액이 부족합니다. (현재 잔액: {target_acc.balance}원)")
                else:
                    target_acc.balance -= amount
                    print(f"[성공] {target_acc.name}님의 계좌에서 {amount}원이 출금되었습니다. (현재 잔액: {target_acc.balance}원)")
            except ValueError:
                print("[오류] 금액은 숫자로만 입력해 주세요.")
        else:
            print("[오류] 존재하지 않는 계좌번호입니다.")

    elif choice == "4" :
        print("\n--- 전체 계좌 목록 ---")
        if not accounts:
            print("등록된 계좌가 없습니다.")
        else:
            for acc in accounts:
                print(f"계좌번호: {acc.acc_id} | 이름: {acc.name}  | 잔액 {acc.balance}원")

    elif choice == "5" :
        print("프로그램을 종료합니다.")
        break
    else :
        print("잘못 입력하셨습니다. 1~5 사이의 숫자를 입력해주세요.")