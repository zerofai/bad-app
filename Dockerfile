# Use an official Python runtime as the base image
FROM python:3.12.2-bullseye

# Set the working directory in the container
WORKDIR /app

# Copy the requirements file to the container
COPY requirements.txt .

# Install the dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Copy the python code and html to the container
COPY app.py login.html .

# Expose the container port
EXPOSE 5000

# Set the entrypoint command
CMD [ "python", "app.py" ]
