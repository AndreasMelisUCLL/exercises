from movie import Movie


def titles(movies:list[Movie]) -> list[str]:
    return [movie.title for movie in movies]

def titles_and_years(movies:list[Movie]) -> list[(str, int)]:
    return [(movie.title, movie.year) for movie in movies]

def titles_and_actor_counts(movies:list[Movie]) -> list[(str, int)]:
    return [(movie.title, len(movie.actors)) for movie in movies]

def titles_and_actor_counts(movies:list[Movie]) -> list[(str, int)]:
    return [(movie.title, len(movie.actors)) for movie in movies]


def reverse_words(sentence:str) -> str:
    return " ".join([word[::-1] for word in sentence.split()])