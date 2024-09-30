# Quorum Legislative Data Dashboard

## Description

This project is a Django/React.js application designed to display legislative data.
It provides an interface to view details about bills and legislators, including their voting records.


## Setting Up the Environment


First, copy the .env.example files to .env files in both the root and frontend folders.:

Root:

    cp .env.example .env

Frontend:

    cp frontend/.env.example frontend/.env

<br/>

After copying the .env files, run docker-compose:

    docker-compose up --build


If everything worked fine, you'll be able to see the expected screen shown above, here:

    http://localhost:80


## Running

If everything worked fine, you should see into:

    http://localhost:80

![Home](./home.png)

    http://localhost:80/bills/

![Bills](./bills.png)

    http://localhost:80/legislators/

![Legislators](./legislators.png)

## Tests

To run the unit tests, you need to access the backend container:

    docker exec -it quorum_legislative_data_backend_1 /bin/bash

and run:

    pytest

Note: We currently have 2 tests (backend/votes/tests/test_views.py).


## Structure:

### Backend:

1. Running into: 

    http://localhost:8000/

2. Using Python/Django;

### Frontend:

1. Running into

    http://localhost:80

2. Using React;