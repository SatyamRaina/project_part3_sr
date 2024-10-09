# Use the official python:3.11 image based on alpine as the base image
FROM python:3.11-alpine

# Sets the working directory inside the container to /inventory_management
WORKDIR /inventory_management

# Copy the requirements.txt file from the host system to the container in /inventory_management/
COPY requirements.txt .

# Install the necessary Python packages from the requirements.txt file
# The --no-cache-dir option prevents caching of package files to reduce the image size
RUN pip install --no-cache-dir -r requirements.txt

# Copy the remaining application files from the host system to the container in the working directory
COPY . .

# Expose port 8001 so that it can be accessed outside the container
EXPOSE 8001

# Run the uvicorn server with the app "main:app", listening on all interfaces (0.0.0.0) and port 8001
CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "8001"]
