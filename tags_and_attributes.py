#################################
#                               #
#       Immuta API Examples     #
#        Tags & Attributes      #
#                               #
# By: Mike Dunlap, Immuta CSA   #
# Born On: 10/8/2021            # 
#                               #
#################################

# Purpose
# Sundry useful API calls related to tags and attribute
#
# Basic instruction

# script doesn't fill a business purpose, just examples

#Install json
import json

#Import requests
import requests

#Import Pandas
import pandas

# set Immuta vars
# Set the hostname (and port if not 443) for the Immuta instance
IMMUTA_URL= "https://<my immuta host>.com"
# IMMUTA_URL= "https://mpdprojectdemo7.internal.immuta.io"
# This is your user API key from Immuta first is databrickhouse
API_KEY= "not your luggage code"
# API_KEY= "916d20131ea745fe8eff0796c7c36efb"


# script variables
# a sample data source ID for experimentation
dataSourceID = 92
# the name of a pre-existing tag for experimentation
tagName = "Blue"
# sample project ID
testProject = 46


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


# UC 1: tag datasources in bulk


# you can create a tag via API
# <IMMUTA_URL>/tag

# attach the tag to data source
# you could drive an a bulk update based on tag and linkage to data sourceID

tagDataSource = requests.post(
      IMMUTA_URL + '/tag/datasource/' + str(dataSourceID),
      headers={'Authorization': authToken,
                 'Content-Type': 'application/json' },
      json=
        [
          {
            "name": tagName
          }
        ]
      
    )

print(tagDataSource.json())

# ok verify that you added the tag
getTagResponse = requests.get(
  IMMUTA_URL + '/dataSource/92/tags',
  headers={'Authorization': authToken }  
)

print(getTagResponse.json())

# UC 3: add data sources to a project in bulk
# you could drive automation based on a two column df of projectID + dataSourceId that you want to associate


addDataSource = requests.post(
      IMMUTA_URL + '/project/' + str(testProject) + '/dataSources',
      headers={'Authorization': authToken,
                 'Content-Type': 'application/json' },
      json=
        {
          "dataSourceIds": [
                            testProject
                              ],
          "comment": "string"
        }
      
    )

print(addDataSource.json())



# UC 4: Tag on date fields regardless of name

# you could feed in data Sources to this call
projectResponse = requests.get(
  IMMUTA_URL + '/dictionary/' + str(dataSourceID),
  headers={'Authorization': authToken }  
)

print(projectResponse.json())

# interogate that call for fields that match 'date'

columnLooksLikeDate = 'DOB'


# pass fields matching date type to this call to add tags

tagDataSource = requests.post(
      IMMUTA_URL + '/tag/column/' + str(dataSourceID) + '_' + columnLooksLikeDate,
      headers={'Authorization': authToken,
                 'Content-Type': 'application/json' },
      json=
        [
          {
            "name": tagName
          }
        ]
      
    )

print(tagDataSource.json())

# UC 5: maintain attributes externally outside of an IDP?

# similar approach to above, you could house user attributes externally and pass them in

iamID = 'bim' #this is the Immuta internal ID manager
userID = 'user@example.com'
attribute = 'TestMe'
attributeValue = 'Success'

addAttribute = requests.put(
      IMMUTA_URL + '/bim/iam/'+ iamID + '/user/' + userID + '/authorizations/'+ attribute +'/' + attributeValue,
      headers={'Authorization': authToken,
                 'Content-Type': 'application/json' },
      json=
        {
        }
      
    )

print(addAttribute.json())







