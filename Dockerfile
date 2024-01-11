FROM python:latest

WORKDIR /app


RUN apt-get update && \
    apt-get install -y \
    python3-tk \
    libmysqlclient-dev \
    && rm -rf /var/lib/apt/lists/*

COPY requirements.txt .

RUN pip install --upgrade pip && \
    pip install --no-cache-dir -r requirements.txt

COPY . .

CMD ["python", "GroceryManagement.py"]
