FROM python:3.11-slim
LABEL maintainer=mcwilk

# Set environment variables
#ENV USER_NAME=$USER_NAME
#ENV USER_PASSWD=$USER_PASSWD
ENV USER_NAME=django_user
ENV USER_PASSWD=django_user_passwd123

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
    apt-get install -y bash nano passwd &&  \
    groupadd "$USER_NAME" &&  \
    useradd -g "$USER_NAME" -p "$USER_PASSWD" "$USER_NAME" && \
    pip install --no-cache-dir -r requirements.txt

#RUN useradd -m -s /bin/bash "$USER_NAME" && echo "$USER_NAME:$USER_PASSWD" | chpasswd && \
#    adduser "$USER_NAME" sudo && chown -R $USER_NAME:$USER_NAME /app

COPY . .
#COPY docker-entrypoint.sh .
RUN chown "$USER_NAME:$USER_NAME" docker-entrypoint.sh && chmod +x docker-entrypoint.sh

USER $USER_NAME

ENTRYPOINT ["/budget_tracker/docker-entrypoint.sh"]
#ENTRYPOINT ["bash", "-c", "whoami && pwd && pip freeze"]

#CMD ["bash"]
