'''
4
124783
667767
054060
101123
'''

def checkb(lst):
    cnt = 0

    for i in (0, 3):
        if lst[i] == lst[i + 1] == lst[i + 2] or (lst[i + 1] == lst[i] + 1 and lst[i + 2] == lst[i + 1] + 1):
            cnt += 1

    if cnt == 2:
        return True
    return False

# 모든 순열 조합을 찾아 baby gin 판별
def dfs(cnt, perm):
    global flag
    if cnt == 6:
        if checkb(perm):
            flag = True
        return

    for i in range(6):
        if not v[i]:
            v[i] = 1
            dfs(cnt + 1, perm + [nums[i]])
            v[i] = 0

T = int(input())
for tc in range(1, T + 1):
    nums = list(map(int, input()))
    v = [0] * 6
    flag = False
    dfs(0, [])
    if flag:
        print('#{} Baby-Gin!!'.format(tc))
    else:
        print('#{} Fail!!'.format(tc))
