FROM ubuntu:20.04

RUN apt-get update -y && \
    apt-get install -y python3-pip python3-dev ncat curl opam

RUN opam init --yes --disable-sandboxing

WORKDIR /app

COPY . /app

RUN chmod -R 555 /app

USER 1000:1000

CMD ncat -klvp 4201 -m 999999 -e /bin/ocaml