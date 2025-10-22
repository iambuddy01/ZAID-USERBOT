FROM python:3.9.7-slim-buster

# 1. Update & install dependencies
RUN apt-get update && apt-get upgrade -y && \
    apt-get install -y --no-install-recommends \
        git \
        curl \
        ffmpeg \
        build-essential \
        libffi-dev \
        libssl-dev && \
    apt-get clean && rm -rf /var/lib/apt/lists/*

# 2. Upgrade pip, setuptools, wheel
RUN python3 -m pip install --no-cache-dir --upgrade pip setuptools wheel

# 3. Copy project files
COPY . /app/
WORKDIR /app/

# 4. Install Python dependencies
RUN pip3 install --no-cache-dir -U -r requirements.txt

# 5. Environment variables for proper Heroku logging & GitPython
ENV PYTHONUNBUFFERED=1 \
    GIT_PYTHON_REFRESH=quiet

# 6. Start bot
CMD ["bash", "start.sh"]
