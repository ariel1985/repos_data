# Github Repo Data Collector

Microservices: Nodejs  FastAPI Angular MongoDB

## Overview

1. FastAPI - for collecting data from Github which will connect to github and get information for a certain repo then save it in MongoDB

2. Angular - for the frontend to show the data visually using rest api

3. Nodejs - for microservices - this will be used for the frontend to query the data from the db

4. MongoDB - for storing the data

## Assumptions & Requirements

Repositories to query are all public repositories. 

Project requires:

- Python 3.10
- MongoDB 

## How to run the services

1. FastAPI with

```
cd backend
pip install -r requirements.txt
uvicorn main:app --reload
```
