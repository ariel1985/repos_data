# POCs To Do

[ ] - FastAPI
[ ] - MongoDB - Install & Connect
[ ] - MongoDB - CRUD
[ ] - Dockers4All
[ ] - Docker-compose
[ ] - Nodejs
[ ] - Angular
[ ] - Documentation





# Github Repo Data Collector

## Table of Contents

- [Description](#description)
- [Overview](#overview)
- [Assumptions & Requirements](#assumptions--requirements)
- [How to run the services](#how-to-run-the-services)


## Description

Microservices: Nodejs  FastAPI Angular MongoDB

This project is a microservices architecture that collects data from Github repositories and stores it in MongoDB. The data is then displayed in a frontend using Angular. The frontend will query the data from the backend using Nodejs.

## Overview

1. FastAPI - for collecting data from Github which will connect to github and get information for a certain repo then save it in MongoDB

2. Angular - for the frontend to show the data visually using rest api

3. Nodejs - for microservices - this will be used for the frontend to query the data from the db

4. MongoDB - for storing the data

## Assumptions & Requirements

Repositories to query are all public repositories. 

Project requires:

- Python v3.10
- MongoDB v7.0.12


## How to run the services

[MongoDB](https://www.mongodb.com/docs/manual/tutorial/install-mongodb-on-ubuntu/)

```
sudo systemctl start mongod
```

FastAPI with python 3.10

```
cd backend
pip install -r requirements.txt
uvicorn app.main:app --reload
```


