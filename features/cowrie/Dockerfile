FROM alpine:3.21

RUN apk add --no-cache \
    git \
    python3 \
    py3-pip \
    py3-virtualenv \
    py3-cryptography \
    build-base \
    libffi-dev \
    openssl-dev \
    python3-dev

RUN addgroup -g 1000 cowrie && \
    adduser -u 1000 -G cowrie -D -h /cowrie cowrie

USER cowrie
WORKDIR /cowrie

RUN mkdir cowrie-git && git clone --branch v3.1.7 --depth 1 https://github.com/cowrie/cowrie.git cowrie-git
WORKDIR /cowrie/cowrie-git

RUN python3 -m venv --system-site-packages cowrie-env && \
    cowrie-env/bin/pip install --upgrade pip && \
    cowrie-env/bin/pip install .

EXPOSE 2222 2223
CMD ["/cowrie/cowrie-git/cowrie-env/bin/twistd", "-n", "--umask=0022", "--pidfile=", "--logger=cowrie.python.logfile.logger", "cowrie"]