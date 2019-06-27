### Project 1: Exploratory Data Analysis of Temperature Trends

<p align="center">
    <img width="300" height="150"
         src="https://i0.wp.com/www.warwickhughes.com/agri/ipcc0112.png?w=584">
</p>

1. Description:

This project includes the exploratory data analysis of local (city 
of Raleigh,NC,US) and global temperature trends and attempts to 
explain any marked difference in the trends by means of descriptive
 statistical analysis. The local and global temperature trend data 
 was obtained from US Weather Database using SQL queries and 
 subsequently were converted into csv files (attached in the 
 repository).
 
 The data pre-processing step involved extraction of the csv data into 
 data frames in Python, wherein the city data was stored in a data 
 frame named `raleigh_temp_data` and the global temperature data was 
 stored in a data frame named `global_temp_data`using the Python 
 Pandas library. Subsequent statistical analyses was accomplished 
 via the pandas statistical functions defined in the library.
 
2. Observation and Conclusion

Several observations can be made based on the 10-year moving average 
line chart obtained in the attached Jupyter Notebook. They are written
 as points below.

-	It can be observed that over the years from 1750 to 2013, the 
average temperature values, in general have increased for both Raleigh
 city and the globe. This shows an overall increasing trend of world 
 temperatures and the trend seems to be consistent over the last few 
 hundred years.

-	The 10-year moving average of temperatures of Raleigh city is 
consistently much higher than that of the global temperature values 
over all the years. This is expected since Raleigh, being in a southern 
state, experiences relatively high temperatures throughout the years 
where snowfall during the winters is often rare. On the other hand, 
the global average considers the effect of the temperatures of regions 
like the arctic where sub zero temperatures are persistent for long periods 
of time, driving the global average to a lower value.

-	The city temperature trend shows more fluctuations when compared 
to the global temperature values. This is expected since the global 
temperature averages over a wide range of areas, latitudes/longitudes 
and climates. Consequently, it is more difficult for the global average 
to change abruptly as opposed to the city average.

-	Both the city and the global temperature values show multiple 
profound dips in the range of the years 1750 – 1850. An investigation 
into this revealed some insight as to why that might have had happened. 
An article published by the climatologist Cliff Harris and Meteorologist 
Randy Mann describes the situation in terms of the following chart.
