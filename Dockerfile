FROM python:3.12-slim

ENV PYTHONUNBUFFERED=1 \
  PYTHONDONTWRITEBYTECODE=1 \
  UV_VERSION=0.5.0

RUN apt-get update && apt-get install -y --no-install-recommends \
  curl \
  build-essential \
  libffi-dev \
  libssl-dev \
  && apt-get clean && rm -rf /var/lib/apt/lists/*

RUN curl -LsSf https://astral.sh/uv/install.sh | sh -s -- -v $UV_VERSION

ENV PATH="/root/.local/bin:$PATH"

WORKDIR /app

COPY . .

EXPOSE 10000

ENTRYPOINT [ "uv", "run", "streamlit", "run", "src/ui/main.py", "--server.port=10000", "--server.address=0.0.0.0"]
