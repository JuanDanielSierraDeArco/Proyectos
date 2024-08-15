FROM  python:3.12

WORKDIR /app
COPY . /app

RUN pip install --no-cache-dir --upgrade -r /app/requirements.txt

CMD bash -c "while true; do sleep 1; done"