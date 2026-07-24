Create table products(
name Text Not Null Default 'Unknown',
price integer Not Null,
quantity Integer default 0
);






-- Do not modify below this line --
SELECT column_name, data_type, is_nullable, column_default
FROM information_schema.columns
WHERE table_name = 'products';
