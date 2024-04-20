from movie import Movie


def movies_from_year(movies:list[Movie], year:int):
    return [
        movie.title
        for movie in movies 
        if movie.year == year
    ]
    
def movies_with_actor(movies:list[Movie], actor:str):
    return [
        movie.title
        for movie in movies
        if actor in movie.actors
    ]
    
def divisors(n:int):
    return [
        k
        for k in range(1, n+1)
        if n % k == 0
    ]