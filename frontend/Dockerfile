FROM python:3.10.11-slim

WORKDIR /streamlit-app

EXPOSE 8501

COPY pyproject.toml .
RUN pip install poetry
RUN poetry install 
COPY . .

CMD ["poetry","run","streamlit", "run", "app/main.py"]