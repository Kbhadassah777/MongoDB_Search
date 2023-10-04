# MongoDB_Search

A Project to demonstrate some textual and spatial searching on MongoDB.
To do so testData.json file is used as document to put inside MongoDb.

Requirements:
You will need MongoDB 
I used pymongo as helper interface with MongoDB


Implementing two functions one for each searching
a.	Textual Search – FindBusinessBasedOnCity(cityToSearch, saveLocation1, collection) 
This function searches the ‘collection’ given to find all the business present in the city provided in ‘cityToSearch’ and save it to ‘saveLocation1’. For each business you found, you should store name Full address, city, state of business in the following format. 
Each line of the saved file will contain, Name$FullAddress$City$State. ($ is the separator and must be present) 

b.	Spatial Search – FindBusinessBasedOnLocation (categoriesToSearch, myLocation, maxDistance, saveLocation2, collection)

This function searches the ‘collection’ given to find name of all the business present in the ‘maxDistance’ from the given ‘myLocation’ that covers all the given categories (the business category needs to match at least one of the given categories) (please use the distance algorithm given below) and save them to ‘ saveLocation2’. Each line of the output file will contain the name of the business only. 
-- categoriesToSearch: a list of categories need to be covered -- ‘myLocation’ will be given with format [“40.3”, “51.6”]. -- maxDistance: the search distance
-- saveLocation2: output location 


1.	Taken reference from http://www.movable-type.co.uk/scripts/latlong.html to find distance between two co-ordinates – using the formula stated here, defined a function called DistanceFunction.
2.	To implement the functions used db.collection.find – to find the required values in the collection

