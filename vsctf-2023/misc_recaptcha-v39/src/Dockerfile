FROM python:3.9-slim-buster

RUN pip3 install requests aiohttp aiodns pillow shades

WORKDIR /app
COPY app .

CMD ["python3", "-u", "-m", "aiohttp.web", "-H", "0.0.0.0", "-P", "8000", "server:init"]