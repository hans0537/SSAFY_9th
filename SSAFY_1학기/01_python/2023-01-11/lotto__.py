import requests

# 요청을 보낼 주소 + 회차 번호 알려주기
url = "https://www.dhlottery.co.kr/common.do?method=getLottoNumber&drwNo=1021"

# 응답 받아오기
response = requests.get(url).json()

for i in range(1,7):
    num = f"drwtNo{i}"
    print(response.get(num))