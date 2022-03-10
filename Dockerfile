# Pull base image
FROM python:3.9

# Set environment Variable
ENV DONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

# Set Working directory
WORKDIR /code

# Install Dependencies
COPY Pipfile Pipfile.lock /code/
RUN pip install pipenv && pipenv install --system

# Copy Project
COPY . /code/




