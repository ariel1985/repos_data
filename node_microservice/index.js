const express = require('express');
const mongoose = require('mongoose');
const axios = require('axios');
const repoSchema = require('./repo.model.js');

const app = express();

app.use(express.json());

const retrieve_repo = async (repo) => { 
    const url = `http://localhost:8000/repo/${repo}`;
    const response = await axios.get(url);
    return response.data;
}

// Connect to MongoDB
mongoose.connect('mongodb://localhost/db_repos', {
    useNewUrlParser: true,
    useUnifiedTopology: true
})
.then(() => console.log('Connected to MongoDB...'))
    .catch(err => console.error('Could not connect to MongoDB...', err));

// --- API Endpoints ---

app.get('/', (req, res) => {
    res.send('Welcome to Node.js Microservice! Go to /repos or /repo/:name');
});

app.get('/repos', async (req, res) => {

    try {
        const repos = await repoSchema.find().sort({ stars: -1 }).limit(10);
        res.send(repos);
    }
    catch (err) {
        res.status(500).json({ message: err.message });
        console.error('Could not connect to MongoDB...', err);
    }
});

app.get('/repo/:name', async (req, res) => {
    const repo = await repoSchema.find({ name: req.params.name });
    // if repo not found in the database
    if (repo.length === 0) {
        console.log('Searching for repo in the backend...');
        // try retrieving from the backend_url
        retrieve_repo(req.params.name)
        .then((data) => {
            console.log('data', data);
            res.send(data);
        })
        .catch((err) => {
            console.error('Could not connect to backend', err);
        });
        res.status(404).send(`${req.params.name} Repository not found.`);
    }
    // repo found in the database
    res.send(repo);
});

// Terminal: export PORT=3000
const port = process.env.PORT || 3000;
app.listen(port, () => {
  console.log(`Node.js Microservice listening on port ${port}. Go to http://localhost:${port}/`);
});