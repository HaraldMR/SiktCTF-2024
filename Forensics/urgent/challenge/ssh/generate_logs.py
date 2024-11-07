import random
import datetime
import os
import time

# Parameters
log_file = "auth.log"


# Generate logs
with open(log_file, 'w') as f:

    # Add some successful logins
    for _ in range(1):
        timestamp = datetime.datetime.now().strftime("%b %d %H:%M:%S")
        f.write(f"{timestamp} sshd[12345]: Accepted password for ctfuser from 192.168.1.10 port 2200 ssh2\n")

    time.sleep(14)

    for _ in range(1):
        timestamp = datetime.datetime.now().strftime("%b %d %H:%M:%S")
        f.write(f"{timestamp} sshd[12345]: Accepted password for ctfuser from 192.168.1.10 port 2200 ssh2\n")

    time.sleep(24)

    for _ in range(20):
        timestamp = datetime.datetime.now().strftime("%b %d %H:%M:%S")
        f.write(f"{timestamp} sshd[12345]: Failed password for invalid user admin from port 2121 ssh2\n")

    time.sleep(100)

    for _ in range(1):
        timestamp = datetime.datetime.now().strftime("%b %d %H:%M:%S")
        f.write(f"{timestamp} sshd[12345]: Accepted password for ctfuser from 192.168.1.10 port 2200 ssh2\n")

    time.sleep(3)

    for _ in range(1):
        timestamp = datetime.datetime.now().strftime("%b %d %H:%M:%S")
        f.write(f"{timestamp} sshd[12345]: Accepted password for ctfuser from 192.168.1.10 port 2200 ssh2\n")

    time.sleep(10)

    for _ in range(1):
        timestamp = datetime.datetime.now().strftime("%b %d %H:%M:%S")
        f.write(f"{timestamp} sshd[12345]: Accepted password for ctfuser from 192.168.1.10 port 2200 ssh2\n")

    time.sleep(26)

    for _ in range(1):
        timestamp = datetime.datetime.now().strftime("%b %d %H:%M:%S")
        f.write(f"{timestamp} sshd[12345]: Accepted password for ctfuser from 192.168.1.10 port 2200 ssh2\n")
