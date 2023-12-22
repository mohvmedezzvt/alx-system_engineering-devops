# 0x14. MySQL

## Description
This repository contains configuration steps for setting up MySQL on two servers (web-01 and web-02) as part of a larger project. The task involves installing MySQL 5.7.x, configuring SSH access, and creating a MySQL user with specific permissions.

## Installation Steps

### MySQL Installation
1. Connect to the server web-01:
    ```bash
    ssh ubuntu@web-01
    ```

2. Update package lists:
    ```bash
    sudo apt update
    ```

3. Install MySQL server 5.7 or above:
    ```bash
    sudo apt install mysql-server
    ```

4. Secure MySQL installation (optional but recommended):
    ```bash
    sudo mysql_secure_installation
    ```

5. Repeat the process on web-02.

### MySQL User Configuration
1. Connect to MySQL on both web-01 and web-02:
    ```bash
    sudo mysql
    ```

2. Create the 'holberton_user' with replication client privileges:
    ```sql
    CREATE USER 'holberton_user'@'localhost' IDENTIFIED BY 'projectcorrection280hbtn';
    GRANT REPLICATION CLIENT ON *.* TO 'holberton_user'@'localhost';
    FLUSH PRIVILEGES;
    SHOW GRANTS FOR 'holberton_user'@'localhost';
    EXIT;
    ```

3. Repeat the process on web-02.

## Verification
To verify the MySQL installation and user configuration, execute the following commands:

1. Check MySQL version:
    ```bash
    mysql --version
    ```

2. Verify the 'holberton_user' privileges:
    ```bash
    mysql -uholberton_user -p -e "SHOW GRANTS FOR 'holberton_user'@'localhost'"
    ```

## Author
Mohamed Ezzat
mohamedelhdary321@gmail.com
