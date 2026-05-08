#!/bin/bash

# Update system
yum update -y

# Install Docker
yum install -y docker

# Start Docker service
systemctl start docker
systemctl enable docker

# Add ec2-user to docker group
usermod -aG docker ec2-user

# Pull latesyourdockt image from Docker Hub
docker pull taiwopeterolatunji/devops-app:latest

# Run container
docker run -d -p 5000:5000 --name devops-container yourdockerhubusername/devops-app:latest