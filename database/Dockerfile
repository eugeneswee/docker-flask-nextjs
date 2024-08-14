FROM mysql:8.0

ENV MYSQL_ROOT_PASSWORD=password
ENV MYSQL_DATABASE=mydatabase

EXPOSE 3306

COPY init.sql /docker-entrypoint-initdb.d/
