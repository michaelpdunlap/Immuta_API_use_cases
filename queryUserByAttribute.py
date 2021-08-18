#################################
#                               #
#    User Query by Attribute    #
#                               #
# By: Mike Dunlap, Immuta CSA   #
# Born On: 8/18/2021            # 
#                               #
#################################

# Purpose
# Based on the input of an attribute, return all users having that attribute
# Basic instruction
  # This script is a simple framework to interogate Immuta users for 
  # users that match the inputed searchTerm

#Install json
import json

#Import requests
import requests

#Import Pandas
import pandas

# Immuta Instance variables
# Set the hostname (and port if not 443) for the Immuta instance
IMMUTA_URL= "https://yourimmutaurl.com"
# This is your user API key from Immuta
API_KEY= "input key here"
# This is the attribute search term
searchTerm = "input term here"

# get your authentication token
response = requests.post(
  IMMUTA_URL + '/bim/apikey/authenticate',
  headers={'Content-Type': 'application/json'},
  json={
    "apikey": API_KEY
  }
)

# get the auth token out of the json response
authResponse = response.json()
authToken = authResponse["token"]

# now let's try to get all connections for a project
  
userResponse = requests.get(
  IMMUTA_URL + '/bim/user',
  headers={'Authorization': authToken }  
)
  
users = userResponse.json()

# parse through all users
userIDs = users['hits']

#create a list of userIDs having the search term
userList = []
#create a list of search strings to verify accuracy
searchStringList = []

for i in userIDs: 
  aUserID = i['userid']
  searchString = str(i['authorizations'])
  # see if the search term is in the search string
  # if it is, add the user ID to the list
  if searchTerm in searchString:
    print (aUserID + " - this one matches")
    userList.append(aUserID)
    searchStringList.append(searchString)
  else:
    print (aUserID + " - this one doesn't match")
    
userReport = pandas.DataFrame({'UserID':userList, 'AuthString':searchStringList})

print(userReport)
    
print ("Done")






