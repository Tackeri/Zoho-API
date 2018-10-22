


// var msg = 'Hello World';
// console.log(msg);






//The following code will send a GET request to NASA’s API and print out 
//the URL for the astronomy picture of the day as well as an explanation:
const https = require('https');
https.get('https://api.nasa.gov/planetary/apod?api_key=DEMO_KEY', (resp) => {
    let data = '';
    // A chunk of data has been recieved.
    resp.on('data', (chunk) => {
        // console.log(chunk);
        data += chunk;
    });
    // The whole response has been received. Print out the result.
    resp.on('end', () => {
        // console.log(JSON.parse(data).explanation);
        console.log('');
        console.log('Date: ' + JSON.parse(data).date);
        console.log(JSON.parse(data).title);
        console.log(JSON.parse(data).hdurl);
        console.log('');
        // console.log(data);
    });
}).on("error", (err) => {
    console.log("Error: " + err.message);
});






// const https = require('https');

// const options = {
//   hostname: 'https://api.weather.gov/gridpoints/EWX/155,90/forecast/hourly',
//   port: 443,
//   path: '/',
//   method: 'GET'
// };

// const req = https.request(options, (res) => {
//   console.log('statusCode:', res.statusCode);
//   console.log('headers:', res.headers);

//   res.on('data', (d) => {
//     process.stdout.write(d);
//   });
// });

// req.on('error', (e) => {
//   console.error(e);
// });
// req.end();





// 'https://api.weather.gov/gridpoints/EWX/155,90/forecast/hourly'