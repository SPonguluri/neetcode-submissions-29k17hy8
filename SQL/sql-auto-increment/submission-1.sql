CREATE SEQUENCE gov_id START WITH 1000 INCREMENT BY 3;

create table gov_employee (
id Integer Primary Key generated always as Identity,
gov_id Integer Default nextval('gov_id'),
name Text
);










-- Do not modify below this line --
INSERT INTO gov_employee (name) 
  VALUES
      ('John Doe'),
      ('Jane Doe'),
      ('Jim Beam');

SELECT * FROM gov_employee;
