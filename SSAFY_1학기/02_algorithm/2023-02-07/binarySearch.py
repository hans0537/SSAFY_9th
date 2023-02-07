def binary_search(arr, n, key):
    # 검색 볌위 지정
    # 시작, 끝
    start = 0
    end = n - 1

    while start <= end:
        # 가운데를 선택
        mid = (start + end) // 2

        # 가운데에 내가 찾는 게 있다
        if arr[mid] == key:
           # 검색 성공
            print('find')
            return mid
        # 가운데 값이 내가 찾고 있는 값보다 크다
        elif arr[mid] > key:
            # 검색 범위를 재지정
            # 오른쪽은 더이상 살펴볼 필요가 없다 => 뒤는 어차피 나보다 큰 애들만 있을거니까
            # 검색의 끝 범위를 가운데로 땡겨온다.
            end = mid - 1
        # 가운데 값이 내가 찾고 있는 값보다 작다
        else:
            # 검색 범위를 재지정
            # 왼쪽은 더이상 살펴볼 필요가 없다 => 앞은 어차피 나보다 작은 애들만 있을거니까
            # 검색의 시작 범위를 가운데로 땡겨온다.
            start = mid + 1
    print('cant find')
    return -1

arr = [2, 3, 5, 7, 8, 16, 77]
n = len(arr)
print(binary_search(arr, n, 16))