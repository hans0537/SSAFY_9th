import json
from pprint import pprint


def movie_info(movie, genres):
    dic = {}
    dic['id'] = movie.get('id')
    dic['title'] = movie.get('title')
    dic['poster_path'] = movie.get('poster_path')
    dic['vote_average'] = movie.get('vote_average')
    dic['overview'] = movie.get('overview')
    dic['genre_ids'] = movie.get('genre_ids')

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
    
    return dic

# 아래의 코드는 수정하지 않습니다.
if __name__ == '__main__':
    movie_json = open('data/movie.json', encoding='utf-8')
    movie = json.load(movie_json)

    genres_json = open('data/genres.json', encoding='utf-8')
    genres_list = json.load(genres_json)

    pprint(movie_info(movie, genres_list))
