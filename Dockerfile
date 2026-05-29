FROM python:3.11-slim

WORKDIR /app

# system dependencies (IMPORTANT for OCR + pdf2image)
RUN apt-get update && apt-get install -y \
    poppler-utils \
    tesseract-ocr \
    && rm -rf /var/lib/apt/lists/*

# upgrade pip first
RUN pip install --upgrade pip

COPY requirements.txt .

RUN pip install --no-cache-dir -r requirements.txt

COPY . .

EXPOSE 8501

CMD ["streamlit", "run", "app/app.py", "--server.address=0.0.0.0"]
