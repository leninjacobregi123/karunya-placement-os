FROM node:20-slim

# Install Python 3 and curl (for downloading/checking Ollama and executing tests)
RUN apt-get update && apt-get install -y python3 python3-pip curl && rm -rf /var/lib/apt/lists/*

# Set working directory to /app
WORKDIR /app

# Copy the package files first to leverage caching
COPY ui/package*.json ./ui/

# Install Next.js dependencies
RUN cd ui && npm ci

# Copy the rest of the application code
COPY . .

# Build Next.js application
RUN cd ui && npm run build

# Expose port
EXPOSE 3000

# Set production environment variables
ENV NODE_ENV=production
ENV PORT=3000
ENV OLLAMA_URL=http://ollama:11434

# Start Next.js server
CMD ["npm", "--prefix", "ui", "start"]
