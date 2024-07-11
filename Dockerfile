# Use an official Python runtime as a parent image
FROM python:3.12.4-slim-bookworm

# Set the working directory in the container
WORKDIR /app

# Copy the requirements file into the container at /app
COPY requirements.txt requirements.txt

# Install any needed packages specified in requirements.txt
RUN pip install -r requirements.txt

# Copy the current directory contents into the container at /app
COPY . .

CMD [ "python3", "crm/manage.py", "runserver", "0.0.0.0:8000" ]

# # Make port 8000 available to the world outside this container
# EXPOSE 8000

