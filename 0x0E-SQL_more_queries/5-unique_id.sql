-- CREATE the table unique_id on your MYSQL server
CREATE TABLE IF NOT EXISTS unique_id(
	id INT AUTO_INCREMENT,
	name VARCHAR(256),
	UNIQUE KEY id_unique(id)
	);
