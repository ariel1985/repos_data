const express = require('express');

const app = express();

app.get('/', (req, res) => {
  res.send('Hello from Node.js Microservice!');
});

app.get('/:name', (req, res) => {
    res.send('Looking for repo name: ' + req.params.name);
    });

app.listen(3000, () => {
  console.log('Node.js Microservice listening on port 3000. Go to http://localhost:3000/');
});