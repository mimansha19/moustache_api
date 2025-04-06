'''
  The code below can also be used if the data is stored in the txt file like property_list.py
  So one just have to put the right .txt file with this name with any number of properties available
  No need to manually type the data.
'''

def load_properties_from_file(file_path="property_list.txt"):
    properties = []
    try:
        with open(file_path, "r", encoding="utf-8") as f:
            for line in f:
                parts = line.strip().split(",")
                if len(parts) != 3:
                    continue
                name, lat, lon = parts
                properties.append({
                    "name": name,
                    "latitude": float(lat),
                    "longitude": float(lon)
                })
    except FileNotFoundError:
        print("Property list file not found.")
    return properties

properties = load_properties_from_file()

# properties = [
#   {"name": "Moustache Udaipur Luxuria", "latitude": 24.57799888, "longitude": 73.68263271},
#   {"name": "Moustache Udaipur", "latitude": 24.58145726, "longitude": 73.68223671},
#   {"name": "Moustache Udaipur Verandah", "latitude": 24.58350565, "longitude": 73.68120777},
#   {"name": "Moustache Jaipur", "latitude": 27.29124839, "longitude": 75.89630143},
#   {"name": "Moustache Jaisalmer", "latitude": 27.20578572, "longitude": 70.85906998},
#   {"name": "Moustache Jodhpur", "latitude": 26.30365556, "longitude": 73.03570908},
#   {"name": "Moustache Agra", "latitude": 27.26156953, "longitude": 78.07524716},
#   {"name": "Moustache Delhi", "latitude": 28.61257139, "longitude": 77.28423582},
#   {"name": "Moustache Rishikesh Luxuria", "latitude": 30.13769036, "longitude": 78.32465767},
#   {"name": "Moustache Rishikesh Riverside Resort", "latitude": 30.10216117, "longitude": 78.38458848},
#   {"name": "Moustache Hostel Varanasi", "latitude": 25.2992622, "longitude": 82.99691388},
#   {"name": "Moustache Goa Luxuria", "latitude": 15.6135195, "longitude": 73.75705228},
#   {"name": "Moustache Koksar Luxuria", "latitude": 32.4357785, "longitude": 77.18518717},
#   {"name": "Moustache Daman", "latitude": 20.41486263, "longitude": 72.83282455},
#   {"name": "Panarpani Retreat", "latitude": 22.52805539, "longitude": 78.43116291},
#   {"name": "Moustache Pushkar", "latitude": 26.48080513, "longitude": 74.5613783},
#   {"name": "Moustache Khajuraho", "latitude": 24.84602104, "longitude": 79.93139381},
#   {"name": "Moustache Manali", "latitude": 32.28818695, "longitude": 77.17702523},
#   {"name": "Moustache Bhimtal Luxuria", "latitude": 29.36552248, "longitude": 79.53481747},
#   {"name": "Moustache Srinagar", "latitude": 34.11547314, "longitude": 74.88701741},
#   {"name": "Moustache Ranthambore Luxuria", "latitude": 26.05471373, "longitude": 76.42953726},
#   {"name": "Moustache Coimbatore", "latitude": 11.02064612, "longitude": 76.96293531},
#   {"name": "Moustache Shoja", "latitude": 31.56341267, "longitude": 77.36733331}
# ]
