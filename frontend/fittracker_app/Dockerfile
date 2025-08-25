# Build stage
FROM ubuntu:22.04 AS build

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
    wget \
    && rm -rf /var/lib/apt/lists/*

# Set up new user
RUN useradd --create-home --shell /bin/bash developer
USER developer
WORKDIR /home/developer

# Download Flutter SDK directly (more reliable than git clone)
RUN wget -O flutter.tar.xz https://storage.googleapis.com/flutter_infra_release/releases/stable/linux/flutter_linux_3.19.6-stable.tar.xz \
    && tar xf flutter.tar.xz \
    && rm flutter.tar.xz

ENV PATH="$PATH:/home/developer/flutter/bin"

# Copy the app files to the container
COPY --chown=developer:developer . .

# Pre-download Flutter dependencies
RUN flutter precache

# Enable web
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
