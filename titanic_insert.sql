-- Insert count of rows
INSERT INTO titanic (

    number_of_rows

) VALUES (

    (SELECT COUNT(*) FROM titanic)

);

-- Insert count of survivors
INSERT INTO titanic (
    
    survived
    
) VALUES 

    ((SELECT COUNT(*) FROM titanic WHERE survived = 1)

);

-- Insert passenger class with largest population
INSERT INTO titanic (
    
    pclass
    
)VALUES
 
 
FROM (

    SELECT pclass, -- gets the pclass values from the subquery

    COUNT(*) AS population FROM titanic GROUP BY pclass ORDER BY population DESC LIMIT 1

) AS subquery;





