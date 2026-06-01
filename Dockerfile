FROM python:3.11-slim

WORKDIR /app

# system dependencies for PDF + OCR + ML builds
RUN apt-get update && apt-get install -y \
    poppler-utils \
    tesseract-ocr \
    build-essential \
    gcc \
    g++ \
    && rm -rf /var/lib/apt/lists/*

COPY requirements.txt .

# upgrade pip tools
RUN pip install --upgrade pip setuptools wheel

# install torch separately (important for stability)
RUN pip install torch torchvision --index-url https://download.pytorch.org/whl/cpu

# install remaining python dependencies
RUN pip install --no-cache-dir -r requirements.txt

COPY . .

EXPOSE 8501

CMD ["streamlit", "run", "app/app.py", "--server.address=0.0.0.0"]
