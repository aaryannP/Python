create database bank_DB;
use bank_DB;

-- Bankers table
create table bankers
(
id int auto_increment Primary key,
usernme varchar(50) unique not null,
password varchar(255) not null
);

select * from bankers;

-- Customers  table 
CREATE TABLE customers (
    id INT AUTO_INCREMENT PRIMARY KEY,
    name VARCHAR(50) NOT NULL,
    email VARCHAR(100) UNIQUE,
    password VARCHAR(255),
    balance DOUBLE DEFAULT 0
);

select * from customers;