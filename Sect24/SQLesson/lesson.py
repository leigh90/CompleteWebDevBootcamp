# CREATING A DATABASE
# CREATE
# CREATE A TABLE
CREATE TABLE nameoftable(
    field DATATYPE,
)
CREATE TABLE products(
    id INT NOT NULL,  #NOT NULL is added esp if the field is a primary key and cannot be null
    name STRING,
    price MONEY,
    PRIMARY KEY(id)  #set primary key as 'id' field
)

# ADD VALUES TO THE TABLE

INSERT INTO nameoftable
VALUES(field,field,field)

INSERT INTO products
VALUES(1, 'pen', 1.30)

INSERT INTO products
VALUES(2, 'pencil', 2.50)

# YOU CAN ADD VALUES EVEN IF YOU DONT HAVE ALL THE FIELDS THEY WILL BE SET TO NULL 
INSERT INTO products
VALUES(3, 'girraffe')

# this only works for all fields except those set as the primary key. since it is set to not null you cannot create a product without  a primary key

# to SELECT EVERYTHING 
SELECT * FROM nameoftable;
SELECT * FROM products;

# to see only selected columns
SELECT nameofcolumn, FROM nameoftable;
SELECT name FROM products;
# to see multiple columns
SELECT name, price FROM products;

# READ THE DATABASE
SELECT * FROM nameoftable WHERE condition;
SELECT * FROM products WHERE id=1;

# to return te speciic column
SELECT nameofcolumn FROM nameoftable WHERE condition;
SELECT id FROM products WHERE id=1; 

# you can read multiple COLUMNS
SELECT nameofcolumn, nameofcolumn, nameofcolumn FROM nameoftable WHERE condition
SELECT id, name, price FROM products



# UPDATE

# UPDATING THE TABLE
# Adding a new column
ALTER TABLE nameoftable ADD nameofnewcolumn DATATYPE
ALTER TABLE products ADD stock INT

# UPDATING COLUMN VALUES
UPDATE nameoftable SET nameofcolumn=value WHERE condition;
UPDATE products SET stock=32 WHERE id=1
UPDATE products SET stock=12 WHERE id=2

# DELETE
DELETE FROM nameoftable WHERE condition;


# CREATE RELATIONSHIPS  FOREIGN KEY

CREATE TABLE(
    id INT NOT NULL,
    order_number INT,
    customer_id INT,
    product_id INT,
    PRIMARY KEY (id)
    FOREIGN KEY nameofthistablescolumn REFERENCES nameoftable(fieldnametolinkto)
    FOREIGN KEY nameofthistablescolumn REFERENCES nameoftable(fieldnametolinkto)

)
CREATE TABLE(
    FOREIGN KEY (customer_id) REFERENCES customer(id)
    FOREIGN KEY (product_id) REFERENCES product(id)
)