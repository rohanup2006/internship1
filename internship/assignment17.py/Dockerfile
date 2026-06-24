FROM python:3.11.18-slim

RUN apt-get update && apt-get install -y openjdk-21-jre-headless

ENV JAVA_HOME=/usr/lib/jvm/java-21-openjdk-amd64
ENV PATH=$JAVA_HOME/bin:$PATH

RUN pip install pyspark pandas

WORKDIR /app

COPY . .

CMD ["python", "app.py"]