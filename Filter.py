# Write a query that will display the results below (Note: some columns might be renamed but use the column names above). It should only show 2020 data and order by driver points.
# Let join_race_results be the DataFrame

from pyspark.sql.functions import col

df_2020 = join_race_results.filter(col('year') == 2020).orderBy(col('points').desc())

df_2020.show()
