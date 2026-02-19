'''
the eq_data.json file is a json file that contains detailed information about
earthquakes around the world for a period of a month. Use this file for this
assignment

NOTE: No hard-coding allowed except for keys for the dictionaries

1) Print out the number of earthquakes

2) Iterate through the eq_dictionary and extract the location, magnitude, 
   longitude and latitude of all earthquakes that have a magnitude > 6.0.
   Put it in a new dictionary. Using the new dictionary, 
   print out the information as shown below (first three shown as example):

Location: Northern Mid-Atlantic Ridge
Magnitude: 6.2
Longitude: -36.0923
Latitude: 35.4364


Location: 166km SSE of Muara Siberut, Indonesia
Magnitude: 6.1
Longitude: 100.0208
Latitude: -2.8604


Location: 14km ENE of Puerto Madero, Mexico
Magnitude: 6.6
Longitude: -92.2981
Latitude: 14.7628

'''



import json
infile = open('eq_data.json','r')#open the file and READ it in as a json file, then store it in a variable called eq_dictionary

eq_dictionary = json.load(infile)#load the json file into a dictionary called eq_dictionary

print('Number of earthquakes:', len(eq_dictionary['features']))#print out the number of earthquakes by using the length of the list that is stored in the 'features' key of the eq_dictionary

for earthquake in eq_dictionary['features']:#iterate through the list of earthquakes that is stored in the 'features' key of the eq_dictionary

    magnitude = earthquake['properties']['mag']#get the magnitude of the earthquake by accessing the 'mag' key that is stored in the 'properties' key of the earthquake dictionary

    if magnitude > 6.0:
        location = earthquake['properties']['place']#get the location of the earthquake by accessing the 'place' key that is stored in the 'properties' key of the earthquake dictionary
        longitude = earthquake['geometry']['coordinates'][0]#get the longitude of the earthquake by accessing the 'coordinates' key that is stored in the 'geometry' key of the earthquake dictionary, then get the first element of the list that is stored in the 'coordinates' key
        latitude = earthquake['geometry']['coordinates'][1]#get the latitude of the earthquake by accessing the 'coordinates' key that is stored in the 'geometry' key of the earthquake dictionary, then get the second element of the list that is stored in the 'coordinates' key

        print(f"\nLocation: {location}")
        print(f"Magnitude: {magnitude}")
        print(f"Longitude: {longitude}")
        print(f"Latitude: {latitude}")

