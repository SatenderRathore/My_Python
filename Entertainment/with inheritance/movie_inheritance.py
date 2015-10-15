import webbrowser
class Video():
    
    VALID_RATINGS = ["G", "PG", "PG-13", "R"]
    def __init__(self,title,tag_line,poster_image,trailer):
        self.title = title
        self.tag_line = tag_line
        self.poster_image = poster_image
        self.trailer = trailer
        
    
    def show_poster_image(self):
        webbrowser.open(self.poster_image)
            
    
    def show_trailer(self):
        webbrowser.open(self.trailer)
        
        
class Movie(Video):
    
    def __init__(self,title,tag_line,poster_image,trailer,story):
        Video.__init__(self,title,tag_line,poster_image,trailer)
        self.story = story
        
class Tv_serial(Video):
    def __init__(self,title,tag_line,poster_image,trailer,star_cast):
        Video.__init__(self,title,tag_line,poster_image,trailer)
        self.star_cast = star_cast
                
                   
        
        
