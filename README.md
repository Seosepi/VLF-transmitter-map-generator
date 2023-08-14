# VLF-transmitter-map-generator
Python script that generates html for interactive map marking positions of VLF transmitters in use.

Config:
1. Edit vlf_transmitters.csv to include the list of your chosen vlf transmitters, including the latitude, longitude, call sign, frequency and location of each vlf transmitter
2. Edit config.py and change the variable csv_location to include the directory location of the vlf_transmitters.csv
3. When vlf_map.py is run it will display a html page of the interactive map, it will also save this as vlf_map.html to the folder local to vlf_map.py.
4. This html file can be embedded into a webpage using the <iframe> attribute
