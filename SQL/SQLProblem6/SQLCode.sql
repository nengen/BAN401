SELECT name, release_year,artist_name FROM songs 

SELECT * FROM songs WHERE artist_name == "Astrid S"

SELECT name, artist_name, sale_price * quantity_sold as revenue FROM songs

SELECT * FROM songs WHERE release_year > 2014

SELECT * FROM songs WHERE sale_price * quantity_sold  > 100000

SELECT artist_name, sum(quantity_sold) FROM songs GROUP BY artist_name ORDER BY sum(quantity_sold) DESC

SELECT artist_name, sum(sale_price*quantity_sold) AS Total_revenue FROM songs GROUP BY artist_name ORDER BY Total_revenue DESC;SELECT artist_name, sum(sale_price*quantity_sold) AS Total_revenue FROM songs GROUP BY artist_name ORDER BY Total_revenue DESC;
