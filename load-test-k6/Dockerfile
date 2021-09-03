## Start of your normal docker file 
FROM oraclelinux:7-slim

# Install hotwrap binary in your container 
COPY --from=fnproject/hotwrap:latest  /hotwrap /hotwrap

# Install K6
RUN yum install wget -y && \
    wget https://github.com/grafana/k6/releases/download/v0.33.0/k6-v0.33.0-linux-amd64.rpm && \
    yum localinstall /k6-v0.33.0-linux-amd64.rpm -y && \
    groupadd --gid 1000 fn && \
    adduser --uid 1000 --gid fn fn

# Transfer test script
ADD script.js /
ADD run-k6.sh /

# Change file permission
RUN chmod 777 /script.js && \
    chmod 777 /run-k6.sh

# Execute load test
CMD "/run-k6.sh"

ENTRYPOINT ["/hotwrap"]

