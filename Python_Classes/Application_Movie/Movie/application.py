# This is an application we are creating using OOPs

class Movie:
    """ This is movie class and all movie details"""

    def __init__(self, movie_name, actor_name, actress_name):
        self.movie_name = movie_name
        self.actor_name = actor_name
        self.actress_name = actress_name # 여배우

    def movie_details(self):
        print("Movie name is ", self.movie_name)
        print("Actor name is ", self.actor_name)
        print("Actress name is ", self.actress_name)







