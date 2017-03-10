from urllib.request import urlopen
import json

def get_location():

	location = input("Enter the location you want to find")
	API_url = "https://maps.googleapis.com/maps/api/geocode/json?address=location&sensor=false"
	send_request = urlopen(API_url)
	get_data = send_request.read().decode("utf")
	json_obj = json.loads(get_data)

	return json_obj

get_location()


