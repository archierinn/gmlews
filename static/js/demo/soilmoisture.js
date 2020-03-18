function dspChrt(hum, time) {

    var ctx = document.getElementById('myChart').getContext('2d');
    var myChart = new Chart(ctx, {
    type: 'line',
    data: {
    labels: time,
    datasets: [{
      label: 'Humidity',
      data: hum, // json value received used in method
      backgroundColor: ["rgba(153,255,51,0.4)"],
      borderColor: ["#808080"],
      borderWidth: 1
    }]
  },
  options: {
    responsive: true,
    scales: {
      yAxes: [{
        ticks: {
          suggestedMin : 0,
          suggestedMax : 100,
          stepSize: 10,
        },
        scaleLabel: {
          display: true,
          labelString: 'Humidity (%)'
        }
      }],
      xAxes: [{
        scaleLabel: {
          display: true,
          labelString: 'Date Time'
        }
      }]
    }
  }
});
}

var myVar = setInterval(loadChart, 60000); // updates chart every one minute

function loadChart()
{
   var data, hum = [], time = [];

   var requestURL = 'http://127.0.0.1:8000/api/data'; //URL of the JSON data
   var request = new XMLHttpRequest({mozSystem: true}); // create http request

   request.onreadystatechange = function() {
    if(request.readyState == 4 && request.status == 200) {
       data = JSON.parse(request.responseText);
       for (var i=0; i<data.length;i++) {
           hum.push(data[i].moisture);
           time.push(data[i].timestamp);
       }
       console.log(hum);
       console.log(time);
       console.log(data);
       
       dspChrt(hum, time);   
 }
}
   request.open('GET', requestURL);
   request.send(); // send the request

}
loadChart();