import requests

url = "https://api.agify.io/?name=minseok"
# 응답 받아와서 저장
# 응답은 JSON 형식이지만, 파이썬에서 사용하는 딕셔너리처럼 사용 가능!
response = requests.get(url).json()

print(response.get("age"))
print(response.get("name"))