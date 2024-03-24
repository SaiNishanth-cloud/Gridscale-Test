FROM --platform=linux/amd64 python:3.8-slim-buster as build

WORKDIR /app
COPY requirements.txt /app/
RUN pip install --no-cache-dir -r requirements.txt
COPY helloworld.py /app/
RUN chown -R filebeat:filebeat /app && \
    chmod -R 644 /app/*
    
EXPOSE 5000

CMD [ "python","helloworld.py" ]
