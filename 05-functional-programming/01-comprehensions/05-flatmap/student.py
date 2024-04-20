from movie import Movie
from util import Card


def genres(movies:list[Movie]):
    return {
        genre
        for movie in movies
        for genre in movie.genres
    }
    
    
def actors(movies:list[Movie]):
    return {
        actor
        for movie in movies
        for actor in movie.actors
    }
    

def repeat_consecutive(xs, n):
    return [
        x
        for x in xs
        for _ in range(n)
    ]
    
    
def repeat_alternating(xs, n):
    return [
        x
        for _ in range(n)
        for x in xs
    ]
    
    
def cards(values, suits):
    return {
        Card(value, suit)
        for suit in suits
        for value in values
    }