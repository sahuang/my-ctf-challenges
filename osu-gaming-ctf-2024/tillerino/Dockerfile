# python:3.12.1-slim-bookworm
FROM python@sha256:85e668ed5c6219f9fd1a70d12103b6c8b2cfbdca971d045cdafc301c061c049d as app
RUN python3 -m pip install --no-cache openai

FROM pwn.red/jail
COPY --from=app / /srv
COPY hook.sh /jail/hook.sh

COPY server.py /srv/app/run
RUN chmod 755 /srv/app/run

ENV JAIL_ENV_OPENAI_KEY="REDACTED" JAIL_PORT=7271 JAIL_PIDS=20 JAIL_TIME=45 JAIL_MEM=75M JAIL_POW=7500 JAIL_CPU=200