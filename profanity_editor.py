from urllib.request import FancyURLopener

class MyOpener(FancyURLopener):
    version = "My new User-Agent"


def read_text():
    quotes = open(r"C:\Users\HP\Desktop\Coding\Projects\Udacity_U36\movie_quotes.txt")
    contents_of_file = quotes.read()
    #print (contents_of_file)
    quotes.close()
    check_profanity(contents_of_file)

def check_profanity(text_to_check):
    myopener = MyOpener()
    page = myopener.open("http://www.wdylike.appspot.com/?q=" + text_to_check)
    output = page.read()
    print (output)

read_text()