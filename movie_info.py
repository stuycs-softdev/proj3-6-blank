import urllib
from bs4 import BeautifulSoup
from operator import itemgetter

#I plan to revise this so you can get multiple results and choose your movie from them
def findMovieLink(title):

    formated = title.replace(' ','+');

    url = "http://www.imdb.com/find?q="+formated+"&s=all"
    page = BeautifulSoup(urllib.urlopen(url))

    link = page.find("tr", {"class" : "findResult odd"}).find("a")["href"].split('?')[0]

    link = "http://www.imdb.com/" + link + "fullcredits?ref_=tt_cl_sm#cast"
    return link

def findActorLinks(movieLink,maxActors):
    results = []
    page = BeautifulSoup(urllib.urlopen(movieLink))
    count = 0
    for x in page.find_all("tr", {"class" : ["odd","even"]}):
       
        if x.parent['class'][0] == 'cast_list':
            results.append([x.find("span").get_text(),"http://www.imdb.com/" + x.find("a")["href"]])
            count = count + 1
            if count == maxActors:
                break
    return results

def getResults(actorLinks):

    results = {}
    actors = []

    deadCount = 0
    aliveCount = 0
    unkownCount = 0
    totalCount = 0

    for x in actorLinks:
        info = {}
        info['name']= x[0]
        
        page = BeautifulSoup(urllib.urlopen(x[1]))

        try:
            birth = page.find("time", {"itemprop" : "birthDate"}).find_all("a")[1].get_text()
            info['birth']= birth
        
            try:
                death =  page.find("time", {"itemprop" : "deathDate"}).find_all("a")[1].get_text()
                        
                info['death'] = death
                info['status'] = "dead"
                deadCount = deadCount + 1
                totalCount = totalCount + 1

            except:
                info['death'] = "alive"
                info['status'] = "alive"
                aliveCount = aliveCount + 1
                totalCount = totalCount + 1

        except:
            info['birth']= "unkown"
            info['death']= "unkown"
            info['status']= "unkown"
            unkownCount = unkownCount + 1
            totalCount = totalCount + 1

        actors.append(info)
        
    results['actors'] = actors

    results['statusCounts'] = {'dead': deadCount, 'alive': aliveCount, 'unkown':unkownCount, 'total': totalCount}
    
    results['statusPercents'] = {'dead': deadCount/float(totalCount) * 100, 'alive': aliveCount/float(totalCount) * 100, 'unkown': unkownCount/float(totalCount) * 100}

    return results

#maxActors is maximum number of actors returned
#0 means unlimited actors
def movieInfo(title,maxActors):

    movieLink = findMovieLink(title)

    actorLinks = findActorLinks(movieLink,maxActors)

    data = getResults(actorLinks)

    
    return data

if __name__ == "__main__":
   print movieInfo("fight club", 2)
   
