#!/bin/bash

# Function to check if the user is logged into GitHub Container Registry
check_docker_login() {
    if docker info | grep -q "ghcr.io"; then
        echo "Already logged in to GitHub Container Registry."
        return 0
    else
        return 1
    fi
}

# Prompt for login if not already logged in
if ! check_docker_login; then
    echo "You are not logged in to GitHub Container Registry."
    read -p "GitHub Username: " username
    read -sp "GitHub Personal Access Token: " token
    echo

    # Perform Docker login
    echo $token | docker login ghcr.io -u $username --password-stdin
    if [ $? -ne 0 ]; then
        echo "Failed to log in to GitHub Container Registry."
        exit 1
    fi
fi

# Variables (replace with your image details)
IMAGE_NAME=$(basename "$PWD")
IMAGE_TAG="latest"
GITHUB_REPO="ghcr.io/$username/$IMAGE_NAME"

# Build the Docker image
docker build -t $GITHUB_REPO:$IMAGE_TAG .

# Push the image to GitHub Container Registry
docker push $GITHUB_REPO:$IMAGE_TAG

if [ $? -eq 0 ]; then
    echo "Docker image pushed successfully!"
else
    echo "Failed to push the Docker image."
    exit 1
fi
