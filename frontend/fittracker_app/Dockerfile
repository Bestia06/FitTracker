# Build stage
FROM ubuntu:20.04 AS build

# Avoid warnings by switching to noninteractive
ENV DEBIAN_FRONTEND=noninteractive

# Install dependencies
RUN apt-get update && apt-get install -y \
    curl \
    git \
    unzip \
    xz-utils \
    zip \
    libglu1-mesa \
    openjdk-11-jdk \
    && rm -rf /var/lib/apt/lists/*

# Set up new user
RUN useradd --create-home --shell /bin/bash developer
USER developer
WORKDIR /home/developer

# Copy the app files to the container
COPY --chown=developer:developer . .

# Get Flutter
RUN git clone https://github.com/flutter/flutter.git
ENV PATH="$PATH:/home/developer/flutter/bin"

# Enable web
RUN flutter channel stable
RUN flutter upgrade
RUN flutter config --enable-web

# Get app dependencies
RUN flutter pub get

# Build the app for the web
RUN flutter build web

# Production stage
FROM nginx:alpine

# Copy the built app from the build stage
COPY --from=build /home/developer/build/web /usr/share/nginx/html

# Copy nginx configuration
COPY nginx.conf /etc/nginx/nginx.conf

# Expose port 80
EXPOSE 80

# Start nginx
CMD ["nginx", "-g", "daemon off;"]
