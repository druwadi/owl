FROM ubuntu:latest

COPY collector/collector.py linux_build/metrics-monitoring.zip /usr/build/

# Setup base packages
RUN apt-get update -y \
    && apt-get install python3 -y \
    && apt-get install python3-pip -y \
    && apt-get install unzip \
    && apt-get install curl -y \
    && apt-get install vim -y 

# Build collector for Linux
RUN cd /usr/build/ \
    && unzip metrics-monitoring.zip \
    && cd metrics-monitoring \
    && pip3 install -r requirements.txt \
    && pip3 install pyinstaller \
    && pyinstaller /usr/build/collector.py --onefile \
    && cp /usr/build/metrics-monitoring/dist/collector /bin/collector

CMD ["/bin/collector"]