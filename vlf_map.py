import pandas as pd
import folium
import webbrowser
from config import csv_location

data = pd.read_csv(csv_location,
                   skipinitialspace=True,
                   delimiter=',',
                names=['LAT','LONG','Call sign','Frequency','Location'])

latitude = data['LAT']
longitude = data['LONG']
call_sign = data['Call sign']
frequency = data['Frequency']
location = data['Location']

#Map starts on Dublin Co-ordinates
vlf_map = folium.Map(location=[53.349805, -6.26031], zoom_start=2, )


# Add markers for each location with information
for lat, lon, station, freq, loc  in zip(latitude, longitude, call_sign, frequency, location):
    popup_text = f'<b>Location:</b> {loc}<br><b>Call Sign:</b> {station}<br><b>Frequency:</b> {freq}'
    folium.Marker([lat, lon], popup=folium.Popup(popup_text, max_width=250)).add_to(vlf_map)
    #folium.PolyLine([(lat,lon),(53.349805, -6.26031)]).add_to(vlf_map)

# Display the map
vlf_map.save('vlf_map.html')
webbrowser.open("vlf_map.html")
