# Use a specific, slim base image for reproducibility and smaller size
FROM python:3.8-slim-buster

# Set the working directory
WORKDIR /app
COPY . /app
RUN apt update -y && apt install awscli -y

# Install Python dependencies without storing cache
RUN pip install -r requirements.txt

# Now copy the rest of the application source code
# This layer will be rebuilt on any code change, but dependencies remain cached


# Define the command to run your application
CMD ["python3", "app.py"]