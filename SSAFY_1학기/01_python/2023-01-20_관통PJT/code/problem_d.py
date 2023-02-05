import json


def max_revenue(movies):

    # 키를 영화 제목, 밸류를 revenue 저장할 딕셔너리 생성
    dic = {}
    
    for i in movies:
        
        # 각 영화의 id값.json 파일을 로드 
        movie = open('data/movies/'+ str(i.get('id')) + '.json', encoding='utf-8')
        movie_detail = json.load(movie)
        
        # 각 영화의 상세 파일에서 reveneue 값을 딕셔너리에 저장
        dic[i.get('title')] = movie_detail.get('revenue')

    # 딕셔너리 value 최대값의 키를 리턴
    return max(dic, key=dic.get)
        
# 아래의 코드는 수정하지 않습니다.
if __name__ == '__main__':
    movies_json = open('data/movies.json', encoding='utf-8')
    movies_list = json.load(movies_json)
    
    print(max_revenue(movies_list))
