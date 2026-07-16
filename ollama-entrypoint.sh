#!/bin/bash

# Start the Ollama server in the background
ollama serve &

# Wait for Ollama server to be ready
echo "Waiting for Ollama server to start..."
until ollama list >/dev/null 2>&1; do
  sleep 1
done

# Pull the models
echo "Pulling llama3.2:latest..."
ollama pull llama3.2:latest

echo "Pulling mxbai-embed-large:latest..."
ollama pull mxbai-embed-large:latest

echo "Models pulled successfully! Keeping Ollama server running..."

# Wait for the background processes to finish (keeping container alive)
wait
