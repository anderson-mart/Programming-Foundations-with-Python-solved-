import fresh_tomatoes
import media

a_clockwork_orange=media.Movie("A Clockwork Orange", "A movie based on the book", "https://upload.wikimedia.org/wikipedia/en/thumb/7/73/A_Clockwork_Orange_%281971%29.png/220px-A_Clockwork_Orange_%281971%29.png", "https://www.youtube.com/watch?v=xHFPi_3kc1U")
back_to_the_future=media.Movie("Back to the Future", "A movie about getting back to the future", "https://upload.wikimedia.org/wikipedia/en/thumb/d/d2/Back_to_the_Future.jpg/220px-Back_to_the_Future.jpg", "https://www.youtube.com/watch?v=qvsgGtivCgs")
benders_big_score=media.Movie("Bender's Big Score", "The first of Futurama's movies", "https://upload.wikimedia.org/wikipedia/en/thumb/9/98/Dvdcoverbender.jpg/220px-Dvdcoverbender.jpg", "https://www.youtube.com/watch?v=oEiJ3QA4kKs")
gone_with_the_wind=media.Movie("Gone with the Wind", "A movie about what was gone with the wind", "https://upload.wikimedia.org/wikipedia/commons/thumb/2/27/Poster_-_Gone_With_the_Wind_01.jpg/220px-Poster_-_Gone_With_the_Wind_01.jpg", "https://www.youtube.com/watch?v=0dTsfsr6-X8")
rocky=media.Movie("Rocky", "A boxing movie", "https://upload.wikimedia.org/wikipedia/en/thumb/1/18/Rocky_poster.jpg/220px-Rocky_poster.jpg", "https://www.youtube.com/watch?v=7RYpJAUMo2M")
tron_legacy=media.Movie("Tron: Legacy", "Futuristic cool stuff", "https://upload.wikimedia.org/wikipedia/en/thumb/c/c2/Tron_Legacy_poster.jpg/220px-Tron_Legacy_poster.jpg", "https://www.youtube.com/watch?v=L9szn1QQfas")

movies = [a_clockwork_orange, back_to_the_future, benders_big_score, gone_with_the_wind, rocky, tron_legacy]

fresh_tomatoes.open_movies_page(movies)