#################################
#                               #
#       Approval Workflow       #
#             via API #1        #
#                               #
# Authenticate and Check Access #
#                               #
# By: Mike Dunlap, Immuta CSA   #
# Born On: 10/13/2021           # 
#                               #
#################################

# Purpose
# Display a set of datasources accessible to a given user based on Immuta attributes
#
# Basic instruction

# 1.) Authenticate as current user (or arbitrary user)
# 2.) Returns data frame with user attributes
# 3.) Based on arbitrary value, return datasources that are "read only"

#Install json
import json

#Import requests
import requests

#Import Pandas
import pandas

# set Immuta vars
# Set the hostname (and port if not 443) for the Immuta instance
IMMUTA_URL= "https://<your-Immuta>.immuta.com"
# This is your user API key from Immuta
API_KEY= "<your luggage combo"


# initiate lists

authAttributeList = []
authAttributeValueList = []
dataSourceList = []

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
# print(authToken)
print(authResponse)


# now get my attributes
# assumption: logging in as self, so use this endpoint

userAttributes = requests.get(
    IMMUTA_URL + '/bim/rpc/user/current',
    headers={'Authorization': authToken}
)

currentUserData = userAttributes.json()

# print (currentUserData)

userAuths = currentUserData['authorizations']

# print (userAuths)

# dynamically parse out a 2-level auth structure
for i in userAuths:
    #print(i)
    userAttributes = currentUserData['authorizations'][i]
    for j in userAttributes:
        #print(j)
        authAttributeList.append(i)
        authAttributeValueList.append(j)
        # based on user auth value, what can user request access to?
        # assumption: user auth value = a data tag
        dataSourceCheck = requests.get(
            IMMUTA_URL + '/dataSource?tag=' + j,
            headers={'Authorization': authToken}
        )
        dataSourceCheckData = dataSourceCheck.json()
        accessSources = dataSourceCheckData['hits']
        for k in accessSources:
            #now append to the data source list
            if k['name'] not in dataSourceList:
                dataSourceList.append(k['name'])
            
        
# construct data frame of user auths

authDictionary = {"Attribute":authAttributeList, "Value":authAttributeValueList}

authDF = pandas.DataFrame(authDictionary)

print("These are the user attributes:")
print(authDF)
print("Based on the user attributes, they can see the following:")
print(dataSourceList)
