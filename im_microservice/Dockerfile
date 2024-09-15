# Use the official Python image from the Docker Hub
FROM python:3.10

# Set the working directory inside the container
WORKDIR /app

# Copy the current directory contents into the container at /app
COPY . .

# Install any dependencies specified in requirements.txt
RUN pip install --no-cache-dir -r requirements.txt

# Make the container's port 5000 available to the outside world
EXPOSE 5000

# Define environment variables
ENV LINE_CHANNEL_ACCESS_TOKEN=""

# Run app.py when the container launches
CMD ["python", "app.py"]
