#!/usr/local/bin/python3

# Fetch and sort the movie names filtered by a title from
# https://jsonmock.hackerrank.com/api/movies/search?Title=substr

import requests


def get_movies(url, page_num):
    url = url + '&page={}'.format(page_num)
    res = requests.get(url, verify=False)
    res.raise_for_status()

    data = res.json()
    return [movie['Title'] for movie in data['data']]


def get_movie_titles(substring):
    url = 'https://jsonmock.hackerrank.com/api/movies/search?Title={}'.format(substring)
    res = requests.get(url, verify=False)
    res.raise_for_status()

    data = res.json()
    movie_titles = []
    for i in range(data['total_pages']):
        movie_titles += get_movies(url, i + 1)
    return sorted(movie_titles)

print(get_movie_titles('world'))

