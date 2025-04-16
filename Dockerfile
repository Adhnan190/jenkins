FROM python:3.13-slim

WORKDIR /app

# Copy the Python script
COPY index.py .

# Create an empty requirements.txt file (or add your dependencies if needed)
RUN echo "" > requirements.txt
RUN pip install --no-cache-dir -r requirements.txt

# Command to run the application
CMD ["python", "index.py"]