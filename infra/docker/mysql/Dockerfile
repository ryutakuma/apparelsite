FROM mysql/mysql-server:8.0

ENV TZ=UTC \
  MYSQL_USER=django \
  MYSQL_PASSWORD=secret \
  MYSQL_ROOT_PASSWORD=secret

COPY init/* /docker-entrypoint-initdb.d/
COPY ./my.cnf /etc/my.cnf

