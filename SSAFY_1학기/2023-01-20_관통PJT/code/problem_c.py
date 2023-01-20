import json
from pprint import pprint


def movie_info(movies, genres):
    infoList = []
    
    for i in movies:
        dic = {}
        dic['id'] = i.get('id')
        dic['title'] = i.get('title')
        dic['poster_path'] = i.get('poster_path')
        dic['vote_average'] = i.get('vote_average')
        dic['overview'] = i.get('overview')
        dic['genre_ids'] = i.get('genre_ids')

        # 장르 이름 리스트 생성
        gen_names = []
        for i in dic.get('genre_ids'):
            for j in genres:
                if j.get('id') == i:
                    gen_names.append(j.get('name'))
        
        # genre_ids 의 밸류를 장르 이름 리스트로 변경
        dic['genre_ids'] = gen_names
        # dic 딕셔너리 안에 genre_ids => genre_names로 키명 변경
        dic['genre_names'] = dic.pop('genre_ids')

        infoList.append(dic)
        
    return infoList
        
# 아래의 코드는 수정하지 않습니다.
if __name__ == '__main__':
    movies_json = open('data/movies.json', encoding='utf-8')
    movies_list = json.load(movies_json)

    genres_json = open('data/genres.json', encoding='utf-8')
    genres_list = json.load(genres_json)

    pprint(movie_info(movies_list, genres_list))
