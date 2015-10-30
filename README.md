# P1: Movie Trailer Website
## Introduction

This is a set of python scripts that may be used to generate an HTML like the one provided in this repo.

Link to the generated HTML: https://rawgit.com/argx/fsnd-p1/master/fresh_tomatoes.html

## Example

### The main script `entertainment_center.py`
```python
import media
import fresh_tomatoes

# Movie's Class Constructor takes 5 required arguments and 1 sixth optional argument
# 1st: The Movie Title
# 2nd: The release Year
# 3rd: The Storyline
# 4th: The Poster Image URL
# 5th: The Trailer Youtube URL
# 6th: The Number of Oscar awards won (optional default = 0)

# Instantiating all the movies

movie1 = media.Movie(
    "The first Movie Title",
    "2009",
    "The Storyline",
    "http://url.to/poster-image.jpg",
    "https://www.youtube.com/watch?v=XXXXXXXXXXX")
    
# sixth argument is optional
# it specifies the number of oscar awards won
movie2 = media.Movie(
    "The second Movie Title",
    "2012",
    "The Storyline",
    "http://url.to/poster-image.jpg",
    "https://www.youtube.com/watch?v=XXXXXXXXXXX",
    5)

# The list with all the movies to display
movies = [ movie1, movie2 ]

# Generate the HTML file that displays all the movies info
# and open it in a new browser tab
fresh_tomatoes.open_movies_page(movies)

```

### Running the script

```
$ python entertainment_center.py
```

## References

https://github.com/adarsh0806/ud036_StarterCode

