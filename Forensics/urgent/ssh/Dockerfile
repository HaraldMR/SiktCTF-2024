# Dockerfile for the web server with SSH logs
FROM ubuntu:latest
RUN apt-get update && \
    apt-get install -y openssh-server && \
    mkdir /var/run/sshd && \
    echo 'root:root' | chpasswd
RUN useradd -m ctfuser && \
    echo 'ctfuser:ctfuser' | chpasswd && \
    mkdir /home/ctfuser/.logs
COPY auth.log /home/ctfuser/.logs/auth.log
EXPOSE 22
CMD service ssh start && tail -f /dev/null
