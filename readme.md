# OneTime Secret

The "OneTime Secret" application allows you to transfer a secret message to another user using a secret key.

## Technologies

- Python
- FastAPI
- MongoDB
- Beanie ODM
- pytest

## Installation

To install OneTime Secret and its dependencies, follow these steps:

1. Install [Poetry](https://python-poetry.org/docs/):

    ```sh
   curl -sSL https://install.python-poetry.org | python3 -
   
2. If you do not have Docker installed locally, then you need to install it.

3. Clone the OneTime Secret repository:
    
4. Install dependencies using Poetry:
    ```sh
    poetry install
   
Configuration
Create a .env file in the project root using example.env. In this file, specify the following settings:

.env

    HEX_ENCODE_KEY=
    DB_PATH=
    DB_TEST_PATH=

## Usage

### Run the application:

    docker-compose up --build -d
    Visit http://localhost:8000 in your browser.
