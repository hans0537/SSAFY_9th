dic = {
    "ZRO" : 0,
    "ONE" : 1,
    "TWO" : 2,
    "THR" : 3,
    "FOR" : 4,
    "FIV" : 5,
    "SIX" : 6,
    "SVN" : 7,
    "EGT" : 8,
    "NIN" : 9,
}
T = int(input())
for tc in range(1, T + 1):
    input()
    words = input().split()
    words.sort(key=lambda x:dic[x])
    print(f'#{tc}\n{" ".join(words)}')

