-- lists all the cities of california that can be found in the database hbtn_0d_usa

SELECT cities.id, cities.state_id, cities.name FROM cities, states WHERE states.name='California';

