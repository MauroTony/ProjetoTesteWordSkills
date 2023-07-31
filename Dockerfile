# Use an official Python runtime as a parent image
FROM python:3.11-slim-buster

# Set environment varibles
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

# Set work directory
WORKDIR /code

# Install MySQL dependencies
RUN apt-get update && apt-get install -y default-libmysqlclient-dev gcc pkg-config

# Install dependencies
COPY requirements.txt /code/
RUN pip install --no-cache-dir -r requirements.txt

# Copy project
COPY . /code/
