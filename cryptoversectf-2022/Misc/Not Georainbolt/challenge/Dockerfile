FROM python:3.9-slim-buster
WORKDIR /home/ctf
RUN useradd -m ctf
RUN apt-get update && \
    apt-get install -y lib32z1 xinetd && \
    echo "Connection banned." > /etc/banner_fail
RUN pip3 install pycryptodome

RUN cp -R /lib* /home/ctf && \
    cp -R /usr/lib* /home/ctf
RUN mkdir /home/ctf/dev && \
    mknod /home/ctf/dev/null c 1 3 && \
    mknod /home/ctf/dev/zero c 1 5 && \
    mknod /home/ctf/dev/random c 1 8 && \
    mknod /home/ctf/dev/urandom c 1 9 && \
    chmod 666 /home/ctf/dev/*
RUN mkdir /home/ctf/bin && \
    cp /bin/sh /home/ctf/bin && \
    cp /bin/ls /home/ctf/bin && \
    cp /bin/cat /home/ctf/bin

COPY ./ctf.xinetd /etc/xinetd.d/ctf
COPY . .
RUN chmod +x /home/ctf/start.sh && \
    chmod +x /home/ctf/result.csv && \
    chown -R root:ctf /home/ctf && \
    chmod -R 750 /home/ctf

CMD ["/home/ctf/start.sh"]

EXPOSE 9999

# docker build --tag rain .
# docker run -d --publish 22606:9999 --name rain rain
# docker run --rm --publish 22606:9999 --name rain rain