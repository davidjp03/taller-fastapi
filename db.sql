CREATE DATABASE carros;
CREATE TABLE cars (
    name VARCHAR(255),
    year INT,
    selling_price INT,
    km_driven INT,
    fuel VARCHAR(50),
    seller_type VARCHAR(50),
    transmission VARCHAR(50),
    owner VARCHAR(50),
    mileage VARCHAR(50),
    engine VARCHAR(50),
    max_power VARCHAR(50),
    torque VARCHAR(100),
    seats FLOAT
);

/*
Los datos del .csv los subi con ayuda de datagrip
*/

SELECT * FROM cars;