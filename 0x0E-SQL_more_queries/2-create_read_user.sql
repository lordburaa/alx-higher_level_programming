-- create the databse hbtn_0c_2 and
-- create user user_od_2 if not exists
-- give permission fo the useruser_0d_2 SELECT 

CREATE DATABASE IF NOT EXISTS hbtn_0d_2;

CREATE USER IF NOT EXISTS 'user_0d_2'@'localhost' IDENTIFIED BY 'user_0d_pwd';
GRANT SELECT ON `hbtn_0d_2`.* TO 'user_0d_2'@'localhost' WITH GRANT OPTION;
