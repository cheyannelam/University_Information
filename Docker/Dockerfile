# Use an official Python runtime as a parent image
FROM python:3.8-slim

# Set the working directory in the container to /app
WORKDIR /app

# Install system dependencies required for pip package compilation
RUN apt-get update && apt-get install -y \
    gcc \
    build-essential \
    libffi-dev \
    && apt-get clean \
    && rm -rf /var/lib/apt/lists/*

# Copy the requirement.txt file into the container at /app
COPY requirement.txt /app/

# Upgrade pip and install any needed packages specified in requirements.txt
RUN pip install --upgrade pip && pip install --no-cache-dir -r requirement.txt

# Copy the rest of your application's code into the container at /app
COPY . /app

# Make port 8501 available to the world outside this container
EXPOSE 8501

# Run app.py when the container launches
CMD ["streamlit", "run", "1_Home.py", "--server.port=8501", "--server.address=0.0.0.0"]
