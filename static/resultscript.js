$(document).ready(function () {
    $(".bevel").click(function(){
	$(this).animate({'margin-left': '0px'},600);
	$(this).addClass("thechosenone");
	$(".bevel").not(".thechosenone").animate(
	    {'opacity':0},
	    600,
	    function(){
		$(this).remove();
		var x = $(".bevel").attr('index');
	    };
	    setTimeOut(
		function(){ window.location = '/results?choice='+x;},
		600);
	);

    });
});









