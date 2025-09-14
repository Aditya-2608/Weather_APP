# Use official Python image
FROM python:3.11-slim

# Set working dir
WORKDIR /app

# Install dependencies
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copy project files
COPY . .

# Expose port
EXPOSE 10000

# Gunicorn command (Render expects web service on $PORT)
CMD ["gunicorn", "-b", "0.0.0.0:10000", "app:app"]
