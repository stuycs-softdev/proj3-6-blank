var peopleList = 
[["Bela Lugosi", "Dracula", "Dead", "August 16, 1956"],
["James Stweart", "Vertigo", "Dead", "July 2, 1997"],
["Peter Sellers", "Dr. Stragelove", "Dead", "July 24, 1980"],
["Marlon Brando", "The Godfather", "Dead", "July 1, 2004"],
["Cary Grant", "North by Northwest", "Dead", "November 29, 1986"],
["Lee Van Cleef", "The Good, The Bad, And the Ugly", "Dead", "December 16, 1989"],
["Henry Fonda", "Once Upon a Time in The West", "Dead", "May 16, 1982"],
["Rod Steiger", "A fistful of Dynomite", "Dead", "July 9, 2002"],
["José Bódalo", "Django", "Dead", "July 24, 1985"],
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
 ["Humphrey Bogart", "The Maltese Falcon", "Dead", "January 14, 1957"]];
var index;
$(document).ready(function(){
    index = Math.floor(Math.random()*20 );
    initialize();
    $(".scroll-left").click(left);
    $(".scroll-right").click(right);
});
var initialize = function(){
    $(".actor").text(peopleList[index][0]);
    $(".movie").text(peopleList[index][1]);
    var namewidth = ($(".actor").width()*2 + 1) + "px";
    $(".nametag").animate({'width': namewidth});
}
var right = function(){
    index = index + 1;
    if (index > 19) {index = 0;}
    var src = "http://static2.wikia.nocookie.net/__cb20080318220810/lotr/images/4/43/Gimli.jpg";
    var $old = $(".dead-person");
    var $new = $("<img src='" + src+"'</img>").addClass("dead-person");  
    $new.css('opacity', 0);
    
    $old.animate({
        'opacity':0,
        'width': 0
    }, 600,  function () { 
        $old.remove();
        $("#dead-pic").append($new);
        var width = $new.css('width');
        $new.css('width',0);
        $new.animate({'opacity':1, 'width': width},600,function() {$new.css('width',width)});
    })
    namechange();
}



var left = function(){
    index = index - 1;
    if (index < 0){ index = 19; }
    var src = "http://static2.wikia.nocookie.net/__cb20080318220810/lotr/images/4/43/Gimli.jpg";
    var $old = $(".dead-person");
    var $new = $("<img src='" + src+"'</img>").addClass("dead-person");  
    $new.css('opacity', 0);
    
    $old.animate({
        'opacity':0,
        'width': 0
    }, 600,  function () { 
        $old.remove();
        $("#dead-pic").append($new);
        var width = $new.css('width');
        $new.css('width',0);
        $new.animate({'opacity':1, 'width': width},600,function() {$new.css('width',width)});
    })
    namechange();
}

var namechange = function(){
    var actor = peopleList[index][0];
    var movie = peopleList[index][1];
    var $oldname= $(".info-box");
    var $newname= $('<p class = "info-box"><span class = "actor">'+actor+'</span> <br><span class = "movie">'+movie+'</span></p> ');
    $oldname.fadeOut(300, function() { $oldname.remove();});
    $(".nametag").animate({'width':0},600);
    $(".nametag").append($newname);
    var namewidth = ($(".actor").width()*2 + 1) + "px";
    $newname.css('opacity',0);
    $(".nametag").animate({'width':namewidth},600, function(){$newname.animate({opacity:1})});
    
    
}
