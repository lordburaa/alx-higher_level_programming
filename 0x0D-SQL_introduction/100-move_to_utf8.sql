-- converts hbtn_0c_0 DATABASE to UTF8
USE hbtn_0c_0;
ALTER DATABASE hbtn_0c_0 CHARACTER SET utf8mb4 COLLATE utf8mb4_unicode_ci;

ALTER TABLE second_table MODIFY name  VARCHAR(255) CHARACTER SET utf8mb4 COLLATE utf8mb4_unicode_ci;
SET names utf8;
