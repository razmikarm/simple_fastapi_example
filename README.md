# simple_fastapi_example
A simple example of FastAPI project

## Pre-Steps

### Run database on docker

> docker run -d --name postgres_db -p 5432:5432 -e POSTGRES_PASSWORD={RANDOM_PASSWORD} postgres

### Enter DB

> docker exec -it postgres_db psql -U postgres

### Initializing database
```
CREATE USER {DB_USER} WITH PASSWORD {DB_PASS} CREATEDB;
SET ROLE {DB_USER};
CREATE DATABASE {DB_NAME};
\q
```

### If container exists, but isn't running
`docker container start postgres_db`


## Instructions

> python -m venv venv

> . venv/bin/activate

> pip install -r requirements.txt

> uvicorn main:app
