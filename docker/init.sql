CREATE DATABASE postgres;
CREATE USER postgres WITH PASSWORD postgres;

GRANT ALL PRIVILEGES ON DATABASE postgres TO postgres;