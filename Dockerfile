# Define the Image with the python version
FROM python:3.9-slim-buster

# Create a directory in the docker container
WORKDIR ./backend

# Copy the requirements.txt into previously created directory on the docker container from the local one
COPY requirements.txt requirements.txt

RUN echo "web: gunicorn core.wsgi --log-file -" >> Procfile
RUN echo "python-3.9.5" >> runtime.txt   
RUN pip3 install gunicorn
RUN pip3 install -U pip

# Run the requirements.txt from the previously created directory on the docker container
RUN pip3 install -r requirements.txt

# Copy all files from local directory to the previously created directory on the docker container
COPY . .

RUN python3 manage.py collectstatic

# Run the django project from the previously created directory on the docker container then,
# Make the project from the previously created directory on the docker container accessible to the main computer using the ip and port number
CMD [ "python3", "manage.py", "runserver", "0.0.0.0:8000" ]