T = int(input())
for tc in range(1, T + 1):
    n = int(input())
    divs = [2,3,5,7,11]
    cnts = [0] * len(divs)

    for i in range(len(divs)):
        while n % divs[i] == 0:
            cnts[i] += 1
            n //= divs[i]

    print(f"#{tc}", *cnts)
