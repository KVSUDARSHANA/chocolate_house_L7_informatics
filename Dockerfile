# Use the official Python image
FROM python:3.9-slim

# Set the working directory in the container
WORKDIR /app

# Copy requirements.txt to the working directory
COPY requirements.txt .

# Install the dependencies
RUN pip install -r requirements.txt

# Copy the entire project into the container
COPY . .

# Run the sample data initialization script
RUN python chocolate_house.py

# Expose the port Flask will run on
EXPOSE 5000

# Run the Flask application
CMD ["python", "app.py"]
