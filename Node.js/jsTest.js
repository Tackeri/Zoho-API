


// var msg = 'Hello World';
// console.log(msg);




const request = require('https');

request.get('https://api.weather.gov/gridpoints/EWX/155,90/forecast/hourly', (resp) => {
    let data = '';

    // Chuck of data is recieved.
    resp.on('data', (chunk) => {
        data += chunk;
    });

    // Whole response is received. Print result.
    resp.on('end', () => {
        console.log(data.explanation);
    });

}).on("error", (err) => {
    console.log("Error: " + err.message);

});