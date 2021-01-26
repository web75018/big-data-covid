FROM spark-base

RUN pip3 install pyspark && \
    pip3 install kafka-python && \
    mkdir /usr/bin/submit/ && \
    mkdir /opt/spark-apps

COPY submit.sh /usr/bin/submit/

ENTRYPOINT [ "/usr/bin/submit/submit.sh" ]