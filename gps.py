from datetime import datetime

def get_location():

    # Replace with actual GPS module later

    latitude = 17.3850
    longitude = 78.4867

    return {
        "latitude": latitude,
        "longitude": longitude,
        "time": datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    }