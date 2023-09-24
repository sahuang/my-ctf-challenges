FROM gcr.io/paradigmxyz/ctf/base:latest

COPY requirements.txt /root

RUN python3 -m pip install -r /root/requirements.txt 

RUN true \
    && curl -L https://foundry.paradigm.xyz | bash \
    && bash -c "source /root/.bashrc && foundryup" \
    && chmod 755 -R /root \
    && true

COPY 98-start-gunicorn /startup

COPY eth_sandbox /usr/lib/python/eth_sandbox

ENV PYTHONPATH=/usr/lib/python
ENV FLAG=vsctf{15_ZKP_s0lvable_0r_MetaTrust==MetaDistrust?}
ENV SHARED_SECRET=A0^POjpxC$r&22
ENV PUBLIC_IP=172.86.96.174
ENV HTTP_PORT=8545
ENV PORT=1337

COPY deploy/ /home/ctf/

COPY contracts /tmp/contracts
COPY foundry.toml /tmp/foundry.toml

RUN true \
    && cd /tmp \
    && /root/.foundry/bin/forge init --force --no-commit \
    && /root/.foundry/bin/forge build --out /home/ctf/compiled \
    && rm -rf /tmp/contracts \
    && true

# docker build --tag zkp . && docker run -d -p 1337:1337 -p 8545:8545 --name zkp zkp