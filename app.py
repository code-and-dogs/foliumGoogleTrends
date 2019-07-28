import folium
import os
import pandas as pd

germanStates = os.path.join('data', 'germanStates.json')
donaldTrumpSearchRes = os.path.join('data', 'geoMap.csv')
searchRes = pd.read_csv(donaldTrumpSearchRes)

map = folium.Map(location=[51.629,10.867], zoom_start=5.4, tiles='openstreetmap')
folium.Choropleth(
    geo_data = germanStates,
    name = 'Donald Trump Search Results',
    data = searchRes,
    columns = ['Region' , 'donald trump'],
    key_on = 'feature.properties.NAME_1',
    fill_color = 'PuBu',
    fill_opacity = 1,
    line_opacity = 1,
    nan_fill_color = '#f2efe9',
    line_color = 'white'
).add_to(map)
map.save('index.html')
