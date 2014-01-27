var peopleList = 
[["Heath Ledger", "The Dark Knight", "04/04/2014"],
["Luis Avolos", "The Electric Company", "01/22/2014"],
["Roger Lloyd Pack", "Only Fools and Horses", "01/22/2014"],
["Dave Madden", ""]];
$(document).ready(function(){
    $(".scroll-left").click(left);
    $(".scroll-right").click(right);
});

var right = function(){
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
    var actor = "Gimli";
    var movie = "LoTR";
    var $oldname= $(".info-box");
    var $newname= $('<p class = "info-box"><span class = "actor">'+actor+'</span> <br><span class = "movie">'+movie+'</span></p> ');
    $oldname.fadeOut(300, function() { $oldname.remove();});
    $(".nametag").animate({'width':0},600);
    $(".nametag").append($newname);
    var namewidth = ($(".actor").width() + 1) + "px";
    $newname.css('opacity',0);
    $(".nametag").animate({'width':namewidth},600, function(){$newname.animate({opacity:1})});
    
    
}
