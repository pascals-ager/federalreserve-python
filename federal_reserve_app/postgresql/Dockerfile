FROM postgres:9.4
MAINTAINER Advith Nagappa <advith.nagappa@gmail.com>
ENV POSTGRES_DB fundingcircle
ENV POSTGRES_USER scott
ENV POSTGRES_PASSWORD tiger
COPY init_schema.sql /docker-entrypoint-initdb.d/