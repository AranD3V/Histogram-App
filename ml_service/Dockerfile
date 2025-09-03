# Stage 1: Use an official Python runtime as a parent image
FROM python:3.9-slim

# Set the working directory in the container
WORKDIR /app

# Copy the requirements file into the container
COPY requirements.txt .

# Install any needed packages specified in requirements.txt
RUN pip install --no-cache-dir -r requirements.txt

# Copy the rest of the application source code
COPY . .

# Expose port 5000 to the outside world
EXPOSE 5000

# Run app.py when the container launches
# Use gunicorn in a real production setup for a more robust server
CMD ["python", "app.py"]
