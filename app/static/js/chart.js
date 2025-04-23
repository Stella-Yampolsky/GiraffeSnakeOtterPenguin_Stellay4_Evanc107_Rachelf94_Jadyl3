console.log("chart.js loaded");

function parse(file, callback) {
    Papa.parse(file, {
      header: true,
      download: true,
      complete: function (results) {
        //debug
        console.log("Parsed data:", results.data);
        callback(results.data);
      },
      //debug
      error: function (err) {
        console.error("PapaParse error:", err);
    }
    });
  }

  
  function hivByHoodFormat(raw) {
    // this gets rid of the empty line at the end of CSV files, if there is one added by 
    // the text editor. Apex Charts get confused with empty data
    const data = raw.filter(row => 
      row.neighborhood && 
      !isNaN(parseFloat(row.hvi))
    );
    return {
      categories: data.map(row => row.neighborhood),
      values: data.map(row => parseFloat(row.hvi))
    };
  }

  function hivProbFormat(raw) {
    const data = raw.filter(row => 
      row.NeighborhoodUHF && 
      !isNaN(parseFloat(row.probabilityOfHIV)) && 
      !isNaN(parseFloat(row.probabilityOfHIVtoAIDS))
    );

    // to fixed rounds down
    return {
      categories: data.map(row => row.NeighborhoodUHF),
      values1: data.map(row => Number(parseFloat(row.probabilityOfHIV)).toFixed(8)),
      values2: data.map(row => Number(parseFloat(row.probabilityOfHIVtoAIDS)).toFixed(8))
    };
  }

  function totalFormat(raw) {
    const data = raw.filter(row => 
      !isNaN(parseFloat(row.Zip)) && 
      row.LocationCode && 
      row.OverallRating
    );
    const counts = { U: 0, P: 0, WD: 0 };

    data.forEach(row => 
      {
      const rating = row.OverallRating;
      if (counts[rating] !== undefined) 
        {
        counts[rating]++;
        }
    });
  
    return {
      categories: ['Underdeveloped', 'Proficient', 'Well developed'],
      values: [counts.U, counts.P, counts.WD]
    };
  }

  // function eachFormat(raw) 
  // {
  //   const data = raw.filter(row => 
  //     !isNaN(parseFloat(row.Zip)) && 
  //     row.LocationCode && 
  //     row.OverallRating
  //   );
  //   const zipCounts = {};
  //   data.forEach(row => 
  //     {
  //     const zip = row.Zip;
  //     const rating = row.OverallRating;
  //     if (!zipCounts[zip]) 
  //       {
  //       zipCounts[zip] = { U: 0, P: 0, WD: 0 };
  //        }
  //     if (rating === "U" || rating === "P" || rating === "WD") 
  //       {
  //       zipCounts[zip][rating]++;
  //        }
  //   });

  //   const categories = Object.keys(zipCounts);
  //   const valuesU = categories.map(zip => zipCounts[zip].U);
  //   const valuesP = categories.map(zip => zipCounts[zip].P);
  //   const valuesWD = categories.map(zip => zipCounts[zip].WD);
  
  //   return {
  //     categories: categories,
  //     valuesU: valuesU,
  //     valuesP: valuesP,
  //     valuesWD: valuesWD
  //   };
  // }
  
  function hivByHood(data) {
    //debug
    console.log("Rendering chart with:", data);
    const options = 
    {
      chart: 
      {
        type: 'bar',
        height: 500,
        fontFamily: 'Avenir, bold'  
      },
      colors: ["#fcdb00"],
      series: 
      [
        {
          name: 'HIV Score',
          data: data.values
        }
    ],
      xaxis: 
      {
        categories: data.categories,
        title: 
        {
          text: 'Neighborhood'
        },
        fontFamily: 'Avenir, bold'  
      },
      yaxis: 
      {
        title: 
        {
          text: 'HIV',
        },
        fontFamily: 'Avenir, bold'  
      },
      title: 
      {
        min: 0,
        max: 1,
        text: 'Scores',
        fontFamily: 'Avenir, bold',
      }
    };

    const chart = new ApexCharts(document.querySelector("#hoodChart"), options);
    chart.render();
  }

  //would love to have this as a multi axis graph
  //so hiv to aid prob is more visible, but itsnot cooperating
  function hivProb(data) {
    //debug
    console.log("Rendering chart with:", data);
    const options = 
    {
      chart: 
      {
        type: 'line',
        height: 350,
        stacked: false,
        fontFamily: 'Avenir, bold'  
      },
      colors:
      [
        "#4077ed", "#fcdb00"
      ],
      stroke: 
      {
        width: [4, 4]
      },
      series: 
      [
        {
        name: 'HIV',
        data: data.values1,
        },
        {
          name: 'HIV to AIDS',
          data: data.values2,
        }
      ],
      xaxis: 
      {
        categories: data.categories,
        title: 
        {
          text: 'Neighborhood'
        },
        fontFamily: 'Avenir, bold'  
      },
      yaxis: 
      {
        title: 
        {
          text: 'Probability'
        },
        fontFamily: 'Avenir, bold'  
      },
      title: 
      {
        text: 'HIV and HIV to AID Scores by Neighborhood',
        fontFamily: 'Avenir, bold'  
      }
    };

  const chart = new ApexCharts(document.querySelector("#aidsChart"), options);
  chart.render();
  }

    function total(data) {
      //debug
      console.log("Rendering chart with:", data);
      const options = 
      {
        chart: 
        {
          type: 'bar',
          height: 350,
          fontFamily: 'Avenir, bold'  
        },
        colors: ["#fcdb00"],
        series: 
        [{
          name: 'Amount of Locations',
          data: data.values
        }],
        xaxis: 
        {
          categories: data.categories,
          title: 
          {
            text: 'Overall Ratings'
          },
          fontFamily: 'Avenir, bold'  
        },
        yaxis: 
        {
          min: 0,
          max: 900,
          title: 
          {
            text: 'Amount of Locations'
          },
          fontFamily: 'Avenir, bold'  
        },
        title: 
        {
          text: 'Location Ratings Distribution',
          fontFamily: 'Avenir, bold'  
        }
      };
  
      const chart = new ApexCharts(document.querySelector("#rateChart"), options);
      chart.render();
    }

    //unstylized and way takes wayyyy too long to render
    // okay with styling it doesn't render?
    // function each(data) {
    //   const options = {
    //     chart: 
    //     {
    //       type: 'bar',
    //       height: 350
    //     },
    //     plotOptions: 
    //     {
    //       bar: {
    //         columnWidth: '50%',
    //         distributed: true,
    //         horizontal: false
    //       }
    //     },
    //     series: 
    //     [
    //       {
    //         name: 'U',
    //         data: data.valuesU
    //       },
    //       {
    //         name: 'P',
    //         data: data.valuesP
    //       },
    //       {
    //         name: 'WD',
    //         data: data.valuesWD
    //       }
    //     ],
    //     xaxis: 
    //     {
    //       categories: data.categories,
    //       title: 
    //       {
    //         text: 'Zip Code'
    //       }
    //     },
    //     yaxis: {
    //       title: 
    //       {
    //         text: 'Number of Ratings'
    //       }
    //     },
    //     title: 
    //     {
    //       text: 'Ratings Distribution by Zip Code'
    //     },
    //     colors: ['#FF1654', '#247BA0', '#FFDD00'],
    //   };
    
    //   const chart = new ApexCharts(document.querySelector("#eachchart"), options);
    //   chart.render();
    // }