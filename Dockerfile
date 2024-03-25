FROM --platform=linux/amd64 python:3.8-slim-buster as build

# Create directory for log files
RUN mkdir -p /var/log/containers

# Set permissions for the log directory
RUN chmod 755 /var/log/containers

# Add the filebeat user and group
RUN groupadd -r filebeat && useradd --no-log-init -r -g filebeat filebeat

WORKDIR /app
COPY requirements.txt /app/
RUN pip install --no-cache-dir -r requirements.txt
COPY helloworld.py /app/
RUN chown -R filebeat:filebeat /app && \
    chmod -R 644 /app/*

EXPOSE 5000

CMD [ "python","helloworld.py" ]
