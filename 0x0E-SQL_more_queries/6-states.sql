-- create a database with states as a table

CREATE DATABASE IF NOT EXISTS hbtn_0d_usa;

USE hbnt_0d_usa;

CREATE TABLE IF NOT EXISTS states(
id INT NOT NULL AUTO_INCREMENT PRIMARY KEY UNIQUE,
name VARCHAR(256) NOT NULL
);
