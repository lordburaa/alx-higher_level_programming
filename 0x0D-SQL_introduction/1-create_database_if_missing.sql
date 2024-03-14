-- creates database `hbtn_0c_0`
IF NOT EXISTS (SELECT 1 FROM sys.databases WHERE name=`hbtn_0c_0`)
BEGIN
	CREATE DATABASE `hbtn_0c_0`;
END
ELSE
BEGIN

END;
