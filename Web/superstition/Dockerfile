# Use Ubuntu as the base image
FROM ubuntu:22.04
ARG DEBIAN_FRONTEND=noninteractive

# Install necessary packages
RUN apt-get update && \
    apt-get install -y apache2 php libapache2-mod-php && \
    rm -rf /var/lib/apt/lists/*

COPY web/ /var/www/html/

# Add a new user with a password and copy the flag file
RUN useradd -m -p $(openssl passwd -1 iwanttobeninja) flaguser
RUN chmod 755 /home/flaguser
COPY flag.txt /home/flaguser/flag.txt
RUN chmod 644 /home/flaguser/flag.txt
RUN chmod 644 /etc/passwd

RUN sed -i 's/DirectoryIndex index.html/DirectoryIndex index.php index.html/' /etc/apache2/mods-enabled/dir.conf

# Expose port 80
EXPOSE 80

# Start Apache in the foreground
CMD ["apachectl", "-D", "FOREGROUND"]
