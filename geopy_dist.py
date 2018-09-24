# Patrik Boloz


from geopy.distance import distance
from geopy.geocorders import Nominatim


geolocator = Nominatim()


loc_1  = raw_input('Please, enter first addresss: ')

loc = geolocator.geocode(loc_1)

if not loc:
	print ('Location not found in Nominatim, try again.')
else:
	loc_2 = raw_input('Please, enter second address: ')

	d = distance((loc.latitude, loc.longitude), (lob_2.latitude, lob_2.longitude)).miles

	print ('The total distance between ', loc_1, ' and ', loc_2, ' is:\n', d)