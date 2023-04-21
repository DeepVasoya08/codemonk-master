# Use an official Python runtime as a parent image
FROM python:3.9-slim-buster

# Set the working directory to /app
RUN mkdir /code

WORKDIR /code

COPY . /code/
# Install any needed packages specified in requirements.txt
RUN pip install --upgrade pip && pip install -r requirements.txt

# Make port 8000 available to the world outside this container
EXPOSE 8000

# Define environment variable
ENV ENVIRONMENT=production

