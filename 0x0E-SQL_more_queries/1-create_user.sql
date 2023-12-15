-- Create user_0d_1, if it doesn't exist.
-- Grant all privileges to user.
CREATE USER IF NOT EXISTS 'user_0d_1'@'localhost' IDENTIFIED BY 'user_0d_1_pwd';
GRANT ALL ON *.* TO user_0d_1@localhost;
