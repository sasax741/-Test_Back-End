# Start from the Python base image
FROM python:3.8-alpine AS python_base

# Install necessary build dependencies
RUN apk add --no-cache \
    build-base \
    gcc \
    musl-dev \
    gfortran \
    openblas-dev \
    lapack-dev

# Set the working directory in the container
WORKDIR /app


# Install Python dependencies
RUN pip install flask psycopg2-binary numpy flask_basicauth



# Copy the rest of your application code
COPY . .

# Command to run your application
CMD ["python", "app.py"]






