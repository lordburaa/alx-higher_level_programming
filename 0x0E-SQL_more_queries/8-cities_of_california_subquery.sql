-- lists all the cities of california that can be found in the database hbtn_0d_usa

SELECT cities.id, states.id, cities.name FROM cities, states WHERE states.id=1;
