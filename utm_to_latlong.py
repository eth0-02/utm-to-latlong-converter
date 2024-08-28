from pyproj import Proj, transform

def utm_to_latlong(easting, northing, zone_number, zone_letter):
    """
    Converts UTM coordinates to latitude and longitude.
    
    Parameters:
    easting (float): UTM easting coordinate
    northing (float): UTM northing coordinate
    zone_number (int): UTM zone number
    zone_letter (str): UTM zone letter (N or S)

    Returns:
    tuple: (latitude, longitude)
    """
    # Define the UTM projection based on the zone number and hemisphere
    is_northern = (zone_letter.upper() >= 'N')
    utm_proj = Proj(proj='utm', zone=zone_number, ellps='WGS84', south=not is_northern)

    # Define the WGS84 (latitude/longitude) projection
    wgs84_proj = Proj(proj='latlong', datum='WGS84')

    # Convert UTM to latitude and longitude
    longitude, latitude = transform(utm_proj, wgs84_proj, easting, northing)

    return latitude, longitude

# Example usage
if __name__ == "__main__":
    easting = 339374  # UTM easting
    northing = 9959921  # UTM northing
    zone_number = 37  # UTM zone number
    zone_letter = 'S'  # UTM zone letter

    latitude, longitude = utm_to_latlong(easting, northing, zone_number, zone_letter)
    print(f"Latitude: {latitude}, Longitude: {longitude}")
