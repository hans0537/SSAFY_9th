import random

def making_card_list() -> list:
	card_list = []

	for shape in ["spade", "heart", "diamond", "clover"]:

		for number in ["A", 2, 3, 4, 5, 6, 7, 8, 9, 10, "J", "Q", "K"]:

			card_list.append((shape, number))

	return card_list

trump_card_list = making_card_list()

# 카드 섞기
random.shuffle(trump_card_list)

def numWin(p1, p2):
	# 알파벳 우선순위 딕셔너리
	dic = {
		'J' : 11,
		'Q' : 12,
		'K' : 13,
		'A' : 14
	}

	# 임시 변수에 저상후 
	p1 = p1
	p2 = p2

	# 만약 각 플레이어가 알파벳이면 숫자로 변환
	if type(p1) == str:
		p1 = dic.get(p1)
	if type(p2) == str:
		p2 = dic.get(p2)

	# 1 p1승, 2 p2승, 0 같다
	if p1 > p2:
		return 1
	elif p2 > p1:
		return 2
	else:
		return 0

def shapeWin(p1, p2):
	# 모양 우선순위 딕셔너리
	dic = {
		'spade' : 4,
		'diamond' : 3,
		'heart' : 2,
		'clover' : 1
	}
	
	if dic.get(p1) > dic.get(p2):
		return 1
	else:
		return 2

p1_win = 0
p2_win = 0
while True:
	if p1_win == 6:
		print(f'{p1_win}:{p2_win} finally player1 win')
		break
	
	if p2_win == 6:
		print(f'{p1_win}:{p2_win} finally player1 win')
		break

	player_1 = trump_card_list.pop(0)
	player_2 = trump_card_list.pop(0)

	if numWin(player_1[1], player_2[1]) == 1:
		p1_win += 1
		print(f'{player_1} {player_2} player1 win!')
	elif numWin(player_1[1], player_2[1]) == 2:
		p2_win += 1
		print(f'{player_1} {player_2} player_2 win!')
	else:
		if shapeWin(player_1[0], player_2[0]) == 1:
			p1_win += 1
			print(f'{player_1} {player_2} player1 win!')
		else:
			p2_win += 1
			print(f'{player_1} {player_2} player_2 win!')
