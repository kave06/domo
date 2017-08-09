function dibujar_grafica_temperatura(titulo, subtitulo,
                                     listaEjeX, series) {
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
        xAxis: {
            categories: listaEjeX
        },
        yAxis: {
            title: {
                text: 'Temperatura (°C)'
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