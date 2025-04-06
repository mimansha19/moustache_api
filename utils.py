from geopy.geocoders import Nominatim
from fuzzywuzzy import process
from math import radians, cos, sin, asin, sqrt

geolocator = Nominatim(user_agent="moustache_locator")

KNOWN_LOCATIONS = [
    "Udaipur", "Jaipur", "Jaisalmer", "Jodhpur", "Agra", "Delhi", "Rishikesh",
    "Varanasi", "Goa", "Koksar", "Daman", "Pushkar", "Khajuraho", "Manali",
    "Bhimtal", "Srinagar", "Ranthambore", "Coimbatore", "Shoja", "Panarpani", "Sissu"
]

def correct_spelling(query):
    """
        Corrects the input query based on fuzzy matching against a list of valid city names.
    
        Args:
            query (str): Misspelled or fast-typed location input.
            city_list (list): List of known valid city names.
        
        Returns:
            str: Closest matching city name based on fuzzy similarity.
    """
    match, score = process.extractOne(query, KNOWN_LOCATIONS)
    return match if score >= 80 else None  

def geocode_location(location):
    """
        Args:
            query (str): The location entered by the telecaller (may contain spelling errors).       
        Returns:
            tuple: (latitude, longitude) if the location is found, otherwise None.
    """
    try:
        loc = geolocator.geocode(location, timeout=3)
        if loc:
            return loc.latitude, loc.longitude
    except Exception:
        return None, None
    return None, None

def haversine(lat1, lon1, lat2, lon2):
    """
        Calculates the great-circle distance between two points on the Earth's surface.
    
        Args:
            lat1 (float): Latitude of the first point.
            lon1 (float): Longitude of the first point.
            lat2 (float): Latitude of the second point.
            lon2 (float): Longitude of the second point.
        
        Returns:
            float: Distance in kilometers between the two points.
    """
    R = 6371  # Earth radius in KM
    lat1, lon1, lat2, lon2 = map(radians, [lat1, lon1, lat2, lon2])
    dlat = lat2 - lat1
    dlon = lon2 - lon1
    a = sin(dlat/2)**2 + cos(lat1) * cos(lat2) * sin(dlon/2)**2
    return R * 2 * asin(sqrt(a))