# Production Dockerfile for hydrocomplex
# Build:  docker build -t hydrocomplex .
# Run:    docker run --rm hydrocomplex
# Override command: docker run --rm hydrocomplex hydrocomplex metrics --obs obs.csv --sim sim.csv

FROM python:3.12-slim

# Keeps Python from generating .pyc files and enables unbuffered stdout/stderr
ENV PYTHONDONTWRITEBYTECODE=1 \
    PYTHONUNBUFFERED=1

WORKDIR /app

# Install build dependencies in a single layer, then remove cache
COPY pyproject.toml README.md ./
COPY src/ ./src/

RUN pip install --no-cache-dir --upgrade pip \
 && pip install --no-cache-dir .

# Default: print help (safe neutral command; override as needed)
CMD ["hydrocomplex", "--help"]
