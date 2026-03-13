FROM hub.dglive.net/internal/python:dev-3.13
ARG VERSION="0.1.19"
RUN pip install --no-cache-dir --upgrade pip  && \
    pip install --no-cache-dir defectdojo-cli2==${VERSION}
CMD ["/usr/local/bin/defectdojo"]
