# movie-recomendation-api-pycaret

[![Python 3.10](https://img.shields.io/badge/python-3.10-blue.svg)](https://www.python.org/downloads/release/python-31010/) 
[![PEP20](https://img.shields.io/badge/code%20style-pep20-red.svg)](https://www.python.org/dev/peps/pep-0020/) 
[![PEP8](https://img.shields.io/badge/code%20style-pep8-orange.svg)](https://www.python.org/dev/peps/pep-0008/) 
[![bandit](https://img.shields.io/badge/code%20style-bandit-green.svg)](https://github.com/PyCQA/bandit)
[![Code style: black](https://img.shields.io/badge/code%20style-black-000000.svg)](https://github.com/psf/black)

## Technology and Resources

- [Python 3.10](https://www.python.org/downloads/release/python-31010/) - **pre-requisite**
- [Docker](https://www.docker.com/get-started) - **pre-requisite**
- [Docker Compose](https://docs.docker.com/compose/) - **pre-requisite**
- [Poetry](https://python-poetry.org/)
- [FastAPI](https://github.com/tiangolo/fastapi)
- [Streamlit](https://docs.streamlit.io/)
- [Uvicorn](https://github.com/encode/uvicorn)

*Please pay attention on **pre-requisites** resources that you must install/configure.*

#### Routes

- `/`: The root path is a redirect to `/docs`
- `/docs`: Swagger
- `/redoc`: Redoc
- `/health-check`: Verify sure the application is up
- `/all-movies`: Get all movies names
- `/recommend`: Recommend movies
- `/info`: Get movie info

*The project will be running at `http://localhost:8000/`*

The `entrypoint` of this project is the `run.py` file on the root path.

### Content

This repository contains the code and documentation for a college project aimed at enhancing our understanding of recommendation clustering techniques through the lens of the film industry. In this project, we delve into the exciting world of movie recommendations and employ clustering algorithms to develop a more efficient and personalized movie recommendation system.