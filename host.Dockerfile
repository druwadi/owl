FROM ubuntu:latest

# Work around until I setup a runner to build the linux version, copies repo in.
COPY . /usr/build/

# Setup base packages
RUN apt-get update -y \
    && apt-get install python3 -y \
    && apt-get install python3-pip -y \
    && apt-get install curl -y 

# Build collector for Linux
RUN cd /usr/build/ \
    && pip3 install -r requirements.txt \
    && pip3 install pyinstaller \
    && pyinstaller /usr/build/collector/collector.py --onefile \
    && cp /usr/build/dist/collector /bin/collector

CMD ["/bin/collector"]