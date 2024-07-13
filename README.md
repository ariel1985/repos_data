# POCs To Do

- [x] FastAPI
- [x] FastAPI + MongoDB 
- [x] FastAPI + Github API
- [x] FastAPI - Docker
- [x] MongoDB - Install & Connect (local)
- [x] MongoDB - Docker
- [x] Angular 
- [x] Angular (with nginx) - Docker
- [x] Angular GUI (input, list, requests)
- [x] Nodejs express
- [ ] Nodejs express + MongoDB 
- [ ] Nodejs express + Backend API
- [ ] Nodejs + express Docker
- [x] Docker-compose


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

### Containers

Build and run the services using Docker Compose:

```sh
docker-compose up --build
```

Or use docker: 

```sh
docker build -t frontend .
docker run -p 4200:80 frontend

docker rmi $(docker images -a -q)
docker stop $(docker ps -a -q)
docker rm $(docker ps -a -q)
```

### Services

[MongoDB](https://www.mongodb.com/docs/manual/tutorial/install-mongodb-on-ubuntu/)

```
sudo systemctl start mongod
```

Backend FastAPI with python 3.10

```
cd backend
pip install -r requirements.txt
uvicorn app.main:app --reload
```



### Frontend 


Using Angular CLI to create the angular-service on the root folder:

```sh
npm install -g @angular/cli
ng new angular-service
ng build --configuration production
```

### Nodejs Microservice

Nodejs

```
cd frontend
npm install
npm install express axios
npm start
```



Angular

```
cd frontend
npm install
ng serve
```


