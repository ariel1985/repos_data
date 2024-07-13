# Backend API

This is the backend API for the project. It is a RESTful API that is built using Flask and Flask-RESTful. The API is used to interact with the database and perform CRUD operations on the data.

## Installation

To install the backend API, you need to have Python 3 installed on your machine. You can install the required dependencies by running the following command:

```bash
pip install -r requirements.txt
```

## Running the API with fastapi and uvicorn

To run the API, you can use the following command:

```bash
uvicorn app.main:app --reload
```

This will start the API on `http://localhost:8000`.