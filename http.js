const https = require('https');
const crypto = require('crypto');
const fs = require('fs');

// Load the JSON file
const jsonData = fs.readFileSync('./oishanu.json');
const jsonObject = JSON.parse(jsonData);

// Extract the email address from the JSON object
const contactEmail = jsonObject.contact_email;

// Generate the TOTP password
const totpSecret = `${contactEmail}HENNGECHALLENGE003`;
const totp = crypto.createHmac('sha512', totpSecret);
const password = totp.update(`${Math.floor(Date.now() / 30000)}`).digest().toString('base32').substr(0, 10);

// Create the Authorization header
const credentials = `${contactEmail}:${password}`;
const encodedCredentials = Buffer.from(credentials).toString('base64');
const authorizationHeader = `Basic ${encodedCredentials}`;

// Make the HTTP POST request
const options = {
  method: 'POST',
  hostname: 'api.challenge.hennge.com',
  path: '/challenges/003',
  headers: {
    'Content-Type': 'application/json',
    'Authorization': authorizationHeader
  }
};

const req = https.request(options, (res) => {
  if (res.statusCode === 200) {
    console.log('Congratulations! You have achieved mission 3');
  } else {
    console.log(`Error: ${res.statusCode}`);
  }
});

req.write(jsonData);
req.end();