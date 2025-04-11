FROM python:3.11-slim
LABEL maintainer=mcwilk

# Set environment variables
ENV DEBIAN_FRONTEND=noninteractive
ENV PYTHONUNBUFFERED=1
ENV PYTHONDONTWRITEBYTECODE=1

# Set the working directory
WORKDIR /budget_tracker

# Set environment
COPY requirements.txt .
RUN apt update && apt install -y bash && pip install --no-cache-dir -r requirements.txt

COPY . .
COPY /docker-entrypoint.sh .
RUN chmod +x docker-entrypoint.sh
#
ENTRYPOINT ["/docker-entrypoint.sh"]
#ENTRYPOINT ["bash", "-c", "whoami && pwd && pip freeze"]

#CMD ["sh"]
