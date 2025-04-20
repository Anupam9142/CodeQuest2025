FROM python:3.10-alpine

# Socat needs to be installed for communication with the sidecar
RUN apk add socat

# This directory needs to exist
RUN mkdir -p /codequest

# Copy all files in the image
COPY src /codequest/src

# Copy run.sh
COPY run.sh /codequest
RUN chmod +x /codequest/run.sh

WORKDIR /codequest

RUN pip install -r src/requirements.txt

CMD ["/bin/sh", "-c", "./run.sh"]