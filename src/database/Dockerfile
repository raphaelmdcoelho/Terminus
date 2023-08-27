FROM mcr.microsoft.com/mssql/server:2017-latest-ubuntu

USER root

RUN mkdir -p /usr/src/app
WORKDIR /usr/src/app

COPY . /usr/src/app

RUN chmod +x /usr/src/app/run-initialization.sh

ENV SA_PASSWORD SqlServer2022*
ENV ACCEPT_EULA Y
ENV MSSQL_PID Express

EXPOSE 1433

# override Dockerfile CMD entry from base image (which runs SQL server) with own CMD, which runs custom script
CMD /bin/bash ./entrypoint.sh