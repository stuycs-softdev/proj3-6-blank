import urllib
from bs4 import BeautifulSoup
from operator import itemgetter

#I plan to revise this so you can get multiple results and choose your movie from them
def findMovieLink(title):

    formated = title.replace(' ','+');

    url = "http://www.imdb.com/find?q="+formated+"&s=all"
    page = BeautifulSoup(urllib.urlopen(url))

    link = page.find("tr", {"class" : "findResult odd"}).find("a")["href"]

    link = "http://www.imdb.com/" + link

    return link

def findActorLinks(movieLink):
    pass
    
    

def movieInfo(title):

    movieLink = findMovieLink(title)

    actorLinks = findActorLinks(movieLink)

    return movieLink

if __name__ == "__main__":
   print movieInfo("plan 9 from outer space")
   
