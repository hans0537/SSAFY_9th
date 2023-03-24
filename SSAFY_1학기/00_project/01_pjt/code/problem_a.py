import json
from pprint import pprint


def movie_info(movie):
    dic = {}
    dic['id'] = movie.get('id')
    dic['title'] = movie.get('title')
    dic['poster_path'] = movie.get('poster_path')
    dic['vote_average'] = movie.get('vote_average')
    dic['overview'] = movie.get('overview')
    dic['genre_ids'] = movie.get('genre_ids')
    
    return dic


# 아래의 코드는 수정하지 않습니다.
if __name__ == '__main__':
    movie_json = open('data/movie.json', encoding='utf-8')
    movie_dict = json.load(movie_json)
    pprint(movie_info(movie_dict))
