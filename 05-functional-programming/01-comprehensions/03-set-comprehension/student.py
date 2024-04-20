from movie import Movie

def directors(movies:list[Movie]):
    return {
        movie.director
        for movie in movies 
    }
    
def common_elements(xs, ys):
    return {
        x
        for x in xs
        if x in ys 
    }