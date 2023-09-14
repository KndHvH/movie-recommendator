FROM python:3.10.11-slim

WORKDIR /streamlit-app

EXPOSE 8501

COPY . .

RUN pip install --no-cache-dir -r requirements.txt

CMD ["streamlit", "run", "app/main.py"]