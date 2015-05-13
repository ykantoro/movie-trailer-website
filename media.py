import webbrowser


# class to store movie related information
class Movie():
    """ This class provides a way to store movie related information"""

    VALID_RATINGS = ["G", "PG", "PG-13", "R"]

    # init set-up, takes in movie properties from enteratinment_center.py
    def __init__(self, movie_title, movie_storyline, poster_img,
                 trailer_yt, release_date, rating):
        self.title = movie_title
        self.storyline = movie_storyline
        self.poster_img_url = poster_img
        self.trailer_yt_url = trailer_yt
        self.release_date = release_date
        self.rating = rating

    # opens webpage that plays the specified yt url
    def show_trailer(self):
        webbrowser.open(self.trailer_yt_url)
