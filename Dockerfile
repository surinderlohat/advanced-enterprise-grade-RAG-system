# -------------------------------
# Base Image
# -------------------------------
FROM python:3.12-slim

# -------------------------------
# Environment Settings
# -------------------------------
ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1

# -------------------------------
# System Dependencies
# -------------------------------
RUN apt-get update && apt-get install -y \
    build-essential \
    curl \
    && rm -rf /var/lib/apt/lists/*

# -------------------------------
# Working Directory
# -------------------------------
WORKDIR /app

# -------------------------------
# Install Python Dependencies
# -------------------------------
COPY requirements.txt .
RUN pip install --upgrade pip \
    && pip install --no-cache-dir -r requirements.txt

# -------------------------------
# Copy Application Code
# -------------------------------
COPY . .

# -------------------------------
# Expose Port (optional – future API)
# -------------------------------
EXPOSE 8000

# -------------------------------
# Run Application
# -------------------------------
CMD ["python", "app.py"]
