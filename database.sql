CREATE DATABASE networking_shop;
USE networking_shop;

CREATE TABLE products (
    id INT AUTO_INCREMENT PRIMARY KEY,
    name VARCHAR(100),
    category VARCHAR(50),
    price DECIMAL(10,2),
    description TEXT
);

INSERT INTO products (name, category, price, description) VALUES
('Cisco 2960 Switch', 'Switch', 45000, '24 Port Managed Switch'),
('TP-Link Router', 'Router', 18000, 'High speed wireless router');
