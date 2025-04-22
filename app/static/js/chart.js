console.log("✅ chart.js loaded");

function parse(file, callback) {
    Papa.parse(file, {
      header: true,
      download: true,
      complete: function (results) {
        callback(results.data);
      }
    });
  }
  
  function format(data) {
    return {
      categories: data.map(row => row.Date),
      values: data.map(row => parseFloat(row.Value))
    };
  }
  
  function render(data) {
    const options = {
      chart: {
        type: 'line',
        height: 350
      },
      series: [{
        name: 'Value',
        data: data.values
      }],
      xaxis: {
        categories: data.categories
      }
    };
  
    const chart = new ApexCharts(document.querySelector("#chart"), options);
    chart.render();
  }
