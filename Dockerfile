#Dockerfile
FROM python:3.11-slim

#Set working directory
WORKDIR /app

#Install dependencies
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

#Copy app code
COPY . .

#Launch with Gunicorn on port 8080
EXPOSE 8080
CMD ["gunicorn", "--bind", "0.0.0.0:8080", "app.main:app"]
