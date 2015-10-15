import urllib


def read_text():
    quotes = open("/home/satender/Downloads/python/my_python/text.txt")
    contents_of_file = quotes.read()
    quotes.close()
    check_profanity(contents_of_file)
    
def check_profanity(text_to_check):
    connection = urllib.urlopen("http://www.wdyl.com/profanity?q="+text_to_check)
    output = connection.read()
    connection.close()
    
    if "true" in output:
        print("Profanity alert !!!")
    elif "false" in output:
        print("The Document has no curse word")
    else:
        print("could not scan the document properly.")
        
read_text()                
