-- create the database hbtn_0d_usa
-- create table states 
CREATE DATABASE IF NOT EXISTS hbtn_0d_usa;
CREATE TABLE IF NOT EXISTS hbtn_0d_usa.states(
	id INT AUTO_INCREMENT,
	name VARCHAR(256) NOT NULL,
	UNIQUE KEY id_unique(id)
);	
