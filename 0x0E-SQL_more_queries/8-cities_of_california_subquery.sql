-- List the cities of California in database hbtn_0d_usa.
SELECT * FROM cities
WHERE state_id IN (SELECT id FROM states WHERE name = 'California')
ORDER BY id ASC;
