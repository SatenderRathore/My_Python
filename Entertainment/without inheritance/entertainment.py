import fresh_tomatoes
import media

toy_story = media.Movie("Toy Story", 
                        "A Story of a boy and his toys that come to life",
                        "http://a.dilcdn.com/bl/wp-content/uploads/sites/8/2013/02/toy_story_wallpaper_by_artifypics-d5gss19.jpg", 
                        "https://youtu.be/KYz2wyBy3kc" )
                        
                        
                       
avatar = media.Movie("Avatar","A marine on an alien planet", "http://cdn.traileraddict.com/content/20th-century-fox/avatar-6.jpg", "https://youtu.be/5PSNL1qE6VY")

singh_is_bling=media.Movie("Singh Is Bling","Story of a singh", "http://s1.dmcdn.net/MzPKm.jpg", "https://youtu.be/J6HIAfNxzQk")
#toy_story.show_trailer()

print(media.Movie.VALID_RATINGS)

movies = [toy_story, avatar,singh_is_bling]
fresh_tomatoes.open_movies_page(movies)              
