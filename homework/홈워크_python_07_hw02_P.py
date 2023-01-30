# Collatz 클래스 활용
class Collatz:
    # 몇번 반복하는지 저장할 클래스 변수 선언
    cnt = 0

    def __init__(self, num):
        # 생성자를 이용하여 해당 번호를 인스턴스.num에 저장후
        # cnt 0으로 초기화
        Collatz.cnt = 0
        self.num = num
    
    # 클래스내에 인스턴스 재귀 메서드 활용
    def run(self):

        # 종료 조건1
        if self.num == 1:
            return Collatz.cnt
        # 종료 조건2
        if Collatz.cnt > 500:
            return -1
        
        # 짝수일경우
        if self.num % 2:
            self.num = self.num * 3 + 1
            Collatz.cnt += 1
            return self.run()
        # 홀수일 경우
        else:
            self.num = self.num // 2
            Collatz.cnt += 1
            return self.run()

# 클래스를 호출할 함수 생성     
def collatz(n):
    return Collatz(n).run()

print(collatz(6))  # => 8
print(collatz(16))  # => 4
print(collatz(27))  # => 111
print(collatz(626331))  # => -1
