from geopy.geocoders import Nominatim

geolocator = Nominatim(user_agent="job_scraper")

# Example job location
location = "Glasgow, Scotland"
coords = geolocator.geocode(location)

if coords:
    print(f"Coordinates of {location}: {coords.latitude}, {coords.longitude}")
else:
    print("Location not found!")
# The code above uses the geopy library to get the coordinates of a location. This can be useful when you want to visualize job locations on a map or calculate distances between them.

from geopy.distance import geodesic

# Your location (set this to whatever city you want)
your_location = (55.9533, -3.1883)  # Edinburgh

# Example job location
job_location = (51.5074, -0.1278)  # London

# Calculate distance
distance = geodesic(your_location, job_location).km
print(f"Distance: {distance:.2f} km")

from geopy.geocoders import Nominatim
from geopy.distance import geodesic

# Set up geolocator
geolocator = Nominatim(user_agent="job_scraper")

# Your location (define your starting point)
your_location = geolocator.geocode("Edinburgh, Scotland")
your_coords = (your_location.latitude, your_location.longitude)

# Set max search radius (in km)
search_radius = 50  # Change this as needed

# Example job locations
job_locations = ["Glasgow, Scotland", "London, England", "Newcastle, England"]

for job in job_locations:
    job_place = geolocator.geocode(job)
    if job_place:
        job_coords = (job_place.latitude, job_place.longitude)
        distance = geodesic(your_coords, job_coords).km

        print(f"📍 {job} is {distance:.2f} km away")  # Debugging line

        if distance <= search_radius:
            print(f"✅ {job} is within {distance:.2f} km")
        else:
            print(f"❌ {job} is too far ({distance:.2f} km away)")
    else:
        print(f"⚠ Could not find location: {job}")

# The code above calculates the distance between your location and multiple job locations. You can set a maximum search radius to filter out jobs that are too far away.
