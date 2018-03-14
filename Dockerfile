# Use an official Python runtime as a parent image
FROM python:2.7-slim

# This sets the working directory to /newapp (inside the container)
WORKDIR /newapp

# This copies the current directory contents into the container at /newapp
ADD . /newapp

# Install any needed packages (i.e. those packages that we specified in requirements.txt)
RUN pip install --trusted-host pypi.python.org -r requirements.txt

# This makes port 80 available to the world outside this container
EXPOSE 80

# Here we define environment variable which we will be passing at Runtime
ENV NAME ""

# At last, run myapp.py when the container launches
CMD ["python", "myapp.py"]