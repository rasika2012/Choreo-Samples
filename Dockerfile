# Use an official Python runtime as a parent image
FROM python:3.9-slim

# Set the working directory in the container
WORKDIR /app

# Copy the current directory contents into the container at /app
COPY . /app

# Install requests library
RUN pip install --no-cache-dir requests

# Define the command to run the Python script
USER 10014
CMD ["python", "main.py"]
