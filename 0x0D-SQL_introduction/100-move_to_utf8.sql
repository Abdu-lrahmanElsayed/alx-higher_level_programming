-- This script converts hbtn_0c_0 database to UTF8.
USE hbtn_0c_0;
ALTER DATABASE hbtn_0c_0 CHARACTER SET utf8mb4 COLLATE utf8mb4_general_ci;
ALTER TABLE first_table CHARACTER SET utf8mb4 COLLATE utf8mb4_general_ci;
ALTER TABLE first_table MODIFY COLUMN name VARCHAR(256) CHARACTER SET utf8mb4 COLLATE utf8mb4_general_ci;
