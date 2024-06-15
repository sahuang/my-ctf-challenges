FROM python:3.9-slim-buster

WORKDIR /app

RUN apt-get update && apt-get install -y ffmpeg
RUN pip3 install requests aiohttp aiodns pillow matplotlib torchaudio transformers torch scipy numpy pydub azure-cognitiveservices-vision-computervision

COPY . .

ENV VISION_KEY=
ENV VISION_ENDPOINT=

CMD ["python3", "-m", "aiohttp.web", "-H", "0.0.0.0", "-P", "8000", "server:init"]

# docker build --tag miku . && docker run -d --publish 22528:8000 --name miku miku