function dibujar_grafica_temperatura(titulo, subtitulo,
                                     xAxis, series) {
    Highcharts.chart('container', {
        chart: {
            type: 'line'
        },
        title: {
            text: titulo
        },
        subtitle: {
            text: subtitulo
        },
        xAxis: xAxis,
        yAxis: {
            title: {
                text: 'Temperature (°C)'
            }
        },
        plotOptions: {
            line: {
                dataLabels: {
                    enabled: true
                },
                enableMouseTracking: false
            }
        },
        series: series
    });
}