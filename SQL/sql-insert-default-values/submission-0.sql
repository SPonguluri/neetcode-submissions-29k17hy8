CREATE TABLE products (
  id INTEGER PRIMARY KEY,
  name TEXT,
  stock INTEGER DEFAULT 0
);

-- Do not modify above this line --


Insert into products (id,name)
    Values (1,'Apple'), (2,'Banana'),(3,'Orange');





-- Do not modify below this line --
SELECT * FROM products;
