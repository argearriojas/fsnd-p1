"""Media Library for Fresh Tomatoes

This module contains the class Movie that is to be used by the Fresh Tomatoes
Project.
"""
import webbrowser


# The Movie Class
class Movie():

    # Constructor
    def __init__(self, movie_title, movie_year, movie_storyline, poster_image,
        	     trailer_youtube, oscars_won=0):
        """Constructor function
        Initializes the attributes for the instance
        inputs:
            :movie_title: The Movie Title
            :movie_year: The Year Released
            :movie_storyline: The Movie Storyline
            :poster_image: The URL to the Poster Image
            :trailer_youtube: The Trailer Youtube URL
            :oscars_won: Number of oscars the Movie won
        """
        self.title = movie_title
        self.year = movie_year
        self.storyline = movie_storyline
        self.poster_image_url = poster_image
        self.trailer_youtube_url = trailer_youtube
        self.oscars_won = oscars_won
