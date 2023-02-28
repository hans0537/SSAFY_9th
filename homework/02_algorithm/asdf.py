bit = ''
s = '196EBC5A316C578'
N = len(s)
tmp = int(s, 16)
for k in range(N * 4 - 1, -1, -1):
    bit += '1' if tmp & (1 << k) else '0'

# 오른쪽에서 1전까지 0 제거
bit = bit.rstrip('0')