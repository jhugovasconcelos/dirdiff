# Use Alpine Linux as base image for smaller footprint
FROM python:3-alpine3.22

# Install system dependencies required for building Python packages
RUN apk add --no-cache \
    git \
    gcc \
    musl-dev \
    linux-headers \
    libffi-dev \
    openssl-dev \
    build-base \
    && rm -rf /var/cache/apk/*

# Set working directory
WORKDIR /usr/local/build

# Copy the repository
COPY . .

# Upgrade pip and install build dependencies
RUN pip install --no-cache-dir --upgrade pip setuptools wheel build

# Install package dependencies if requirements.txt exists
RUN if [ -f requirements.txt ]; then pip install --no-cache-dir -r requirements.txt; fi

# Build the package
RUN python -m build --wheel --outdir dist/

# Optional: Install the built package for testing
RUN pip install dist/*.whl

CMD ["/bin/sh"]