FROM python:3-alpine3.22

WORKDIR /usr/local/build

COPY . .

RUN pip install --no-cache-dir --upgrade pip setuptools wheel build
RUN python -m build --wheel --outdir dist/
RUN pip install dist/*.whl

CMD ["/bin/sh"]