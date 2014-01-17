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
    results = []

    page = BeautifulSoup(urllib.urlopen(movieLink))
    
    for x in page.find_all("tr", {"class" : "even"} or {"class" : "odd"}):
       
        if x.parent['class'][0] == 'cast_list':
            results.append([x.find("span").get_text(),"http://www.imdb.com/" + x.find("a")["href"]])

    return results

def movieInfo(title):

    movieLink = findMovieLink(title)

    actorLinks = findActorLinks(movieLink)

    return actorLinks

if __name__ == "__main__":
   print movieInfo("plan 9 from outer space")
   
