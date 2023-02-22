import pandas as pd
import csv
import plotly.express as px
df = pd.read_csv('total_stars.csv')
# df.head()
print(df)
rows = []
for row in df:
 rows.append(row)
# header = rows[0]
# print(header)
print(rows)

star_mass = []
star_radius = []
star_name = []
for star_data in rows:
  star_mass.append(star_data[3])
  star_radius.append(star_data[4])
  star_name.append(star_data[1])
star_gravity = []
for index,name in enumerate(star_name):
  gravity = (float(star_mass[index])*1.989e+30) / (float(star_radius[index])*6317000*6317000) * 6.957e+8
  star_gravity.append(gravity)
fig = px.scatter(x = star_radius,y = star_mass,size = star_gravity,hover_data = [star_name])
fig.show()