CREATE DATABASE IF NOT EXISTS django_test;
GRANT ALL ON `django_test`.* TO 'django'@'%';
ALTER USER 'django'@'%' IDENTIFIED WITH mysql_native_password BY 'secret';