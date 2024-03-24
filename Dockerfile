FROM python:3.8.2

COPY .  /app
WORKDIR /app

RUN sed -i -E 's/deb.debian.org/mirror.kakao.com/' /etc/apt/sources.list
RUN dpkg --add-architecture i386 && apt update && apt install -y wine wine32 && rm -rf /var/lib/apt/lists/*

RUN pip3 install zugbruecke
RUN pip3 install flask

RUN python -c 'import zugbruecke; zugbruecke.windll.LoadLibrary("fcrypt_es.dll")'

CMD ["python3", "app.py"]
