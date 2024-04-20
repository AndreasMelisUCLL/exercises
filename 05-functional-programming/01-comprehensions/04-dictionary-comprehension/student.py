from movie import Movie


def title_to_director(movies:list[Movie]):
    return {
        movie.title: movie.director
        for movie in movies
    }
    
def director_to_titles(movies:list[Movie]):
    return {
        director: [
            movie.title
            for movie in movies
            if movie.director == director
        ]
        for director in {
            movie.director
            for movie in movies
        }
    }