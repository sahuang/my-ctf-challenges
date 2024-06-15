FROM pwn.red/jail

# python:3.12.1-slim-bookworm
COPY --from=python@sha256:db7e9284d53f7b827c58a6239b9d2907c33250215823b1cdb7d1e983e70dafa5 / /srv

COPY challenge.py /srv/app/run
RUN chmod 755 /srv/app/run

ENV JAIL_PORT=7270