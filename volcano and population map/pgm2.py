import folium
import pandas
def color(elev):
    if elev<2000:
        return "green"
    elif elev>=2000 and elev<3000:
        return "orange"
    else:
        return "red"
data = pandas.read_csv("Volcanoes.txt")
longitude=list(data["LON"])
latitude=list(data["LAT"])
elev=list(data["ELEV"])

map = folium.Map(location=[38.58,-99.09],zoom_start=5,tiles="Stamen Terrain")  
fgv=folium.FeatureGroup(name="Volcanos")

for i,j,k in zip(longitude,latitude,elev):
    txt = folium.Popup("k",parse_html=True)
    fgv.add_child(folium.CircleMarker(location=[j,i],radius=6,popup=str(k)+' m',fill_color=color(k),color='grey',fill_opacity=0.7))
 
fgp=folium.FeatureGroup(name="Population")
fgp.add_child(folium.GeoJson(data=open('world.json', 'r', encoding='utf-8-sig').read(),
style_function=lambda x:{'fillColor':'yellow' if x['properties']['POP2005']<10000000 
else 'orange' if 10000000<=x['properties']['POP2005']< 20000000 else 'red'}))

map.add_child(fgv)
map.add_child(folium.LayerControl())
map.save("map1.html")