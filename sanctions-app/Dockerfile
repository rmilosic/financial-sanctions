FROM python:3.7-alpine
WORKDIR /sanctions-app
COPY requirements.txt requirements.txt
RUN pip install -r requirements.txt
COPY . .
CMD ["python", "main.py"]
