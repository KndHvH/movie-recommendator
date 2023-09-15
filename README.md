# Movie Recommendator

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

*The api will be running at `http://localhost:8000/v1`*

The `entrypoint` of the api is the `run.py` file on the api foulder.

#### Frontend

*The frontend will be running at `http://localhost:8501/`*

The `entrypoint` of the frontend project is the `main.py` file on the frontend foulder.

### Content

This repository contains the code and documentation for a college project aimed at enhancing our understanding of recommendation clustering techniques through the lens of the film industry. In this project, we delve into the exciting world of movie recommendations and employ clustering algorithms to develop a more efficient and personalized movie recommendation system.

### Recommendation Methodology

The methodology used for recommending movies is as follows:

1. **Data Loading**: The movie data is loaded from a CSV file named `all_movies.csv` into a dataframe.
2. **Text Vectorization**: The synopsis of each movie (`sinopse_aprimorada`) is vectorized using the TF-IDF (Term Frequency-Inverse Document Frequency) method. This results in a matrix (`tfidf_matrix`) where each row represents a movie and each column represents a term's TF-IDF score.
3. **Movie Indexing**: For a given movie title, its index in the dataframe is retrieved.
4. **Movie Vector Retrieval**: For a given movie index, its corresponding vector from the `tfidf_matrix` is retrieved.
5. **K-Nearest Neighbors**: Using the movie vector, the K-Nearest Neighbors algorithm is applied to find movies that are similar to the given movie. This is done using a pre-trained model that has been fit with the `tfidf_matrix`.
6. **Recommendation Generation**: The distances and indices of the K-Nearest Neighbors are retrieved. These are paired and sorted based on distances. Movie titles corresponding to the sorted indices are retrieved, ensuring that the given movie and any other movies in the blacklist are excluded. The resulting list of movie titles is the recommended movies.
7. **Random Movie Retrieval**: There's also a function to retrieve a random movie title from the dataframe.

### Members

* [@kndhvh](https://github.com/KndHvH)
* [@The-Icaro](https://github.com/The-Icaro)
* [@eduardomatoss](https://github.com/eduardomatoss)
* [@cesarnorena](https://github.com/cesarnorena)