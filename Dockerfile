FROM python:3.11-slim
LABEL maintainer=mcwilk

# Receive build.args from docker-compose
ARG USER_NAME
ARG USER_GROUP
ARG USER_GROUP_ID

# Set environment variables
ENV USER_NAME=${USER_NAME}
ENV USER_GROUP=${USER_GROUP}
ENV USER_GROUP_ID=${USER_GROUP_ID}

ENV DEBIAN_FRONTEND=noninteractive
# Use console for logs
ENV PYTHONUNBUFFERED=1
# Do not create .pyc files
ENV PYTHONDONTWRITEBYTECODE=1

# Set the working directory
WORKDIR /budget_tracker

# Set environment with general non-root user
COPY requirements.txt .
RUN apt-get update &&  \
    apt-get install -y bash nano netcat-openbsd passwd curl &&  \
    groupadd -g "$USER_GROUP_ID" "$USER_GROUP" &&  \
    useradd -m -u "$USER_GROUP_ID" -g "$USER_GROUP" "$USER_NAME" && \
    pip install --no-cache-dir -r requirements.txt

COPY . .
RUN chown "$USER_NAME:$USER_GROUP" docker-entrypoint.sh && chmod +x docker-entrypoint.sh

USER $USER_NAME

ENTRYPOINT ["/budget_tracker/docker-entrypoint.sh"]