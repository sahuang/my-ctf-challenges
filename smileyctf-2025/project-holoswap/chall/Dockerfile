FROM python:3.10.12-slim-buster

RUN useradd -m ctf

WORKDIR /home/ctf

RUN apt-get update && \
    apt-get install -y lib32z1 xinetd && \
    rm -rf /var/lib/apt/lists/* && \
    echo "Connection banned." > /etc/banner_fail

RUN pip3 install numpy tensorflow pillow

COPY ctf.xinetd /etc/xinetd.d/ctf
COPY server.py start.sh model.h5 gura.png ./

RUN chmod +x /home/ctf/start.sh && \
    chown -R root:ctf /home/ctf && \
    chmod -R 750 /home/ctf

ENV PYTHONUNBUFFERED=1
ENV FLAG=".;,;.{Graduation_is_not_the_end_samekosaba_:eyes:}"

CMD ["/home/ctf/start.sh"]

EXPOSE 1337

# docker build --tag gura . && docker run -d --publish 12345:1337 --name gura gura