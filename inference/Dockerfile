FROM python:3.9

COPY requirements.txt .
RUN pip install -r requirements.txt

EXPOSE 8000
WORKDIR /app



CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "8000"]