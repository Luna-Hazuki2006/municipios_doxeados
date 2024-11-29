from geopy.geocoders import Nominatim
geolocator = Nominatim(user_agent="municipios_doxeados")
location = geolocator.reverse("10.078059339461356, -69.28161803343771")
print(location.address)
# Potsdamer Platz, Mitte, Berlin, 10117, Deutschland, European Union
print((location.latitude, location.longitude))
# (52.5094982, 13.3765983)
print(location.raw)