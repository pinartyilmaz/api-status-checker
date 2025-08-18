Async URL Status Checker - FastAPI

A basic FastAPI service that checks the HTTP status codes of multiple URLs concurrently using aiohttp and asyncio.

Features

Accepts a list of URLs via a POST request

Returns the HTTP status code for each URL

Fully asynchronous for fast concurrent requests

Installation
1. clone the repository
2. cd fetcher
3. docker compose up --build