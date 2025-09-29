# Use an official Python runtime as a parent image
FROM python:3.12-slim

# Install Node.js and npm, then the AWS CDK
RUN apt-get update && \
    apt-get install -y nodejs npm && \
    npm install -g aws-cdk

# Set the working directory in the container
WORKDIR /usr/src/app

# Copy the requirements file and install dependencies
COPY requirements.txt ./
RUN pip install --no-cache-dir -r requirements.txt

# Copy the rest of the application's code
COPY . .

# Synthesize the CDK app
CMD ["cdk", "synth"]

