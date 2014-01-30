console.log("Javascript loaded");
var index;
$(document).ready(function () {
    console.log("Jquery Loaded");
    $(".bevel").click(function(){
//	$(this).animate({'margin-left': '0px'},600);
	$(this).addClass("thechosenone");
	x = $(this).attr('index');
	$(".bevel").not(".thechosenone").animate(
	    {'opacity':0, 'height':0},
	    600
	);
	setTimeout(
	    function(){ window.location = '/results?choice='+x;},
	    600);
    });
    if ($("#living").length){
	console.log("loaded");
	loadChart();
    };
});



/**

var chart;
var legend;
var chartData=[
    {
	"state": "Living";
	"number": $("#living");
    },
    {
	"state": "Dead";
	"number": $("#dead");
    },
    {
	"state": "Fate Unknown";
	"number": $("#unknown");
    }
];


var loadChart = function () {
    // PIE CHART
    chart = new AmCharts.AmPieChart();
    chart.dataProvider = chartData;
    chart.titleField = "state";
    chart.valueField = "#number";
    chart.outlineColor = "#FFFFFF";
    chart.outlineAlpha = 0.8;
    chart.outlineThickness = 2;
    chart.balloonText = "[[title]]<br><span style='font-size:14px'><b>[[value]]</b> ([[percents]]%)</span>";
    
    // WRITE
    chart.write("chartdiv");
};





**/