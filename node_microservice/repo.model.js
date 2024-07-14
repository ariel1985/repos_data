const mongoose = require('mongoose');

const repoSchema = new mongoose.Schema({
    repo_id: {
        type: String,
        required: true,
        unique: true // Ensure repo_id is unique
    },
    name: {
        type: String,
        required: true
    },
    stars: {
        type: Number,
        required: true,
        default: 0
    },
    owner: {
        type: String,
        required: true
    },
    description: {
        type: String,
        required: true,
        default: 'No description'
    },
    forks: {
        type: Number,
        required: true,
        default: 0
    },
    languages: {
        type: [String],
        default: [] // Removed required constraint
    },
    topics: {
        type: [String],
        default: [] // Removed required constraint
    }
}, {
    timestamps: true // Add timestamps
});

// Indexing for faster queries on these fields
repoSchema.index({ repo_id: 1, name: 1, owner: 1 });

const Repo = mongoose.model('Repo', repoSchema);

module.exports = Repo;

