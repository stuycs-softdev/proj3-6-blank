import urllib
import time

from bs4 import BeautifulSoup
from operator import itemgetter



if __name__ == "__main__":
    
    deathlink = "http://www.ssa.gov/OACT/STATS/table4c6.html"
    deathpage = BeautifulSoup(urllib.urlopen(deathlink))

    result = []


    for x in deathpage.find_all("tr",{"valign":"bottom"}):
        k = x.find_all("td")
        try: 
            result.append(int((float(k[3].getText())+float(k[6].getText())) / 2))
        except:
            pass


    print(result)
