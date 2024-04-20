from movie import Movie


def movie_count(movies:list[Movie], director):
    return len([
        movie 
        for movie in movies
        if movie.director == director
    ])
    
def longest_movie_runtime_with_actor(movies:list[Movie], actor):
    return max([
        movie.runtime
        for movie in movies
        if actor in movie.actors
    ])
    
def has_director_made_genre(movies: list[Movie], director, genre):
    return any([
        movie
        for movie in movies
        if movie.director == director
        if genre in movie.genres
    ])
  
    
def is_prime(n):
    return n > 1 and all([
        n % k != 0
        for k in range(2, n)
    ])

def is_increasing(ns):
    return all([
        ns[i] <= ns[i+1]
        for i in range(len(ns) - 1)
    ])

def count_matching(xs, ys):
    return len([
        ...
        for x, y in zip(xs, ys)
        if x == y
    ])
    
def weighted_sum(ns, weights):
    return sum([
        n * weight 
        for n, weight in zip(ns, weights)
    ])
    

def alternating_caps(string:str):
    return "".join([
        char.upper() 
        if i % 2 == 0
        else char.lower()
        for i, char in enumerate(string)
    ])
    
    
def find_repeated_words(sentence:str):
    import re
    
    words = [
        word.lower()
        for word in re.findall(r'\w+', sentence)
        ]
    
    return {
        word1
        for word1, word2 in zip(words, words[1:])
        if word1 == word2
    }