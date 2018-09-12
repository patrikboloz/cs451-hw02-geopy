Write a command line utility in Python that computes the geodisic distance between two addresses that are input on the terminal. Sample interaction:

```python
>>Enter starting location: 1314 chavez st., las vegas, nm
>>Enter starting location: 1701 bryant st, denver, co
Distance between 1314, Chavez Street, Las Vegas, San Miguel County, New Mexico, 87701, USA and
Mile High, 1701, Bryant Street, Jefferson Park, Denver, Denver County, Colorado, 80204, USA is
286.802274959 miles
```
You can choose which python packages you want to use to do geographic computations but I suggest the following:

a. Use the geopy package (https://pypi.org/project/geopy/)

b. geopy has a connector to Nominatum for accessing geodata (http://nominatim.org/)

c. Research the geopy documentation (https://geopy.readthedocs.io/en/stable/) to learn how you might compute distance from to geo location objects.

## What to turn in?

1. You will need to fork this repository (containing this readme.md file) to your GitHub account then clone your forked copy to your development machine.

2. Next, you will add:

a. A requirements.txt file with the necessary dependencies for the application

b. Your python script (source code) file containing your application

3. Submission for this assignment is met when you add, commit, and push your changes to your remote repository.


## Sample basic usage of geopy to locate an address using OpenStreetMap data from Nominatum:

```python
from geopy.geocoders import Nominatim

# Create a geolocator object to access geo data using Nominatum
geolocator = Nominatim()

# A query address
query = '1314 chavez st, las vegas, nm'

# Build/retrieve a geopy Location object with a query address
location = geolocator.geocode(query)

# Access the latitude from location object
print(location.latitude)

# Access the longitude from location object
print(location.longitude)

# View the Location object API
help(location)
```
