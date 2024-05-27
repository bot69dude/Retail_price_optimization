FROM python:3.8-slim-buster

RUN apt update -y && apt install awscli -y
WORKDIR /app

COPY . /app
RUN pip install -r requirements.txt

RUN python main.py

EXPOSE 8081

CMD ["python3", "app.py"]
