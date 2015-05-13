import media
import fresh_tomatoes

# dictionary of movie titles
titles = {
    "Garfield: The Movie": "Garfield: The Movie",
    "Cats & Dogs": "Cats & Dogs",
    "The Aristocats": "The Aristocats",
    "The Cat In The Hat": "The Cat In The Hat",
    "Puss in Boots": "Puss in Boots",
    "The Lion King": "The Lion King"
    }

# dictionary of movie desctioptions
description = {
    "Garfield: The Movie": "Based on the popular comic strip, this live-action comedy follows the exploits of Garfield (Bill Murray), the large, lazy and wisecracking cat owned by hapless Jon Arbuckle (Breckin Meyer). Jon's other housemate, Odie, is a dim but sweet dog who frequently annoys Garfield. When the conniving orange feline gets fed up with Odie, he devises a way to get rid of the pooch. However, after Garfield has a change of heart about Odie, he must find a way to get his fellow pet back.",
    "Cats & Dogs": "Cats and Dogs uncovers the truth about the high-tech, secret war being waged in neighborhoods everywhere that humans aren't even aware of: an eternal struggle between the two great armies of Cats and Dogs. The story follows a Cat plan to destroy a new vaccine that, if developed, would destroy all human allergies to Dogs, and the Dogs' efforts to stop the Cats from executing their plan.",
    "The Aristocats": "When a retired opera singer leaves her inheritance to her cat, Duchess (Eva Gabor), and three kittens, the woman's butler drugs the cats and abandons them in the countryside in order to inherit the fortune himself. Lost in unfamiliar territory, Duchess and the kittens meet Thomas O'Malley (Phil Harris), an alley cat willing to help them return to their home in Paris. They meet several kooky characters along the way, including two English geese and an alley cat jazz band.",
    "The Cat In The Hat": "In this live-action film based on the favorite children's tale, the trouble-making Cat in the Hat (Mike Myers) arrives at the home of bored young Sally Walden (Dakota Fanning) and her brother, Conrad (Spencer Breslin), while their mother (Kelly Preston) is out. The family's pet fish (Sean Hayes) objects to the Cat's presence, but that doesn't stop the hat-wearing giant feline from trying to have fun, no matter how much destruction is left in his wake.",
    "Puss in Boots": "Long before meeting Shrek, Puss in Boots (Antonio Banderas) -- just named a hero for saving a woman from a charging bull -- is run out of town on suspicion of bank robbery, even though the real villain is Puss' friend, Humpty Dumpty (Zach Galifianakis). Though there is still animosity between them, Puss and Humpty reunite to steal a goose that lays golden eggs. Joining them for the adventure of nine lifetimes is notorious cat burglar, Kitty Softpaws (Salma Hayek).",
    "The Lion King": "This Disney animated feature follows the adventures of the young lion Simba (Jonathan Taylor Thomas), the heir of his father, Mufasa (James Earl Jones). Simba's wicked uncle, Scar (Jeremy Irons), plots to usurp Mufasa's throne by luring father and son into a stampede of wildebeests. But Simba escapes, and only Mufasa is killed. Simba returns as an adult (Matthew Broderick) to take back his homeland from Scar with the help of his friends Timon (Nathan Lane) and Pumbaa (Ernie Sabella)"
    }

# dictionary of movie poster img links
poster = {
    "Garfield: The Movie": "http://www.gstatic.com/tv/thumb/movieposters/34575/p34575_p_v7_aa.jpg",
    "Cats & Dogs": "http://www.gstatic.com/tv/thumb/movieposters/27959/p27959_p_v7_aa.jpg",
    "The Aristocats": "http://www.gstatic.com/tv/thumb/movieposters/19375/p19375_p_v7_aa.jpg",
    "The Cat In The Hat": "http://upload.wikimedia.org/wikipedia/en/d/db/Cat_in_the_hat.jpg",
    "Puss in Boots": "https://lh4.ggpht.com/u4AuPkrABNY25-HkH-s1JGK1gks6LHK8U5FkENxmInJ3pE3-Na4TIsrCvOVN5xjLQCHs=w300",
    "The Lion King": "http://ia.media-imdb.com/images/M/MV5BMjEyMzgwNTUzMl5BMl5BanBnXkFtZTcwNTMxMzM3Ng@@._V1_SX640_SY720_.jpg"
    }

# dictionary of youtube video urls for movie trailer
yt_url = {
    "Garfield: The Movie": "https://www.youtube.com/watch?v=4UlzK3X9ddQ",
    "Cats & Dogs": "https://www.youtube.com/watch?v=qzBD_8zOGVA",
    "The Aristocats": "https://www.youtube.com/watch?v=wjA5LWNUPDY",
    "The Cat In The Hat": "https://www.youtube.com/watch?v=4KNKiFud9oM",
    "Puss in Boots": "https://www.youtube.com/watch?v=LKHwaWZdXZU",
    "The Lion King": "https://www.youtube.com/watch?v=MPugv1k7r-s"
    }

# dictionary of release dates for movies
release_date = {
    "Garfield: The Movie": "June 6, 2004",
    "Cats & Dogs": "July 4, 2001",
    "The Aristocats": "December 24, 1970",
    "The Cat In The Hat": "November 8, 2003",
    "Puss in Boots": "October 28, 2011",
    "The Lion King": "June 15, 1994"
    }

# dictionary of movie ratings, actual ratings array in media.py file.
rating = {
    "Garfield: The Movie": media.Movie.VALID_RATINGS[2],
    "Cats & Dogs": media.Movie.VALID_RATINGS[2],
    "The Aristocats": media.Movie.VALID_RATINGS[1],
    "The Cat In The Hat": media.Movie.VALID_RATINGS[2],
    "Puss in Boots": media.Movie.VALID_RATINGS[2],
    "The Lion King": media.Movie.VALID_RATINGS[1]
    }

# array to hold media.Movie class instances
movies = []

# Loop to create instances from dictionary items
for movie, title in titles.items():
    globals()[movie] = media.Movie(title,
                                   description[title],
                                   poster[title],
                                   yt_url[title],
                                   release_date[title],
                                   rating[title])

    # addes movie instances to movies array
    movies.append(globals()[movie])

# sends movie instances to fresh_tomatoes.py to create webpage
fresh_tomatoes.open_movies_page(movies)
