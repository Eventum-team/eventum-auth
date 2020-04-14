FROM python:3.6

ENV PYTHONUNBUFFERED 1

# create root directory for our project in the container
RUN mkdir /src

# Set the working directory to /music_service
WORKDIR /src

# Copy the current directory contents into the container at /music_service
ADD . /src/

# Install any needed packages specified in requirements.txt
RUN pip install -r requirements.txt
