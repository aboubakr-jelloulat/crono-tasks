#!/bin/bash



# If image doesn't exist or user passes "build" argument, build first
if [[ "$(docker images -q my-cli-app 2>/dev/null)" == "" || "$1" == "build" ]]; then
    echo "🔨 Building Docker image..."
    docker build -t my-cli-app .
fi

echo "🚀 Running Crono CLI..."
docker run -it my-cli-app