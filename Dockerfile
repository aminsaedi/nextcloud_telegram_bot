FROM python:alpine

# Install dependencies from requirements.txt
COPY requirements.txt /app/requirements.txt
RUN pip install -r /app/requirements.txt

# Copy the rest of the code
COPY . /app

# Set the working directory to /app
WORKDIR /app

# Run the app
CMD ["python", "main.py"]

