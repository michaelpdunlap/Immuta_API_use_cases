#################################
#                               #
#          Data Source          #
#   Stakeholder Identification  #
#                               #
# By: Mike Dunlap, Immuta CSA   #
# Born On: 9/8/2021             # 
#                               #
#################################

# Purpose
# Query owners and subscribers of any datasource based on entry 
# of data source name
#
# Basic instruction

# 1.) enter the data source as a search parameter
# 2.) execute the script
# 3.) returns data frame with owner and subscribers

#Install json
import json

#Import requests
import requests

#Import Pandas
import pandas

# set Immuta vars
# Set the hostname for the Immuta instance
IMMUTA_URL= "https://<yourImmuta>.com"
# This is your user API key from Immuta 
API_KEY= "<your key here>"

# use a source specific string to detect a type of connection
# Databricks source type
dataSourceName = "Fake Medical Claims 2017" 

# initiate lists

userNameList = []
userNameRoleList = []

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
# adding this to troubleshoot auth errors
print(authResponse)
authToken = authResponse["token"]
# print(authToken)


# pull a datasource ID by it's name
  
dataSourceResponse = requests.get(
  IMMUTA_URL + '/dataSource/name/' + dataSourceName,
  headers={'Authorization': authToken }  
)
  
# swell, now let's get the data source ID
  
dataSource = dataSourceResponse.json()
# print (dataSource)
dataSourceID = dataSource['policyHandler']['dataSourceId']

# need to handle name not found at least

# this is the endpoint that gets the users associated with a datasourceID

dataAccessResponse = requests.get(
  IMMUTA_URL + '/dataSource/' + str(dataSourceID) + '/access',
  headers={'Authorization': authToken }  
)

dataAccess = dataAccessResponse.json()
dataAccessIds = dataAccess['users']

# loop through the users and append to lists

for i in dataAccessIds:
    userName = i['name']
    accessLevel = i['state']
    # append to the lists
    userNameList.append(userName)
    userNameRoleList.append(accessLevel)
    
    
# build and print final data frame

sourceDictionary = {"UserName":userNameList, "AccessLevel":userNameRoleList}

userSummary = pandas.DataFrame(sourceDictionary)

print(userSummary)
    

