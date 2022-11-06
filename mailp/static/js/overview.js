let closeBtn = document.getElementById("close-sidebar");
let sidebar = document.querySelector(".sidebar");
let showBtn = document.getElementById("show-sidebar");
var graph = document.getElementById("chart_type");



closeBtn.addEventListener("click", function () {
    sidebar.classList.toggle("hide");
    showBtn.classList.add("toggle");
})

showBtn.addEventListener("click", function () {
    sidebar.classList.toggle("hide");
    showBtn.classList.remove("toggle");
})

function processData(dataset) {
    var result = []
    dataset = JSON.parse(dataset);
    dataset.forEach(item => result.push(item.fields));
    return result;
}

var pivot = new WebDataRocks({
    container: "#data-analysis-container",
    toolbar: true,
    report: {
        dataSource: {
            filename: tempo
        }
    },
    reportcomplete: function () {
        pivot.off("reportcomplete");
        pivotTableReportComplete = true;
        createGoogleChart();
    }
});

var tempo = function dataCollection(data) {
    return data;
}

var hehe;

$.ajax({
    url: $("#data-analysis-container").attr("data-url"),
    dataType: 'json',
    success: function (data) {
        tempo(data);
        hehe = new WebDataRocks({
            container: "#data-analysis-container",
            width: "100%",
            height: "100%",
            toolbar: true,
            report: {
                dataSource: {
                    data: processData(data)
                },
                formats: [{
                    maxDecimalPlaces: 2
                }],
                slice: {
                    rows: [{
                        "uniqueName": "Program Type"
                    }],
                    columns: [{
                        "uniqueName": "Numbers"
                    }],
                    measures: [{
                        "uniqueName": "Grades",
                        "aggregation": "average"
                    }]
                },
            },
            reportcomplete: function () {
                pivot.off("reportcomplete");
                pivotTableReportComplete = true;
                createGoogleChart();
            }

        });
        return hehe;
    }
});



var pivotTableReportComplete = true;
var googleChartsLoaded = false;

google.charts.load('current', {
    'packages': ['corechart']
});

google.charts.setOnLoadCallback(onGoogleChartsLoaded);

function onGoogleChartsLoaded() {
    googleChartsLoaded = true;
    if (pivotTableReportComplete) {
        createGoogleChart();
    }
}

function createGoogleChart() {
    if (googleChartsLoaded) {
        hehe.googlecharts.getData({
                type: "pie"
            }, // specify the chart type
            drawChart,
            drawChart
        );
    }
}


function drawChart(_data) {
    console.log(_data)
    var data = google.visualization.arrayToDataTable(_data.data);
    var options = {
        title: "Number of students per education level",
        // height: 700,
        legend: {
            position: 'top'
        },
        is3D: true,
        colors: ['#66ccff', '#22fe44', '#ff6622', '#ffff00']
    };
    var chart = new google.visualization.PieChart(document.getElementById('googlechartContainer'));
    // var chart = new google.visualization.ColumnChart(document.getElementById('googlechartContainer'));
    chart.draw(data, options);
}