#!/usr/bin/python
import media
import fresh_tomatoes

# Instatiating all the movies
avatar = media.Movie(
    "Avatar",
    "2009",
    "A paraplegic marine dispatched to the moon Pandora on a unique mission becomes torn between following his orders and protecting the world he feels is his home.",
    "https://upload.wikimedia.org/wikipedia/en/b/b0/Avatar-Teaser-Poster.jpg",
    "https://www.youtube.com/watch?v=5PSNL1qE6VY",3)
hgttg = media.Movie(
    "The Hitchhiker's Guide to the Galaxy",
    "2005",
    "Mere seconds before the Earth is to be demolished by an alien construction crew, journeyman Arthur Dent is swept off the planet by his friend Ford Prefect, a researcher penning a new edition of \"The Hitchhiker's Guide to the Galaxy.\"",
    "https://upload.wikimedia.org/wikipedia/en/7/7a/Hitchhikers_guide_to_the_galaxy.jpg",
    "https://www.youtube.com/watch?v=eLdiWe_HJv4")
gladiator = media.Movie(
    "Gladiator",
    "2000",
    "When a Roman general is betrayed and his family murdered by an emperor's corrupt son, he comes to Rome as a gladiator to seek revenge.",
    "https://upload.wikimedia.org/wikipedia/en/8/8d/Gladiator_ver1.jpg",
    "https://www.youtube.com/watch?v=0BLZbrLogTo",5)
inception = media.Movie(
    "Inception",
    "2010",
    "A thief who steals corporate secrets through use of dream-sharing technology is given the inverse task of planting an idea into the mind of a CEO.",
    "https://upload.wikimedia.org/wikipedia/en/7/7f/Inception_ver3.jpg",
    "https://www.youtube.com/watch?v=YoHD9XEInc0",4)
limitless = media.Movie(
    "Limitless",
    "2011",
    "With the help of a mysterious pill that enables the user to access 100 percent of his brain abilities, a struggling writer becomes a financial wizard, but it also puts him in a new world with lots of dangers.",
    "https://upload.wikimedia.org/wikipedia/en/1/17/Limitless_Poster.jpg",
    "https://www.youtube.com/watch?v=4TLppsfzQH8")
pulpfiction = media.Movie(
    "Pulp Fiction",
    "1994",
    "The lives of two mob hit men, a boxer, a gangster's wife, and a pair of diner bandits intertwine in four tales of violence and redemption.",
    "https://upload.wikimedia.org/wikipedia/en/8/82/Pulp_Fiction_cover.jpg",
    "https://www.youtube.com/watch?v=s7EdQ4FqbhY",1)
fightclub = media.Movie(
    "Fight Club",
    "1999",
    "An insomniac office worker, looking for a way to change his life, crosses paths with a devil-may-care soap maker, forming an underground fight club that evolves into something much, much more...",
    "https://upload.wikimedia.org/wikipedia/en/f/fc/Fight_Club_poster.jpg",
    "https://www.youtube.com/watch?v=SUXWAEX2jlg")
forrestgump = media.Movie(
    "Forrest Gump",
    "1994",
    "Forrest Gump, while not intelligent, has accidentally been present at many historic moments, but his true love, Jenny Curran, eludes him.",
    "https://upload.wikimedia.org/wikipedia/en/6/67/Forrest_Gump_poster.jpg",
    "https://www.youtube.com/watch?v=bLvqoHBptjg",6)
thematrix = media.Movie(
    "The Matrix",
    "1999",
    "A computer hacker learns from mysterious rebels about the true nature of his reality and his role in the war against its controllers.",
    "https://upload.wikimedia.org/wikipedia/en/c/c1/The_Matrix_Poster.jpg",
    "https://www.youtube.com/watch?v=vKQi3bBA1y8",4)
lifeisbeautiful = media.Movie(
    "Life is Beautiful",
    "1997",
    "When an open-minded Jewish librarian and his son become victims of the Holocaust, he uses a perfect mixture of will, humor and imagination to protect his son from the dangers around their camp.",
    "https://upload.wikimedia.org/wikipedia/en/7/7c/Vitaebella.jpg",
    "https://www.youtube.com/watch?v=16RZHqCIy9M",3)
spiritedaway = media.Movie(
    "Spirited Away",
    "2001",
    "During her family's move to the suburbs, a sullen 10-year-old girl wanders into a world ruled by gods, witches, and spirits, and where humans are changed into beasts.",
    "https://upload.wikimedia.org/wikipedia/en/3/30/Spirited_Away_poster.JPG",
    "https://www.youtube.com/watch?v=ByXuk9QqQkk",1)
thegreenmile = media.Movie(
    "The Green Mile",
    "1999",
    "The lives of guards on Death Row are affected by one of their charges: a black man accused of child murder and rape, yet who has a mysterious gift.",
    "https://upload.wikimedia.org/wikipedia/en/c/ce/Green_mile.jpg",
    "https://www.youtube.com/watch?v=ctRK-4Vt7dA")
backtothefuture = media.Movie(
    "Back The Future",
    "1985",
    "A young man is accidentally sent 30 years into the past in a time-traveling DeLorean invented by his friend, Dr. Emmett Brown, and must make sure his high-school-age parents unite in order to save his own existence.",
    "https://upload.wikimedia.org/wikipedia/en/d/d2/Back_to_the_Future.jpg",
    "https://www.youtube.com/watch?v=qvsgGtivCgs",1)
walle = media.Movie(
    "Wall-E",
    "2008",
    "In the distant future, a small waste collecting robot inadvertently embarks on a space journey that will ultimately decide the fate of mankind.",
    "https://upload.wikimedia.org/wikipedia/en/c/c2/WALL-Eposter.jpg",
    "https://www.youtube.com/watch?v=8-_9n5DtKOc",1)
braveheart = media.Movie(
    "Braveheart",
    "1995",
    "When his secret bride is executed for assaulting an English soldier who tried to rape her, William Wallace begins a revolt and leads Scottish warriors against the cruel English tyrant who rules Scotland with an iron fist.",
    "https://upload.wikimedia.org/wikipedia/en/5/55/Braveheart_imp.jpg",
    "https://www.youtube.com/watch?v=wj0I8xVTV18",5)
toystory = media.Movie(
    "Toy Story",
    "1995",
    "A cowboy doll is profoundly threatened and jealous when a new spaceman figure supplants him as top toy in a boy's room.",
    "https://upload.wikimedia.org/wikipedia/en/1/13/Toy_Story.jpg",
    "https://www.youtube.com/watch?v=KYz2wyBy3kc",3)
up = media.Movie(
    "Up",
    "2009",
    "Seventy-eight year old Carl Fredricksen travels to Paradise Falls in his home equipped with balloons, inadvertently taking a young stowaway.",
    "https://upload.wikimedia.org/wikipedia/en/0/05/Up_%282009_film%29.jpg",
    "https://www.youtube.com/watch?v=qas5lWp7_R0",2)
diehard = media.Movie(
    "Die Hard",
    "1988",
    "John McClane, officer of the NYPD, tries to save wife Holly Gennaro and several others, taken hostage by German terrorist Hans Gruber during a Christmas party at the Nakatomi Plaza in Los Angeles.",
    "https://upload.wikimedia.org/wikipedia/en/7/7e/Die_hard.jpg",
    "https://www.youtube.com/watch?v=2TQ-pOvI6Xo")
vforvendetta = media.Movie(
    "V for Vendetta",
    "2005",
    "In a future British tyranny, a shadowy freedom fighter, known only by the alias of \"V\", plots to overthrow it with the help of a young woman.",
    "https://upload.wikimedia.org/wikipedia/en/9/9f/Vforvendettamov.jpg",
    "https://www.youtube.com/watch?v=IHVzzxrPt1c")
howtotrainyourdragon = media.Movie(
    "How To Train Your Dragon",
    "2010",
    "A hapless young Viking who aspires to hunt dragons becomes the unlikely friend of a young dragon himself, and learns there may be more to the creatures than he assumed.",
    "https://upload.wikimedia.org/wikipedia/en/9/99/How_to_Train_Your_Dragon_Poster.jpg",
    "https://www.youtube.com/watch?v=VEcM3rbnwQ4")
thesixthsense = media.Movie(
    "The Sixth Sense",
    "1999",
    "A boy who communicates with spirits that don't know they're dead seeks the help of a disheartened child psychologist.",
    "https://upload.wikimedia.org/wikipedia/en/6/66/The_sixth_sense.jpg",
    "https://www.youtube.com/watch?v=VG9AGf66tXM")
groundhogday = media.Movie(
    "Groundhog Day",
    "1993",
    "A weatherman finds himself living the same day over and over again.",
    "https://upload.wikimedia.org/wikipedia/en/b/b1/Groundhog_Day_%28movie_poster%29.jpg",
    "https://www.youtube.com/watch?v=tSVeDx9fk60")
kingsspeech = media.Movie(
    "The King's Speech",
    "2010",
    "The story of King George VI of the United Kingdom of Great Britain and Northern Ireland, his impromptu ascension to the throne and the speech therapist who helped the unsure monarch become worthy of it.",
    "http://3.bp.blogspot.com/_LG5VeWc_two/TT3PCZE2poI/AAAAAAAACos/7YhH6ItfGNc/s1600/King_Speech_12915032823333.jpg",
    "https://www.youtube.com/watch?v=pzI4D6dyp_o",4)
pirates = media.Movie(
    "Pirates of the Caribbean: The Curse of the Black Pearl ",
    "2003",
    "Blacksmith Will Turner teams up with eccentric pirate \"Captain\" Jack Sparrow to save his love, the governor's daughter, from Jack's former pirate allies, who are now undead.",
    "https://upload.wikimedia.org/wikipedia/en/0/0e/Pirates_of_the_Caribbean_movie.jpg",
    "https://www.youtube.com/watch?v=0Z1XpfbuZOA")

# The list with all the movies
movies = [
    avatar,hgttg,gladiator,inception,limitless,pulpfiction,fightclub,
    forrestgump,thematrix,pirates,lifeisbeautiful,spiritedaway,thegreenmile,
    backtothefuture,walle,braveheart,toystory,up,diehard,vforvendetta,
    howtotrainyourdragon,thesixthsense,groundhogday,kingsspeech
]

# Generate the HTML file that displays all the movies info
fresh_tomatoes.open_movies_page(movies)

