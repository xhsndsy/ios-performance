


var res = $.ajax('http://127.0.0.1:5000/perfdata',
    {
        dataType: 'json',
        success: function (msg) {
            var cpu_data = msg.cpu_data
            var fps_data = msg.fps_data
            var gpu_data = msg.gpu_data
            var memory_data = msg.memory_data

    //Flot Multiple Axes Line Char
$(function() {





    function euroFormatter(v, axis) {
        return ""+v.toFixed(axis.tickDecimals);
    }


    function doPlot(position) {

        // console.log(res)
        // console.log(cpu_data)
        // console.log(fps_data)
        // console.log(gpu_data)
        // console.log(memory_data)

        $.plot($("#flot-line-chart-multi"), [{

            data: cpu_data,
            label: "cpu"
        }, {
            data: memory_data,
            label: "memory",
            yaxis: 2
        }, {
            data: fps_data,
            label: "fps",
            yaxis: 3
        }, {
            data: gpu_data,
            label: "gpu",
            yaxis: 4
        }], {
            xaxes: [{
                mode: 'time'
            }],
            yaxes: [{
                min: 0
            }, {
                // align if we are to the right
                alignTicksWithAxis: position === "right" ? 1 : null,
                position: position,
                tickFormatter: euroFormatter
            }],
            legend: {
                position: 'sw'
            },
            xaxis: {
                mode: "time",
                timeformat: "%H:%M:%S"
            },
            colors: ["#1ab394"],
            grid: {
                color: "#999999",
                clickable: true,
                tickColor: "#D4D4D4",
                borderWidth:0,
                hoverable: true //IMPORTANT! this is needed for tooltip to work,

            },
            tooltip: true,
            tooltipOpts: {
                content: "%s %x 为 %y",
                xDateFormat: "%H:%M:%S",

                onHover: function(flotItem, $tooltipEl) {
                    // console.log(flotItem, $tooltipEl);
                }
            }

        });
    }

    doPlot("right");

    $("button").click(function() {
        doPlot($(this).text());
    });

});
}
    });



