# Base image
FROM python:3.11-slim

# Copy to app dir
COPY . /app

# Change dir
WORKDIR /app

# Install dependencies
RUN pip install -r requirements.txt

# Make port 5003 available to the world outside this container
EXPOSE 5003

# Start cmd
CMD [ "python", "app.py" ]