# 최대 100개의 key
# 최대힙

def enq(n):
    global last
    last += 1   # 완전 이진트리에 마지막 정점을 추가하고
    heap[last] = n  # 마지막 정점에 입력값 저장
    # 부모가 있고, 부모 > 자식 => 조건 검사
    c = last
    p = c // 2

    while p > 0 and heap[p] < heap[c]:
        heap[p], heap[c] = heap[c], heap[p]
        c = p       # 옮긴 자리의 부모와 또 비교를 하기 위해
        p = c // 2

    return

def deq():
    global last
    tmp = heap[1]   # 루트 임시 저장
    # 마지막 정점의 값을 루트로 이동
    heap[1] = heap[last]
    last -= 1   # 마지막 정점 삭제
    p = 1
    c = p * 2   # 왼쪽 자식노드 번호
    while c <= last:    # 자식이 하나 이상 있으면
        if c + 1 <= last and heap[c] < heap[c + 1]:   # 근데 오른쪽 자식도 있고 오른쪽 자식의 값이 더 크면?
            c += 1                                    # 비교대상을 오른쪽 자식으로 변경
        if heap[c] > heap[p]:    # 비교대상인 자식의 값이 부모보다 크면
            heap[c], heap[p] = heap[p], heap[c]
            p = c
            c = p * 2

    return tmp



heap = [0] * 101  # 완전이진트리 1번 - 100버 인덱스 준비
last = 0  # 완전이진트리의 마지막 정점 번호
enq(5)
print(heap[1])
print(heap[:6])
enq(15)
print(heap[1])
print(heap[:6])
enq(8)
print(heap[1])
print(heap[:6])
enq(2)
print(heap[1])
print(heap[:6])
enq(20)
print(heap[1])
print(heap[:6])
