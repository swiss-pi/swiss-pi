#* Installation process is provided by: https://github.com/instrumentisto/nmap-docker-image
#* Thank you intrumentisto ♥

# https://hub.docker.com/_/alpine
#FROM alpine:3.23
FROM python:3.10.10-alpine

ARG nmap_ver=7.98
ARG build_rev=2


# Install dependencies.
RUN apk add --update --no-cache \
            ca-certificates \
            libgcc libstdc++ \
            libcrypto3 libssl3 \
            libpcap \
            libssh2 \
            lua5.4-libs \
            zlib \
 && update-ca-certificates \
 && rm -rf /var/cache/apk/*


# Compile and install Nmap from sources.
RUN apk add --update --no-cache --virtual .build-deps \
        linux-headers \
        openssl-dev \
        libpcap-dev \
        libssh2-dev \
        lua5.4-dev \
        pcre-dev \
        zlib-dev \
        autoconf automake g++ libtool make \
        curl \
    \
 && curl -fL -o /tmp/nmap.tar.bz2 \
         https://nmap.org/dist/nmap-${nmap_ver}.tar.bz2 \
 && tar -xjf /tmp/nmap.tar.bz2 -C /tmp \
 && cd /tmp/nmap* \
 # Fix `strlcat` type conflict. See Alpine patch for details:
 # https://gitlab.alpinelinux.org/alpine/aports/-/merge_requests/83849
 && sed -i '22,25d' libdnet-stripped/acconfig.h \
 && autoreconf libpcre libdnet-stripped -ivf \
 && ./configure \
        --prefix=/usr \
        --sysconfdir=/etc \
        --mandir=/usr/share/man \
        --infodir=/usr/share/info \
        --without-zenmap \
        --without-nmap-update \
        --with-liblua=/usr/lua5.4 \
        --with-libpcap=yes \
        --with-libpcre=yes \
        --with-libssh2=yes \
        --with-libz=yes \
        --with-openssl=yes \
 && make \
 && make install \
    \
 && apk del .build-deps \
 && rm -rf /var/cache/apk/* \
           /tmp/nmap* \
#* --- Here starts my own code --- 
&& mkdir -p /nmap

RUN apk add --no-cache wget && \
    apk add --no-cache build-base libffi-dev && \
    apk add python3 py3-pip gcc musl-dev

RUN pip install --no-cache-dir --upgrade pip
COPY requirements.txt .
#//
RUN pip install --no-cache-dir -r requirements.txt

WORKDIR /app
COPY nmap.json .
COPY nmap.lastknowngood.json .
COPY nmapscript.py .
RUN chmod 700 nmapscript.py

ENTRYPOINT [ "python3", "./nmapscript.py" ]


#SSByZWFsbHkgc2hvdWxkIGdldCBiZXR0ZXIgaW4gRG9ja2VyCg==
