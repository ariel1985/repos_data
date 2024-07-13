const express = require('express');

const app = express();

const repos = [
    { name: 'repo1', description: 'This is repo1' },
    { name: 'repo2', description: 'This is repo2' },
    { name: 'repo3', description: 'This is repo3' },
    { name: 'repo4', description: 'This is repo4' },
    { name: 'repo5', description: 'This is repo5' },
    { name: 'repo6', description: 'This is repo6' },
    { name: 'repo7', description: 'This is repo7' },
    { name: 'repo8', description: 'This is repo8' },
    { name: 'repo9', description: 'This is repo9' },
    { name: 'repo10', description: 'This is repo10' }
];

app.get('/', (req, res) => {
  res.send('Welcome to Node.js Microservice! Go to http://localhost:3000/repos or http://localhost:3000/repo/:name');
});

app.get('/repos', (req, res) => {
  res.send('Get list of all repos from the database - limited to 10!');
});

app.get('/repo/:name', (req, res) => {
    // 
    res.send('Get repo by name (initially from db, if not - from backend): ' + req.params.name);
});

// Terminal: export PORT=3000
const port = process.env.PORT || 3000;
app.listen(port, () => {
  console.log(`Node.js Microservice listening on port ${port}. Go to http://localhost:${port}/`);
});