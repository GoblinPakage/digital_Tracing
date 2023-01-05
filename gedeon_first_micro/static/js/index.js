d3
 .csv("../static/Iris.csv")
 .then(makeChart);


 const groupBy = (array, key) => {
  // Return the end result
  return array.reduce((result, currentValue) => {
    // If an array already present for key, push it to the array. Else create an array and push the object
    (result[currentValue[key]] = result[currentValue[key]] || []).push(
      currentValue
    );
    // Return the current iteration `result` value, this will be taken as next iteration `result` value and accumulate
    return result;
  }, {}); // empty object is the initial value for result object
};

function makeChart(data) {
  
    // Group by specie as key to the person array
    // var newdata= groupBy(data, "Species");
    // console.log(newdata)
      var country = data.map(function(d) { return d.Species;});
      var value = data.map(function(d) {return d.SepalLengthCm});

// Bar chart
new Chart(document.getElementById("myChart"), {
    type: 'bar',
    data: {
      labels: country,
      datasets: [
        {
          label: "Iris (categories)",
          backgroundColor: ["#3e95cd", "#8e5ea2","#3cba9f","#e8c3b9","#c45850"],
          data: value
        }
      ]
    },
    options: {
      legend: { display: false },
      title: {
        display: true,
        text: 'difference in Iris'
      }
    }
});
}