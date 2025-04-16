FROM python:3.13-slim

WORKDIR /app

# Copy the Python script
COPY index.py .

# Install pytest
RUN pip install --no-cache-dir pytest

# Command to run the application
CMD ["python", "index.py"]
