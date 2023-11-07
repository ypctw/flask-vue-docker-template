FROM ubuntu:latest

USER root
RUN apt-get update &&  apt-get install -y ca-certificates curl gnupg && \
    curl -fsSL https://deb.nodesource.com/gpgkey/nodesource-repo.gpg.key | gpg --dearmor -o /etc/apt/keyrings/nodesource.gpg  && \
    echo "deb [signed-by=/etc/apt/keyrings/nodesource.gpg] https://deb.nodesource.com/node_20.x nodistro main" |  tee /etc/apt/sources.list.d/nodesource.list  && \
    apt-get update &&  apt-get install nodejs -y

RUN apt-get -y install nodejs
WORKDIR /home/app
COPY vue .

RUN npm i @vue/cli@5.0.8
RUN npm i vue-axios
RUN npm install

CMD [ "npm", "run", "serve" ]