
FROM ubuntu:latest

ARG UID=1000
ARG GID=1000
ARG USERNAME="user"
ARG TZ="Asia/Taipei"

ENV INSTALLATION_TOOLS apt-utils \
    curl \
    software-properties-common \
    wget \
    dos2unix

ENV DEVELOPMENT_PACKAGES python3 \
    python3-pip \
    python-is-python3

# setup time zone
RUN ln -snf /usr/share/zoneinfo/${TZ} /etc/localtime && echo ${TZ} > /etc/timezone

# install system packages
RUN apt-get -qq update && \
    apt-get -qq install ${INSTALLATION_TOOLS} && \
    # prerequisite - git
    add-apt-repository ppa:git-core/ppa && \
    # start install
    apt-get -qq update && \
    apt-get -qq upgrade && \
    apt-get -qq install ${DEVELOPMENT_PACKAGES}

# install python libraries
COPY ./config/requirements.txt /tmp/requirements.txt
RUN pip3 install -r /tmp/requirements.txt && \
    rm /tmp/requirements.txt

# add scripts and setup permissions
WORKDIR /usr
# add scripts and setup permissions
COPY --chown=${UID}:${GID} ./scripts/start.sh .
RUN dos2unix -ic "/usr/start.sh" | xargs dos2unix && \
    chmod +x "/usr/start.sh"


