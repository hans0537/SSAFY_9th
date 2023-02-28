'''
보수 => 보충해주는 수
n진법수 x가 있을때, 이 x에 더해서 n의 최소 제곱수가 될수 있도록
만드는 수를 x의 n의 보수

6에서 10의 최소 제곱수인 10으로 만들어 주는 수 => 4
4는 십진수 6의 10의 보수가 된다.

우리가 이걸 왜 쓰냐?
컴퓨터에서 음수를 표현하기 위해 보수를 사요한다.
컴퓨터는 사칙연산을 할때 사실 더하기(가산기)만 사용가능

뺄셈도 덧셈으로 계산
A - B = A + ( -B )
B의 보수를 구한 뒤에 더함

이진법에서
음수를 표현하기 위해서 비트를 모두 반대로 바꿈
1의 보수 => 어떤 수를 커다란 2의 거듭제곱수 -1(모든 비트의 숫자가 1)
에서 빼서 얻은 이진수

이진수 0101의 1의 보수 => 1111 - 0101 = 1010
    1111
-   0101
--------
    1010
'''