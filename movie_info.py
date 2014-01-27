import urllib
import time

from bs4 import BeautifulSoup
from operator import itemgetter

LIFEDATA = [78, 77, 76, 75, 74, 73, 72, 71, 70, 69, 68, 67, 66, 65, 65, 64, 63, 62, 61, 60, 59, 58, 57, 56, 55, 54, 53, 52, 51, 50, 49, 48, 47, 46, 45, 44, 43, 43, 42, 41, 40, 39, 38, 37, 36, 35, 34, 33, 32, 32, 31, 30, 29, 28, 27, 26, 26, 25, 24, 23, 22, 21, 21, 20, 19, 18, 18, 17, 16, 15, 15, 14, 13, 13, 12, 11, 11, 10, 10, 9, 8, 8, 7, 7, 6, 6, 5, 5, 5, 4, 4, 4, 3, 3, 3, 3, 2, 2, 2, 2, 2, 2, 2, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0, 0, 0, 0, 0, 0, 0]


#I plan to revise this so you can get multiple results and choose your movie from them
def findMovieLink(title):

    formated = title.replace(' ','+')

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

    deathlink = "http://www.ssa.gov/OACT/STATS/table4c6.html"
    deathpage = BeautifulSoup(urllib.urlopen(deathlink))

    allDead = 0
    currentYear = int(time.strftime("%Y"))

    for x in actorLinks:
        info = {}
        info['name']= x[0]
        
        page = BeautifulSoup(urllib.urlopen(x[1]))

        try:
            birth = int(page.find("time", {"itemprop" : "birthDate"}).find_all("a")[1].get_text())
            info['birth']= birth
        

            try:
                death =  int(page.find("time", {"itemprop" : "deathDate"}).find_all("a")[1].get_text())
                
                info['death'] = death
                info['status'] = "dead"
                info['deathPrediction'] = death
                deadCount = deadCount + 1
                totalCount = totalCount + 1
                if death > allDead:
                    allDead = death
            
                
            except:
                info['death'] = "alive"
                info['status'] = "alive"
                age = int(currentYear) - birth
                yearsLeft = LIFEDATA[age]
                deathYear = currentYear + yearsLeft
                info['deathPrediction'] = deathYear
                aliveCount = aliveCount + 1
                totalCount = totalCount + 1
                if deathYear > allDead:
                    allDead = deathYear

        
        
        except:
            info['birth']= "unkown"
            info['death']= "unkown"
            info['status']= "unkown"
            info['deathPrediction'] = 0
            unkownCount = unkownCount + 1
            totalCount = totalCount + 1

        actors.append(info)
        
    results['actors'] = actors

    results['statusCounts'] = {'dead': deadCount, 'alive': aliveCount, 'unkown':unkownCount, 'total': totalCount}
    
    results['statusPercents'] = {'dead': deadCount/float(totalCount) * 100, 'alive': aliveCount/float(totalCount) * 100, 'unkown': unkownCount/float(totalCount) * 100}
    
    #Predicted year when cas is dead
    results['predictedAllDeadYear'] = allDead

    return results

#maxActors is maximum number of actors returned
#0 means unlimited actors
def movieInfo(title,maxActors):

    movieLink = findMovieLink(title)

    actorLinks = findActorLinks(movieLink,maxActors)

    data = getResults(actorLinks)

    
    return data

if __name__ == "__main__":
    print(movieInfo("star wars episode IV", 10))
    
