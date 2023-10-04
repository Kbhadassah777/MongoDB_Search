#
# DDS Mini Project Interface
# Name: Blessy Hadassa Konedana
#


from pymongo import MongoClient
import math
import os
import sys
import json

def DistanceFunction(lat2, long2, lat1, long1): #defining a function to calculate distance using latitude and longitude
   R=3959
   x2 = math.radians(lat2)
   x1 = math.radians(lat1)
   diff_x = math.radians(lat2-lat1)
   diff_y = math.radians(long2-long1)
   a = math.sin(diff_x/2) * math.sin(diff_x/2) + math.cos(x2) * math.cos(x1) * math.sin(diff_y/2) * math.sin(diff_y/2)
   c = 2 * math.atan2(math.sqrt(a), math.sqrt(1-a))
   d = R * c
   return d

def FindBusinessBasedOnCity(cityToSearch, saveLocation1, collection): 
    BusinessOnCity =open(saveLocation1, 'w')				# opening saved location1
    result = []	
    for i in collection.find({'city':cityToSearch.capitalize()}):
    	# city search
	    value = i['name']+"$"+i['full_address'].replace('\n',',')+"$"+i['city']+"$"+i['state']  # Storing it in given format
	    result.append(value)				# Storing it in results
    for i in result:
	    BusinessOnCity.write(i.upper()+"\n")	# writing the output file
    BusinessOnCity.close()

def FindBusinessBasedOnLocation(categoriesToSearch, myLocation, maxDistance, saveLocation2, collection):
    BusinessOnLocation = open(saveLocation2, "w")  # opening saved location2
    lat1 = float(myLocation[0])
    long1 = float(myLocation[1])

    for business in collection.find(): 
        categories = business['categories'] # storing all the categories of businesss
        if not set(categories).isdisjoint(categoriesToSearch):   
            lat2 = float(business['latitude'])
            long2 = float(business['longitude'])
            dist = DistanceFunction(lat1, long1, lat2, long2) # finding the distance using predefined function
            if dist <= maxDistance:
                BusinessOnLocation.write("{}\n".format(business['name'].upper())) # writing the output file 
    BusinessOnLocation.close()

