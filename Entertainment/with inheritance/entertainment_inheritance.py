import movie_inheritance

Bajirao_Mastani = movie_inheritance.Movie("Bajirao_Mastani", "The love story of a warrior", "http://i.ytimg.com/vi/NDEExEhvk1Y/maxresdefault.jpg", "https://youtu.be/NDEExEhvk1Y", "https://en.wikipedia.org/wiki/Bajirao_Mastani_(film)")

Baahubali = movie_inheritance.Movie("Baahubali", "The Beginning", "http://f23.wapka-files.com/download/5/1/1/1367319_511cfbc9faad106ab2dfe159.jpg/c7de8d82544318acfac3/baahubali.jpg", "https://www.youtube.com/watch?v=VdafjyFK3ko", "https://en.wikipedia.org/wiki/Baahubali:_The_Beginning")

print(movie_inheritance.Movie.VALID_RATINGS)
print(movie_inheritance.Movie.__bases__)
Baahubali.show_trailer()

Bajirao_Mastani.show_trailer()

