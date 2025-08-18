FROM python:3.12-slim

RUN apt-get update \
    && apt-get install -y --no-install-recommends \
        gcc \
        libc-dev \
        libssl-dev \
        libffi-dev \
        curl \
    && apt-get clean \
    && rm -rf /var/lib/apt/lists/*

WORKDIR /app

COPY ./app.py /app
COPY ./tests /app/tests
RUN pip install --upgrade pip
RUN pip install aiohttp uvicorn fastapi requests 'dramatiq[redis]' pytest pytest-asyncio httpx

EXPOSE 8000

CMD ["uvicorn", "app:app", "--host", "0.0.0.0", "--port", "8000", "--reload"]
