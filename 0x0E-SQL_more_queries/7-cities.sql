-- database and table with foreign key

CREATE DATABASE IF NOT EXISTS hbtn_0d_usa;

-- switch to the created data base
USE hbtn_0d_usa;

-- create table
CREATE TABLE IF NOT EXISTS cities(
id INT UNIQUE NOT NULL PRIMARY KEY AUTO_INCREMENT,
state_id INT NOT NULL,
name VARCHAR(256) NOT NULL,
PRIMARY KEY (id),
FOREIGN KEY (state_id) REFERENCES states(id)
);
