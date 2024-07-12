const express = require('express');
const axios = require('axios');
const app = express();
const port = 3000;

// Dummy in-memory database
const db = {};

app.get('/api/repos/:name', async (req, res) => {
    const name = req.params.name;

    // Check if the repository is already in the local database
    if (db[name]) {
        return res.json(db[name]);
    }

    // Fetch the repository data from GitHub API
    try {
        const response = await axios.get(`https://api.github.com/repos/${name}`);
        db[name] = response.data;  // Store the data in the local database
        res.json(response.data);
    } catch (error) {
        res.status(404).json({ error: 'Repository not found' });
    }
});

app.listen(port, () => {
    console.log(`Microservice listening at http://localhost:${port}`);
});
