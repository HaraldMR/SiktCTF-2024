# Use a minimal base image
FROM debian:latest

# Install necessary packages
RUN apt-get update && apt-get install -y \
    rsync \
    openssh-server \
    sudo \
    whois \
    && rm -rf /var/lib/apt/lists/*

# Create a user for rsync
RUN useradd -m -s /bin/bash ted && echo "ted:grape" | chpasswd

# Create directories for shared folders
RUN mkdir -p /shared/open /shared/protected

# Set permissions for the open folder (no password)
RUN chown -R ted:ted /shared/open && chmod -R 755 /shared/open

# Set up the protected folder with a password and place the flag
COPY flag.txt /shared/protected/flag.txt
RUN chown -R ted:ted /shared/protected && chmod -R 555 /shared/protected
COPY hash.txt /shared/open/password_hash.txt
COPY users /shared/open/users

# Configure rsync daemon
COPY rsyncd.secrets /etc/rsyncd.secrets 
RUN chmod 600 /etc/rsyncd.secrets

# Configuration for the protected folder (requires authentication)
COPY rsyncd.conf /etc/rsyncd.conf

# Expose rsync port
EXPOSE 873

# Start the rsync daemon
CMD ["rsync", "--daemon", "--no-detach", "--config=/etc/rsyncd.conf", "--log-file=/dev/stdout"]
