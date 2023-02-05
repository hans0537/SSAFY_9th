import requests

url = "https://random-data-api.com/api/v2/users?size=10"

# 임의의 사용자 정보 10명 가져오기
# 요청은 한번만 보낼수 있다.

response = requests.get(url).json()

# 사용자 10명의 username 을 출력해보자.
for user in response:
    print(user.get("username"))