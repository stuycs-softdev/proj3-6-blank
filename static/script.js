var peopleList = [['Bela Lugosi', 'Dracula', 'Dead', 'August 16, 1956', 'http://www.doctormacro.com/Images/Lugosi,%20Bela/Annex/Annex%20-%20Lugosi,%20Bela%20(Mark%20of%20the%20Vampire)_02.jpg'], ['James Stweart', 'Vertigo', 'Dead', 'July 2, 1997', 'http://cdn.motocross.transworld.net/files/2011/01/a1_wallpaper_06.jpg'], ['Peter Sellers', 'Dr. Stragelove', 'Dead', 'July 24, 1980', 'http://upload.wikimedia.org/wikipedia/commons/8/85/Peter_Sellers_at_home_in_Belgravia,_London,_1973.jpg'], ['Marlon Brando', 'The Godfather', 'Dead', 'July 1, 2004', 'http://www.biography.com/imported/images/Biography/Images/Profiles/B/Marlon-Brando-9224306-2-402.jpg'], ['Cary Grant', 'North by Northwest', 'Dead', 'November 29, 1986', 'http://upload.wikimedia.org/wikipedia/commons/2/27/Grant,_Cary_(Suspicion)_01_Crisco_edit.jpg'], ['Lee Van Cleef', 'The Good, The Bad, And the Ugly', 'Dead', 'December 16, 1989', 'http://upload.wikimedia.org/wikipedia/it/5/5a/Lee_Van_Cleef.jpg'], ['Henry Fonda', 'Once Upon a Time in The West', 'Dead', 'May 16, 1982', 'http://www.goldenhollywoodera.com/_files/image/Henry%20Fonda_3.jpg'], ['Rod Steiger', 'A fistful of Dynomite', 'Dead', 'July 9, 2002', 'http://www.nndb.com/people/762/000026684/rod-steiger-2-sized.jpg'], ['Jose Bodalo', 'Django', 'Dead', 'July 24, 1985', 'http://upload.wikimedia.org/wikipedia/en/thumb/6/62/Jos%C3%A9_B%C3%B3dalo.jpg/220px-Jos%C3%A9_B%C3%B3dalo.jpg'], ['Anthony Perkins', 'Psycho', 'Dead', 'September 12, 1992', 'http://www.biography.com/imported/images/Biography/Images/Profiles/P/Anthony-Perkins-9437779-1-402.jpg'], ['Graham Chapman', 'Monty Python and the Holy Grail', 'Dead', 'October 4, 1989', 'http://upload.wikimedia.org/wikipedia/en/f/f7/Graham_Chapman_Portrait.png'], ['Heath Ledger', 'The Dark Knight', 'Dead', 'January 22, 2008', 'http://upload.wikimedia.org/wikipedia/commons/4/4f/Heath_Ledger.jpg'], ['John Lennon', "A Hard Day's Night", 'Dead', 'December 8, 1980', 'http://www.johnlennon.com/wp-content/themes/jl/images/home-gallery/2.jpg'], ['Andy Kaufman', 'My Breakfast With Blassie', 'Dead', 'May 16, 1980', 'http://upload.wikimedia.org/wikipedia/en/9/9a/Akaufman1.jpg'], ['Gene Wilder', 'Blazing Saddles', 'Dead', 'July 11, 1933', 'http://upload.wikimedia.org/wikipedia/commons/0/0d/Gene_Wilder_02.jpg'], ['John Candy', 'Spaceballs', 'Dead', 'March 4, 1994', 'http://upload.wikimedia.org/wikipedia/commons/4/4a/John_Candy.jpg'], ['Alec Guinness', 'Star Wars', 'Dead', 'August 5, 2000', 'http://upload.wikimedia.org/wikipedia/commons/e/e9/Alec_Guinness_6_Allan_Warren.jpg'], ['Tor Johnson', 'Plan 9 From Outer Space', 'Dead', 'May 12, 1971', 'http://upload.wikimedia.org/wikipedia/commons/thumb/2/2f/PlanNine_10.jpg/220px-PlanNine_10.jpg'], ['Groucho Marx', 'Duck Soup', 'Dead', 'August 19, 1977', 'http://cdn.pastemagazine.com/www/articles/groucho.jpg?1348139211'], ['Humphrey Bogart', 'The Maltese Falcon', 'Dead', 'January 14, 1957', 'http://beingsakin.files.wordpress.com/2012/05/humphrey-bogart.jpg']];

var index;
$(document).ready(function(){
    index = Math.floor(Math.random()*20 );
    initialize();
    $(".scroll-left").click(left);
    $(".scroll-right").click(right);

    $(".scroll-left").mouseenter(function(){
	$(".scroll-left").attr("src","http://i.imgur.com/VNIMZMc.png");
    });
    $(".scroll-left").mouseout(function(){
	$(".scroll-left").attr("src","http://i.imgur.com/GJSstSW.png");
    });
    $(".scroll-right").mouseenter(function(){
	$(".scroll-right").attr("src","http://i.imgur.com/eSt5zkQ.png");
    });
    $(".scroll-right").mouseout(function(){
	$(".scroll-right").attr("src","http://i.imgur.com/X2GTv0I.png");
    });

});
var initialize = function(){
    $(".actor").text(peopleList[index][0]);
    $(".movie").text(peopleList[index][1]);
    $(".dead-person").attr("src",peopleList[index][4]);
    $(".death-date").text("Died: "+peopleList[index][3]);
    var namewidth = ($(".actor").width()*2 + 1) + "px";
    $(".nametag").animate({'width': namewidth});
}
var right = function(){
    index = index + 1;
    if (index > 19) {index = 0;}
    var src = peopleList[index][4];
    var $old = $(".dead-person");
    var $new = $("<img title= 'We see dead people' src='" + src+"'</img>").addClass("dead-person");  
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
    var src = peopleList[index][4];
    var $old = $(".dead-person");
    var $new = $("<img title = 'We see dead people.' src='" + src+"'</img>").addClass("dead-person");  
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
    var deathdate = peopleList[index][3];
    var $oldname= $(".info-box");
    var $newname= $('<p class = "info-box"><span class = "actor">'+actor+'</span> <br><span class = "movie">'+movie+'</span><br><span class = "death-date">'+deathdate+'</span></p> ');
    $oldname.fadeOut(300, function() { $oldname.remove();});
    $(".nametag").animate({'width':0},600);
    $(".nametag").append($newname);
    var namewidth = ($(".actor").width()*2 + 1) + "px";
    $newname.css('opacity',0);
    $(".nametag").animate({'width':namewidth},600, function(){$newname.animate({opacity:1})});    
}

    
