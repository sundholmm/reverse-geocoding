# reverse-geocoding
Flask WSGI web application for geocoding

### Meaning
> "Reverse geocoding is the process of back (reverse) coding of a point location (latitude, longitude) to a readable address or place name."
> [Wikipedia](https://en.wikipedia.org/wiki/Reverse_geocoding)

> "Nominatim (from the Latin, 'by name') is a tool to search OSM data by name and address (geocoding) and to generate synthetic addresses of OSM points (reverse geocoding)."
> [OpenStreetMap Wiki](https://wiki.openstreetmap.org/wiki/Nominatim)

### #1 Implementation
The application listens on ```/api/v1/reverse``` and takes **lat**, **lng** and **app_name** as HTTP GET arguments.
It then returns reverse geolocation for the given latitude and longitude point.
Application name is used as an identifier for OpenStreetMap API.

### Setup
[Please refer to Flask documentation](https://flask.palletsprojects.com/en/1.1.x/quickstart/)

### Example
Query:
```
$ curl "http://localhost:5000/api/v1/reverse?lat=52.509669&lng=13.376294&app_name=my_application"
```

Will return:
```
{
	"address":{
		"borough":"Mitte",
		"city":"Berlin",
		"country":"Deutschland",
		"country_code":"de",
		"postcode":"10785",
		"road":"Potsdamer Platz",
		"shop":"Steinecke",
		"suburb":"Tiergarten"
	},
	"boundingbox":[
		"52.5097484",
		"52.5098379",
		"13.3762557",
		"13.3763681"
	],
	"display_name":"Steinecke, Potsdamer Platz, Tiergarten, Mitte, Berlin, 10785, Deutschland",
	"lat":"52.5098134",
	"licence":"Data \u00a9 OpenStreetMap contributors, ODbL 1.0. https://osm.org/copyright",
	"lon":"13.37631790998454",
	"osm_id":464904418,
	"osm_type":"way",
	"place_id":189803969
}
```
