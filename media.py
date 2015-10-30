import webbrowser

# The Movie Class
class Movie():

    # Constructor
    def __init__(self, movie_title, movie_year,movie_storyline, poster_image, 
        trailer_youtube, oscars_won = 0 ):
        
        # The Movie Title
        self.title = movie_title
        
        # The Year Published
        self.year = movie_year
        
        # The Movie Storyline
        self.storyline = movie_storyline
        
        # The URL to the Poster Image
        self.poster_image_url = poster_image
        
        # The Trailer Youtube URL
        self.trailer_youtube_url = trailer_youtube
        
        # Number of oscars the Movie won
        self.oscars_won = oscars_won
        
