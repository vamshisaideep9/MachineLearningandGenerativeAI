FROM python:3.11

WORKDIR /app

ENV FLASK_APP=app.py 
ENV FLASK_RUN_HOST=0.0.0.0

# Install build dependencies
RUN apt-get update && apt-get install -y build-essential && rm -rf /var/lib/apt/lists/*

COPY . /app

RUN pip install -r requirements.txt

EXPOSE 5000 

CMD ["flask","run"]