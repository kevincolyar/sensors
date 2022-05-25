FROM python:3.10
MAINTAINER Kevin Colyar <kevin@colyar.net>

ENV LANG C.UTF-8
ENV APP_USER deploy
ENV APP_HOME /home/$APP_USER/app

SHELL ["/bin/bash", "-o", "pipefail", "-c"]

# Set timezone
ENV TZ=America/Los_Angeles
RUN ln -snf /usr/share/zoneinfo/$TZ /etc/localtime && echo $TZ > /etc/timezone

# Create app user and app home
RUN useradd --create-home ${APP_USER}
RUN mkdir -p ${APP_HOME}
RUN chown -R ${APP_USER}:${APP_USER} ${APP_HOME}

# Change working directory
WORKDIR ${APP_HOME}

# Install libraries
COPY requirements.txt .
RUN pip install -r requirements.txt

COPY dev_requirements.txt .
RUN pip install -r dev_requirements.txt

# Change user
USER ${APP_USER}

# Copy source
COPY --chown=$APP_USER:$APP_USER . ./

# Run Server
CMD uvicorn main:app --reload --host 0.0.0.0
