import folium

map = folium.Map([13.07080474395801, 80.15057063590864], zoom_control=7, tiles= "Stamen Terrain")

fg = folium.FeatureGroup(name="My Map")

# fg.add_child(folium.Marker(location=[13.07080474395801, 80.15057063590864], popup="Hi I am a Green Marker", icon=folium.Icon(color="green")))

for coodrinates in [[13.07080474395801, 80.15057063590864], [15.07080474395801, 81.15057063590864]]:
    fg.add_child(folium.Marker(location=coodrinates, popup="Hi I am a Red Marker", icon=folium.Icon(color="green")))

map.add_child(fg)

map.save("Map1.html")