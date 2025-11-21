FROM python:3.14.0-alpine3.21
ARG VERSION="0.1.14"

RUN pip install --no-cache-dir --upgrade pip && \
    pip install --no-cache-dir defectdojo-cli2==${VERSION}

CMD ["/usr/local/bin/defectdojo"]
