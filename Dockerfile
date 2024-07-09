# Use an official Python runtime as a parent image
FROM python:3.9.19-slim-bullseye

# Set the working directory in the container
WORKDIR /app

# Copy the requirements file into the container at /app
COPY requirements.txt /app/

# Install any needed packages specified in requirements.txt
RUN pip install --no-cache-dir -r requirements.txt

# Copy the current directory contents into the container at /app
COPY . /

# Make port 8000 available to the world outside this container
EXPOSE 8000

# Run the Django server
RUN python3 manage.py migrate --no-input

RUN python3 manage.py runsrever
