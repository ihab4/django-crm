# Use an official Python runtime as a parent image
FROM python:3.12.4-slim-bookworm
ENV PYTHONUNBUFFERED=1

# Set the working directory in the container
WORKDIR /django

# Copy the requirements file into the container at /app
COPY requirements.txt requirements.txt

# Install any needed packages specified in requirements.txt
RUN pip install -r requirements.txt

# Copy the current directory contents into the container at /app


