FROM python:3.10.5-bullseye

RUN useradd -m ctf

WORKDIR /home/ctf

RUN apt-get update && \
    apt-get install -y lib32z1 xinetd && \
    rm -rf /var/lib/apt/lists/* && \
    echo "Connection banned." > /etc/banner_fail

RUN pip3 install pycryptodome

COPY ctf.xinetd /etc/xinetd.d/ctf
COPY challenge.py start.sh secret.py ./

RUN chmod +x /home/ctf/start.sh && \
    chown -R root:ctf /home/ctf && \
    chmod -R 750 /home/ctf

CMD ["/home/ctf/start.sh"]

EXPOSE 7272

# docker build --tag knapsack .
# docker run -d --publish 7272:7272 --name knapsack knapsack
