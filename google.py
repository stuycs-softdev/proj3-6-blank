#adapted from JASE

import urllib2
import simplejson

def getImages(actor,movie):
    url = "https://ajax.googleapis.com/ajax/services/search/images?v=1.0&q=" + actor + "%20" + movie + "&key=AIzaSyCzb-imYEF9wzQX6r8mTanmjR3U7kZvGaw"

    results = simplejson.load(urllib2.urlopen(urllib2.Request(url)))
    data = results['responseData']
    dataInfo = data['results']
    for myUrl in dataInfo:
        return myUrl['unescapedUrl']

if __name__ == "__main__":
    peeps = [["Bela Lugosi", "Dracula", "Dead", "August 16, 1956"],
["James Stweart", "Vertigo", "Dead", "July 2, 1997"],
["Peter Sellers", "Dr. Stragelove", "Dead", "July 24, 1980"],
["Marlon Brando", "The Godfather", "Dead", "July 1, 2004"],
["Cary Grant", "North by Northwest", "Dead", "November 29, 1986"],
["Lee Van Cleef", "The Good, The Bad, And the Ugly", "Dead", "December 16, 1989"],
["Henry Fonda", "Once Upon a Time in The West", "Dead", "May 16, 1982"],
["Rod Steiger", "A fistful of Dynomite", "Dead", "July 9, 2002"],
["Jose Bodalo", "Django", "Dead", "July 24, 1985"],
["Anthony Perkins", "Psycho", "Dead", "September 12, 1992"],
["Graham Chapman", "Monty Python and the Holy Grail", "Dead", "October 4, 1989"],
["Heath Ledger", "The Dark Knight", "Dead", "January 22, 2008"],
["John Lennon", "A Hard Day's Night", "Dead", "December 8, 1980"],
["Andy Kaufman", "My Breakfast With Blassie", "Dead", "May 16, 1980"],
["Gene Wilder", "Blazing Saddles", "Dead", "July 11, 1933"],
["John Candy", "Spaceballs", "Dead", "March 4, 1994"],
["Alec Guinness", "Star Wars", "Dead", "August 5, 2000"],
["Tor Johnson", "Plan 9 From Outer Space", "Dead", "May 12, 1971"],
["Groucho Marx", "Duck Soup", "Dead", "August 19, 1977"],
 ["Humphrey Bogart", "The Maltese Falcon", "Dead", "January 14, 1957"]]
    for name in peeps:
        c = name[0].split()
        a = c[0]
        b = c[1]
        
        name.append(getImages(a, b));
    print(peeps)
