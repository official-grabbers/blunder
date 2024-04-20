# Use the official Python image from Docker Hub
FROM python:3.10

# Set environment variables from .env.docker file
ARG DOCKER_ENV_FILE
ENV DOCKER_ENV_FILE=${DOCKER_ENV_FILE}
RUN if [ -f "$DOCKER_ENV_FILE" ]; then export $(cat $DOCKER_ENV_FILE | xargs); fi

# Set working directory in the container
WORKDIR /app

# Copy the rest of the application app
COPY . /app/

# Set DJANGO_SETTINGS_MODULE environment variable
ENV DJANGO_SETTINGS_MODULE=config.settings

# Install requirements
RUN pip install --no-cache-dir -r requirements.txt
