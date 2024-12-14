FROM python:3.13-slim

# Install system dependencies
RUN apt-get update && apt-get install -y \
    build-essential \
    cmake \
    cargo \
    rustc \
    g++ \
    libopenblas-dev \
    liblapack-dev \
    && rm -rf /var/lib/apt/lists/*

WORKDIR /app

COPY requirements.txt .

# Set environment variables to help with BLAS detection
ENV OPENBLAS_NUM_THREADS=1
ENV GOTO_NUM_THREADS=1
ENV OMP_NUM_THREADS=1

RUN pip install --no-cache-dir -r requirements.txt

ENTRYPOINT ["jupyter"]

CMD ["notebook", "--ip=0.0.0.0", "--allow-root"]
