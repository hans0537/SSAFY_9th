import json


def dec_movies(movies):
    # 12 월 영화 리스트 선언
    dec_list = []
    
    for i in movies:
        
        # 각 영화의 id값.json 파일을 로드 
        movie = open('data/movies/'+ str(i.get('id')) + '.json', encoding='utf-8')
        movie_detail = json.load(movie)
        
        # 날짜 문자열 슬라이싱
        if movie_detail.get('release_date')[5:7] == '12':
            dec_list.append(movie_detail.get('title'))

    return dec_list
        

# 아래의 코드는 수정하지 않습니다.
if __name__ == '__main__':
    movies_json = open('data/movies.json', encoding='utf-8')
    movies_list = json.load(movies_json)
    
    print(dec_movies(movies_list))
