# Dockerfile for the FTP server
FROM ubuntu:latest

# Install vsftpd
RUN apt-get update && \
    apt-get install -y vsftpd && \
    mkdir -p /var/run/vsftpd/empty /home/ftp

# Configure vsftpd
RUN echo "listen=YES" >> /etc/vsftpd.conf && \
    echo "listen_ipv6=NO" >> /etc/vsftpd.conf && \
    echo "anonymous_enable=YES" >> /etc/vsftpd.conf && \
    echo "anon_root=/home/ftp" >> /etc/vsftpd.conf && \
    echo "no_anon_password=YES" >> /etc/vsftpd.conf && \
    echo "pasv_min_port=10000" >> /etc/vsftpd.conf && \
    echo "pasv_max_port=10010" >> /etc/vsftpd.conf && \
    echo "pasv_address=127.0.0.1" >> /etc/vsftpd.conf && \
    echo "port_enable=YES" >> /etc/vsftpd.conf && \
    echo "Remember your ftp server!" > /home/ftp/readme.txt

# Add the flag file
COPY flag.txt /home/ftp/flag.txt

# Expose FTP and passive mode ports
EXPOSE 21 10000-10010

# Start vsftpd service
CMD /usr/sbin/vsftpd /etc/vsftpd.conf
