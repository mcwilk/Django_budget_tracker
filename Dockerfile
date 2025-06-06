FROM python:3.11-slim
LABEL maintainer=mcwilk

# Receive build.args
ARG USER_NAME
ARG USER_PASSWD

# Set environment variables
ENV USER_NAME=${USER_NAME}
ENV USER_PASSWD=${USER_PASSWD}

ENV DEBIAN_FRONTEND=noninteractive
# Use console for logs
ENV PYTHONUNBUFFERED=1
# Do not create .pyc files
ENV PYTHONDONTWRITEBYTECODE=1

# Set the working directory
WORKDIR /budget_tracker

# Set environment
COPY requirements.txt .
RUN apt-get update &&  \
    apt-get install -y bash nano netcat-openbsd passwd curl &&  \
    groupadd "$USER_NAME" &&  \
    useradd -g "$USER_NAME" -p "$USER_PASSWD" "$USER_NAME" && \
    pip install --no-cache-dir -r requirements.txt

COPY . .
RUN chown "$USER_NAME:$USER_NAME" docker-entrypoint.sh && chmod +x docker-entrypoint.sh

USER $USER_NAME

ENTRYPOINT ["/budget_tracker/docker-entrypoint.sh"]