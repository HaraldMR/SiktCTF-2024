# Use an official Ubuntu as a parent image
FROM ubuntu:latest

# Set environment variables
ENV DEBIAN_FRONTEND=noninteractive

# Install necessary packages, including bash
RUN apt-get update && apt-get install -y \
    python3 \
    python3-pip \
    python3-venv \
    openssh-server \
    git \
    bash \
    cron \
    && rm -rf /var/lib/apt/lists/*

# Set the default shell to bash
SHELL ["/bin/bash", "-c"]

# Add the cron job
RUN echo "*/30 * * * * root find /app/uploads/ -type f ! -name 'readme.txt' -delete > /dev/null 2>&1" >> /etc/cronjob
RUN crontab /etc/cronjob

# Create necessary directories
RUN mkdir /var/run/sshd
RUN mkdir /app
WORKDIR /app

# Create a virtual environment for the Flask application
RUN python3 -m venv venv

# Activate the virtual environment and install Flask
RUN source venv/bin/activate && pip install Flask

# Copy the Flask app code into the container
COPY app /app

# Set up the SSH server
RUN echo 'root:reallydifficultrootpasswordyouwouldneverguessinonego1234132' | chpasswd
RUN sed -i 's/#PermitRootLogin prohibit-password/PermitRootLogin yes/' /etc/ssh/sshd_config
RUN sed -i 's/PasswordAuthentication no/PasswordAuthentication yes/' /etc/ssh/sshd_config

# Create dustin and admin users and set passwords
RUN useradd -m -s /bin/bash dustin && echo 'dustin:dustin55534llol' | chpasswd
RUN useradd -m -s /bin/bash admin && echo 'admin:admin1992¤21#!PEccD11Erheh' | chpasswd

RUN touch /home/dustin/.hushlogin && touch /home/admin/.hushlogin

# Set up .git repository in dustin's home
RUN mkdir /home/dustin/repo
WORKDIR /home/dustin/repo

# Configure Git with generic info
RUN git config --global user.email "dustin@repo.xyz"
RUN git config --global user.name "dustin elop"

# Initialize git and make commits
RUN git init
RUN echo "Welcome to the repository!" > readme.txt
RUN git add readme.txt
RUN git commit -m "Initial commit"
RUN echo "Remember to delete this file before starting the server! Dont leak the server password!" >> readme.txt
RUN echo "Username: admin\tPassword: admin1992¤21#!PEccD11Erheh" >> readme.txt
RUN git add readme.txt
RUN git commit -m "Update readme with admin credentials"
RUN echo "Welcome to the repository!" > readme.txt
RUN echo "Remember to delete this file before starting the server! Dont leak the server password!" >> readme.txt
RUN echo "Username: dustin\tPassword: dustin55534llol" >> readme.txt
RUN git add readme.txt
RUN git commit -m "Update readme with dustin credentials"

# Set permissions for .git directory
RUN chown -R dustin:dustin /home/dustin/repo/.git
RUN chown -R dustin:dustin /home/dustin/repo/

# Add git reset functionality to dustin's .bashrc
RUN echo 'cd /home/dustin/repo && git checkout master >/dev/null 2>&1 && git reset --hard HEAD >/dev/null 2>&1 && cd /home/dustin/' >> /home/dustin/.bashrc
# RUN echo 'find /app/uploads/ -type f -not -name "readme.txt" -delete >/dev/null 2>&1' >> /home/dustin/.bashrc

# Place the flag in admin's home
RUN echo "SiktCTF{Do_You_Know_How_To_Pwn?}" > /home/admin/flag.txt
RUN chown admin:admin /home/admin/flag.txt

# Expose the necessary ports
EXPOSE 80 22

# Run Flask app and SSH server
CMD service ssh start && /bin/bash -c "source /app/venv/bin/activate && python /app/app.py"