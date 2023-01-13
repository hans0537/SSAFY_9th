import random

dic = {1 : "가위", 2 : "바위", 3 : "보"}

def game(a, com):
    if (a == 1 and com == 3) or (a == 2 and com == 1) or (a == 3 and com == 2):
        print(f"com : {dic[com]}  |  {dic[a]} : 나")
        print("WIN!!! 쨔쓰~")
        return 1
    elif (a == 3 and com == 1) or (a == 1 and com == 2) or (a == 2 and com == 3):
        print(f"com : {dic[com]}  |  {dic[a]} : 나")
        print("LOSEㅠㅠ")
        return 0
    elif (a == 3 and com == 3) or (a == 1 and com == 1) or (a == 2 and com == 2):
        print(f"com : {dic[com]}  |  {dic[a]} : 나")
        print("비김!! 다시")
        return -1

while True:
    print("==================")
    print("가위 바위 보 게임!!!")
    print("1. 게임하기 \n2. 종료")
    sel = int(input("선택: "))
    if sel == 1:
        while True:
            print("=================")
            print("1. 일반게임\n2. 단판\n3. 삼세판\n4. 묵찌빠\n0. 뒤로")

            sel1 = int(input("선택: "))
            
            if sel1 == 1:
                while True:
                    com = random.choice(range(1,4))
                    print("=================")
                    a = int(input("가위(1) 바위(2) 보(3) 종료(0) 선택: "))
                    check = 0

                    if a == 0:
                        break
                    elif a < 0 or a > 3:
                        print("1,2,3,0 만 선택하세요!!")
                    else:
                        check = game(a, com)

            elif sel1 == 2:
                check = -1
                while check == -1:
                    com = random.choice(range(1,4))
                    print("=================")
                    a = int(input("가위(1) 바위(2) 보(3) 선택: "))

                    if a < 0 or a > 3:
                        print("1,2,3 만 선택하세요!!")
                    else:
                        check = game(a, com)
            elif sel1 == 3:
                a_win = 0
                com_win = 0

                while a_win < 2 and com_win < 2:
                    check = -1  
                    
                    while check == -1:
                        print("=================")
                        a = int(input("가위(1) 바위(2) 보(3) 선택: "))
                        com = random.choice(range(1,4))

                        if a < 0 or a > 3:
                            print("1,2,3 만 선택하세요!!")
                        else:
                            check = game(a, com)
                    
                    if check == 1:
                        a_win += 1
                    elif check == 0:
                        com_win += 1

                    print(f"[나 : {a_win} | com : {com_win}]")
                
                if a_win > com_win:
                    print("나 승리!!!!")
                else:
                    print("com 승리!!!!")
            elif sel1 == 4:
                check = -1
                com = 0
                a = 0
                while check == -1:
                    com = random.choice(range(1,4))
                    print("=================")
                    a = int(input("가위(1) 바위(2) 보(3) 선택: "))
                    
                    if a < 0 or a > 3:
                            print("1,2,3 만 선택하세요!!")
                    else:
                        check = game(a, com)
                print("묵찌바 start!!!")

                while True:
                    print("=================") 
                    print(f"com : {dic[com]}  |  {dic[a]} : 나")
                    if check == 1:
                        a = int(input("[내턴]가위(1) 바위(2) 보(3) 선택: "))
                        com = random.choice(range(1,4))
                        if (a == 1 and com == 3) or (a == 2 and com == 1) or (a == 3 and com == 2):
                            print(f"com : {dic[com]}  |  {dic[a]} : 나")
                            check = 1
                        elif (a == 3 and com == 1) or (a == 1 and com == 2) or (a == 2 and com == 3):
                            print(f"com : {dic[com]}  |  {dic[a]} : 나")
                            check = 0
                        elif (a == 3 and com == 3) or (a == 1 and com == 1) or (a == 2 and com == 2):
                            print(f"com : {dic[com]}  |  {dic[a]} : 나")
                            print("묵찌빠 승리!!!")
                            check = -1
                            break
                    elif check == 0:
                        a = int(input("[com턴]가위(1) 바위(2) 보(3) 선택: "))
                        com = random.choice(range(1,4))
                        if (a == 1 and com == 3) or (a == 2 and com == 1) or (a == 3 and com == 2):
                            print(f"com : {dic[com]}  |  {dic[a]} : 나")
                            check = 1
                        elif (a == 3 and com == 1) or (a == 1 and com == 2) or (a == 2 and com == 3):
                            print(f"com : {dic[com]}  |  {dic[a]} : 나")
                            check = 0
                        elif (a == 3 and com == 3) or (a == 1 and com == 1) or (a == 2 and com == 2):
                            print(f"com : {dic[com]}  |  {dic[a]} : 나")
                            print("묵찌빠 패배ㅠㅠ")
                            check = -1
                            break
            elif sel1 == 0:
                break
            else:
                print("1,2,3,4,0 만 선택하세요!")
    elif sel == 2:
        print("프로그램 종료")
        break
    else:
        print("1, 2번만 선택하세요")