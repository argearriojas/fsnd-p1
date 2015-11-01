import webbrowser
import os
import re


# Styles and scripting for the page
main_page_head = '''
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="utf-8">
    <title>Fresh Tomatoes!</title>

    <!-- Bootstrap 3 -->
    <link rel="stylesheet" href="https://netdna.bootstrapcdn.com/bootstrap/3.1.0/css/bootstrap.min.css">
    <link rel="stylesheet" href="https://netdna.bootstrapcdn.com/bootstrap/3.1.0/css/bootstrap-theme.min.css">
    <script src="http://code.jquery.com/jquery-1.10.1.min.js"></script>
    <script src="https://netdna.bootstrapcdn.com/bootstrap/3.1.0/js/bootstrap.min.js"></script>
    <style type="text/css" media="screen">
        body {
            padding-top: 80px;
        }
        #trailer .modal-dialog {
            margin-top: 200px;
            width: 640px;
            height: 480px;
        }
        .hanging-close {
            position: absolute;
            top: -12px;
            right: -12px;
            z-index: 9001;
        }
        #trailer-video {
            width: 100%;
            height: 100%;
        }
        .movie-tile {
            margin-bottom: 20px;
            padding-top: 20px;
            min-height: 495px;
            perspective: 1500px;
            border-radius: 20px;
            transition: background-color .4s 1s ease-out;
        }
        .movie-tile:hover {
            transition-delay: 0s;
            background-color: #EEE;
            cursor: pointer;
        }
        .movie-tile .cover-img {
            transition: all .6s 1s ease-in-out;
            transform-origin: left;
            position: relative;
        }
        .movie-tile:hover .cover-img {
            transition-duration: .3s;
            transition-delay: 0s;
            transform: rotateY(-100deg);
        }
        .diptic {
            position: relative;
            width: 220px;
            margin-left: auto;
            margin-right: auto;
            background-image: 
                url(http://digital.films.com/images/animated_loading_icon.gif);
            background-position: center;
            background-repeat: no-repeat;
        }
        .storyline-container {
            position: absolute;
            left: 0;
            top: 0;
            text-align: left;
            padding: 25px;
        }
        .trailer-hint {
            position: absolute;
            right: 5px;
            top: 5px;
        }
        .awards {
            position: absolute;
            left: 35px;
            bottom: 5px;
        }
        .awards img{
            margin-right: 5px;
        }
        .scale-media {
            padding-bottom: 56.25%;
            position: relative;
        }
        .scale-media iframe {
            border: none;
            height: 100%;
            position: absolute;
            width: 100%;
            left: 0;
            top: 0;
            background-color: white;
        }
    </style>
    <script type="text/javascript" charset="utf-8">
        // Hide some elements until the image that covers then is loaded
        $('.cover-img, .storyline-container, .awards, .trailer-hint')
            .css("opacity","0");
        // Show hidden elements after image is loaded
        $('.cover-img').load(function(){
            $(this).animate({opacity: 1});
            $(this).siblings().animate({opacity: 1});
            $(this).parent().css('background-image','');
        });
        // Pause the video when the modal is closed
        $(document).on('click', '.hanging-close, .modal-backdrop, .modal', function (event) {
            // Remove the src so the player itself gets removed, as this is the only
            // reliable way to ensure the video stops playing in IE
            $("#trailer-video-container").empty();
        });
        // Start playing the video whenever the trailer modal is opened
        $(document).on('click', '.movie-tile', function (event) {
            var trailerYouTubeId = $(this).attr('data-trailer-youtube-id')
            var sourceUrl = 'http://www.youtube.com/embed/' + trailerYouTubeId + '?autoplay=1&html5=1';
            $("#trailer-video-container").empty().append($("<iframe></iframe>", {
              'id': 'trailer-video',
              'type': 'text-html',
              'src': sourceUrl,
              'frameborder': 0
            }));
        });
        // Animate in the movies when the page loads
        $(document).ready(function () {
          $('.movie-tile').hide().first().show("fast", function showNext() {
            $(this).next("div").show("fast", showNext);
          });
        });
        // Make sure everything is visible after full document is loaded        
        $(window).load(function () {
            $('.cover-img, .storyline-container, .awards, .trailer-hint')
                .css("opacity","1");
            $('.diptic').css('background-image','');
        });
    </script>
</head>
'''


# The main page layout and title bar
main_page_content = '''
  <body>
    <!-- Trailer Video Modal -->
    <div class="modal" id="trailer">
      <div class="modal-dialog">
        <div class="modal-content">
          <a href="#" class="hanging-close" data-dismiss="modal" aria-hidden="true">
            <img src="https://lh5.ggpht.com/v4-628SilF0HtHuHdu5EzxD7WRqOrrTIDi_MhEG6_qkNtUK5Wg7KPkofp_VJoF7RS2LhxwEFCO1ICHZlc-o_=s0#w=24&h=24"/>
          </a>
          <div class="scale-media" id="trailer-video-container">
          </div>
        </div>
      </div>
    </div>

    <!-- Main Page Content -->
    <div class="container">
      <div class="navbar navbar-inverse navbar-fixed-top" role="navigation">
        <div class="container">
          <div class="navbar-header">
            <a class="navbar-brand" href="#">Fresh Tomatoes Movie Trailers</a>
          </div>
        </div>
      </div>
    </div>
    <div class="container">
      {movie_tiles}
    </div>
  </body>
</html>
'''


# A single movie entry html template
movie_tile_content = '''
<div class="col-md-6 col-lg-4 movie-tile text-center" data-trailer-youtube-id="{trailer_youtube_id}" data-toggle="modal" data-target="#trailer">
    <div class="diptic">
        <div class="storyline-container">
            <h3>Storyline</h3>
            <p>{movie_storyline}</p>
        </div>
        <small class="trailer-hint"><i>(click to watch trailer)</i></small>
        <div class="awards">{awards}</div>
        <img class="cover-img" src="{poster_image_url}" width="220" height="342">
    </div>
    <h2>{movie_title} <small>({movie_year})</small></h2>
</div>
'''


def create_movie_tiles_content(movies):
    # The HTML content for this section of the page
    content = ''
    for movie in movies:
        # Extract the youtube ID from the url
        youtube_id_match = re.search(
            r'(?<=v=)[^&#]+', movie.trailer_youtube_url)
        youtube_id_match = youtube_id_match or re.search(
            r'(?<=be/)[^&#]+', movie.trailer_youtube_url)
        trailer_youtube_id = (youtube_id_match.group(0) if youtube_id_match
                              else None)
                       
        # Make img tags for awards count
        awards_imgs = ''
        for n in range( 0, movie.oscars_won ):
            awards_imgs += '<img src="oscar_icon.png" width="18" height="50"/>'

        # Append the tile for the movie with its content filled in
        content += movie_tile_content.format(
            movie_title=movie.title,
            movie_year=movie.year,
            movie_storyline=movie.storyline,
            poster_image_url=movie.poster_image_url,
            trailer_youtube_id=trailer_youtube_id,
            awards=awards_imgs
        )
    return content


def open_movies_page(movies):
    # Create or overwrite the output file
    output_file = open('fresh_tomatoes.html', 'w')

    # Replace the movie tiles placeholder generated content
    rendered_content = main_page_content.format(
        movie_tiles=create_movie_tiles_content(movies))

    # Output the file
    output_file.write(main_page_head + rendered_content)
    output_file.close()

    # open the output file in the browser (in a new tab, if possible)
    url = os.path.abspath(output_file.name)
    webbrowser.open('file://' + url, new=2)
