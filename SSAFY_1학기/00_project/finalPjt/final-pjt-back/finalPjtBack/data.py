import requests
import json


def get_movie_datas():
    total_data = []
    
    url = "https://api.themoviedb.org/3/genre/movie/list?language=ko"
    headers = {
    "accept": "application/json",
    "Authorization": "Bearer eyJhbGciOiJIUzI1NiJ9.eyJhdWQiOiIwYjU2OWZjNjEwNTVkYzZhNjA3M2JiOTNlYjgxYmNiMSIsInN1YiI6IjY0MWQ0NTBlMzQ0YThlMDA5YjBiMDE2ZiIsInNjb3BlcyI6WyJhcGlfcmVhZCJdLCJ2ZXJzaW9uIjoxfQ.bHKaUaJcO2JnSsD5myVc7n4CcFdrW6YE_879_00jYhw"
    }
    genre = requests.get(url,headers=headers).json()
    for gen in genre['genres']:
        fields = {
            'id':gen['id'],
            'name':gen['name']
        }
        data = {
            "model": "movies.genre",
            "fields": fields
        }
        total_data.append(data)
    # 1페이지부터 500페이지까지의 데이터를 가져옴.(popularmovie)
    for i in range(1,180):
        request_url = "https://api.themoviedb.org/3/movie/top_rated?language=ko-kr&page=" + str(i) + "&region=kr"
        headers = {
                    "accept": "application/json",
                    "Authorization": "Bearer eyJhbGciOiJIUzI1NiJ9.eyJhdWQiOiIwYjU2OWZjNjEwNTVkYzZhNjA3M2JiOTNlYjgxYmNiMSIsInN1YiI6IjY0MWQ0NTBlMzQ0YThlMDA5YjBiMDE2ZiIsInNjb3BlcyI6WyJhcGlfcmVhZCJdLCJ2ZXJzaW9uIjoxfQ.bHKaUaJcO2JnSsD5myVc7n4CcFdrW6YE_879_00jYhw"
                }
        movies = requests.get(request_url,headers=headers).json()
        for movie in movies['results']:
            if movie.get('release_date', ''):
                fields = {
                    'id':movie['id'],
                    'adult': movie['adult'],
                    'title': movie['title'],
                    'backdrop_path': movie['backdrop_path'],
                    'original_language': movie['original_language'],
                    'original_title': movie['original_title'],
                    'video': movie['video'],
                    'release_date': movie['release_date'],
                    'popularity': movie['popularity'],
                    'vote_count': movie['vote_count'],
                    'vote_average': movie['vote_average'],
                    'overview': movie['overview'],
                    'poster_path': movie['poster_path'],
                    'genre_ids': movie['genre_ids'],
                }
                
                data = {
                    "model": "movies.movie",
                    "fields": fields
                }

                total_data.append(data)
    # 상영중인 최신영화
    for i in range(1,5):
        request_url = "https://api.themoviedb.org/3/movie/now_playing?language=ko-kr&page=" + str(i) + "&region=kr"
        headers = {
                    "accept": "application/json",
                    "Authorization": "Bearer eyJhbGciOiJIUzI1NiJ9.eyJhdWQiOiIwYjU2OWZjNjEwNTVkYzZhNjA3M2JiOTNlYjgxYmNiMSIsInN1YiI6IjY0MWQ0NTBlMzQ0YThlMDA5YjBiMDE2ZiIsInNjb3BlcyI6WyJhcGlfcmVhZCJdLCJ2ZXJzaW9uIjoxfQ.bHKaUaJcO2JnSsD5myVc7n4CcFdrW6YE_879_00jYhw"
                }
        movies = requests.get(request_url,headers=headers).json()
        for movie in movies['results']:
            if movie.get('release_date', ''):
                fields = {
                    'id':movie['id'],
                    'adult': movie['adult'],
                    'title': movie['title'],
                    'backdrop_path': movie['backdrop_path'],
                    'original_language': movie['original_language'],
                    'original_title': movie['original_title'],
                    'video': movie['video'],
                    'release_date': movie['release_date'],
                    'popularity': movie['popularity'],
                    'vote_count': movie['vote_count'],
                    'vote_average': movie['vote_average'],
                    'overview': movie['overview'],
                    'poster_path': movie['poster_path'],
                    'genre_ids': movie['genre_ids'],
                }
                
                data = {
                    "model": "movies.movie",
                    "fields": fields
                }

                total_data.append(data)
    # 개봉예정작
    for i in range(1,2):
        request_url = "https://api.themoviedb.org/3/movie/upcoming?language=ko-kr&page=" + str(i) + "&region=kr"
        headers = {
                    "accept": "application/json",
                    "Authorization": "Bearer eyJhbGciOiJIUzI1NiJ9.eyJhdWQiOiIwYjU2OWZjNjEwNTVkYzZhNjA3M2JiOTNlYjgxYmNiMSIsInN1YiI6IjY0MWQ0NTBlMzQ0YThlMDA5YjBiMDE2ZiIsInNjb3BlcyI6WyJhcGlfcmVhZCJdLCJ2ZXJzaW9uIjoxfQ.bHKaUaJcO2JnSsD5myVc7n4CcFdrW6YE_879_00jYhw"
                }
        movies = requests.get(request_url,headers=headers).json()
        for movie in movies['results']:
            if movie.get('release_date', ''):
                fields = {
                    'id':movie['id'],
                    'adult': movie['adult'],
                    'title': movie['title'],
                    'backdrop_path': movie['backdrop_path'],
                    'original_language': movie['original_language'],
                    'original_title': movie['original_title'],
                    'video': movie['video'],
                    'release_date': movie['release_date'],
                    'popularity': movie['popularity'],
                    'vote_count': movie['vote_count'],
                    'vote_average': movie['vote_average'],
                    'overview': movie['overview'],
                    'poster_path': movie['poster_path'],
                    'genre_ids': movie['genre_ids'],
                }
                
                data = {
                    "model": "movies.movie",
                    "fields": fields
                }

                total_data.append(data)

    with open("movies/fixtures/movie_data.json", "w", encoding="utf-8") as w:
        json.dump(total_data, w, indent="\t", ensure_ascii=False)
        
def get_movie():
    total_data = []
    
    url = "https://api.themoviedb.org/3/genre/movie/list?language=ko"
    headers = {
    "accept": "application/json",
    "Authorization": "Bearer eyJhbGciOiJIUzI1NiJ9.eyJhdWQiOiIwYjU2OWZjNjEwNTVkYzZhNjA3M2JiOTNlYjgxYmNiMSIsInN1YiI6IjY0MWQ0NTBlMzQ0YThlMDA5YjBiMDE2ZiIsInNjb3BlcyI6WyJhcGlfcmVhZCJdLCJ2ZXJzaW9uIjoxfQ.bHKaUaJcO2JnSsD5myVc7n4CcFdrW6YE_879_00jYhw"
    }
    genre = requests.get(url,headers=headers).json()
    for gen in genre['genres']:
        fields = {
            'id':gen['id'],
            'name':gen['name']
        }
        data = {
            "model": "movies.genre",
            "fields": fields
        }
        total_data.append(data)
    # 1페이지부터 500페이지까지의 데이터를 가져옴.(popularmovie)
    for i in range(1,180):
        request_url = "https://api.themoviedb.org/3/movie/top_rated?language=ko-kr&page=" + str(i) + "&region=kr"
        headers = {
                    "accept": "application/json",
                    "Authorization": "Bearer eyJhbGciOiJIUzI1NiJ9.eyJhdWQiOiIwYjU2OWZjNjEwNTVkYzZhNjA3M2JiOTNlYjgxYmNiMSIsInN1YiI6IjY0MWQ0NTBlMzQ0YThlMDA5YjBiMDE2ZiIsInNjb3BlcyI6WyJhcGlfcmVhZCJdLCJ2ZXJzaW9uIjoxfQ.bHKaUaJcO2JnSsD5myVc7n4CcFdrW6YE_879_00jYhw"
                }
        movies = requests.get(request_url,headers=headers).json()
        for movie in movies['results']:
            if movie.get('release_date', ''):
                fields = {
                    'id':movie['id'],
                    'adult': movie['adult'],
                    'title': movie['title'],
                    'backdrop_path': movie['backdrop_path'],
                    'original_language': movie['original_language'],
                    'original_title': movie['original_title'],
                    'video': movie['video'],
                    'release_date': movie['release_date'],
                    'popularity': movie['popularity'],
                    'vote_count': movie['vote_count'],
                    'vote_average': movie['vote_average'],
                    'overview': movie['overview'],
                    'poster_path': movie['poster_path'],
                    'genre_ids': movie['genre_ids'],
                }
                
                data = {
                    "model": "movies.PopularMovie",
                    "fields": fields
                }

                total_data.append(data)
    # 상영중인 최신영화
    for i in range(1,5):
        request_url = "https://api.themoviedb.org/3/movie/now_playing?language=ko-kr&page=" + str(i) + "&region=kr"
        headers = {
                    "accept": "application/json",
                    "Authorization": "Bearer eyJhbGciOiJIUzI1NiJ9.eyJhdWQiOiIwYjU2OWZjNjEwNTVkYzZhNjA3M2JiOTNlYjgxYmNiMSIsInN1YiI6IjY0MWQ0NTBlMzQ0YThlMDA5YjBiMDE2ZiIsInNjb3BlcyI6WyJhcGlfcmVhZCJdLCJ2ZXJzaW9uIjoxfQ.bHKaUaJcO2JnSsD5myVc7n4CcFdrW6YE_879_00jYhw"
                }
        movies = requests.get(request_url,headers=headers).json()
        for movie in movies['results']:
            if movie.get('release_date', ''):
                fields = {
                    'id':movie['id'],
                    'adult': movie['adult'],
                    'title': movie['title'],
                    'backdrop_path': movie['backdrop_path'],
                    'original_language': movie['original_language'],
                    'original_title': movie['original_title'],
                    'video': movie['video'],
                    'release_date': movie['release_date'],
                    'popularity': movie['popularity'],
                    'vote_count': movie['vote_count'],
                    'vote_average': movie['vote_average'],
                    'overview': movie['overview'],
                    'poster_path': movie['poster_path'],
                    'genre_ids': movie['genre_ids'],
                }
                
                data = {
                    "model": "movies.NowMovie",
                    "fields": fields
                }

                total_data.append(data)
    # 개봉예정작
    for i in range(1,2):
        request_url = "https://api.themoviedb.org/3/movie/upcoming?language=ko-kr&page=" + str(i) + "&region=kr"
        headers = {
                    "accept": "application/json",
                    "Authorization": "Bearer eyJhbGciOiJIUzI1NiJ9.eyJhdWQiOiIwYjU2OWZjNjEwNTVkYzZhNjA3M2JiOTNlYjgxYmNiMSIsInN1YiI6IjY0MWQ0NTBlMzQ0YThlMDA5YjBiMDE2ZiIsInNjb3BlcyI6WyJhcGlfcmVhZCJdLCJ2ZXJzaW9uIjoxfQ.bHKaUaJcO2JnSsD5myVc7n4CcFdrW6YE_879_00jYhw"
                }
        movies = requests.get(request_url,headers=headers).json()
        for movie in movies['results']:
            if movie.get('release_date', ''):
                fields = {
                    'id':movie['id'],
                    'adult': movie['adult'],
                    'title': movie['title'],
                    'backdrop_path': movie['backdrop_path'],
                    'original_language': movie['original_language'],
                    'original_title': movie['original_title'],
                    'video': movie['video'],
                    'release_date': movie['release_date'],
                    'popularity': movie['popularity'],
                    'vote_count': movie['vote_count'],
                    'vote_average': movie['vote_average'],
                    'overview': movie['overview'],
                    'poster_path': movie['poster_path'],
                    'genre_ids': movie['genre_ids'],
                }
                
                data = {
                    "model": "movies.UpMovie",
                    "fields": fields
                }

                total_data.append(data)

    with open("movies/fixtures/movie_detail_data.json", "w", encoding="utf-8") as w:
        json.dump(total_data, w, indent="\t", ensure_ascii=False)

get_movie_datas()
get_movie()