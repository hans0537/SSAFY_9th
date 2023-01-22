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

print(trump_card_list)

print(trump_card_list.pop(0))
print(trump_card_list)
p1 = 0
p2 = 0

while p1<7 and p2<7:
	player_1 = trump_card_list.pop(0)
	player_2 = trump_card_list.pop(0)

	