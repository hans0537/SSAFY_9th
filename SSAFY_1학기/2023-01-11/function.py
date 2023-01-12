import requests

# url = "https://api.agify.io/?name=sungjoo"

# print(requests.get(url).json())
# requests.get(url).json()
# url = "https://www.dhlottery.co.kr/common.do?method=getLottoNumber&drwNo=1021"

# print(requests.get(url).json())

# response = requests.get(url).json()
# for i in range(1, 7):
#     num = f"drwtNo{i}"
#     print(response.get(num))

num = int(input("가져올 회원 수: "))

url = f"https://random-data-api.com/api/v2/users?size={num}"
response = requests.get(url).json()

j = 1
for i in response:
    print(f"[{j}] firstname : {i.get('first_name')}, lastname : {i.get('last_name')}, username : {i.get('username')}")
    j+=1