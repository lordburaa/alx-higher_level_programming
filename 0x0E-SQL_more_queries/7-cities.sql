-- create database hbtn_od_usa
-- create tabel cities in the database hbtn_od_usa
CREATE DATABASE IF NOT EXISTS hbtn_0d_usa;

CREATE TABLE IF NOT EXISTS hbtn_0d_usa.cities(
	id INT AUTO_INCREMENT,
	state_id INT NOT NULL,
	name VARCHAR(256) NOT NULL,
	UNIQUE KEY id_unique(id),
	FOREIGN KEY (state_id) REFERENCES state(id)
	);
