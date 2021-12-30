FROM python:3.9-slim

WORKDIR /app

RUN apt-get -qq update -y && apt-get --no-install-recommends -y install vim procps
RUN pip install --upgrade pip

ENV PYTHONPATH "${PYTHONPATH}:/app"

EXPOSE 8000

COPY requirements.txt .
RUN pip3 install -r requirements.txt

COPY . .

RUN chmod 777 /app/deploy/docker_entrypoint.sh
CMD ["python3", "src/main.py"]
