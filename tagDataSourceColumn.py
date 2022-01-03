#################################
#                               #
#       Immuta API Example:     #
#     Add tag to data source    #
#          column               #
#                               #
# By: Mike Dunlap, Immuta CSA   #
# Born On: 10/7/2021            # 
# Last Mod: 12/30/2021          # 
#                               #
#################################

# Purpose
# Create a tag and apply to a column
#
# Basic instruction
#
# 1.) Enter a tag description and column string as parameters
# 2.) Enter the datasource ID for the data source you want to tag
# 3.) Rock and roll
# 4.) You can confirm that the tag was added via the call below

#Install json
import json

#Import requests
import requests

#Import Pandas
import pandas

# set Immuta vars
# Set the hostname for the Immuta instance
IMMUTA_URL= "https://<your-immuta>.com/"
# This is your user API key
API_KEY= "1234"
# this is the column you are looking to tag
columnLooksLikeDate = 'DOB'

# script variables
# a sample data source ID for experimentation
dataSourceID = 1
# the name of a pre-existing tag for experimentation
tagName = "Your Tag Here"
# column to look for
columnLooksLikeDate = "Search for this field name"


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

# you can create a tag via API
# <IMMUTA_URL>/tag

createTag = requests.post(
    IMMUTA_URL + '/tag',
    headers={'Authorization': authToken,
                'Content-Type': 'application/json'},
    json=
        {
          "rootTag": 
            {
                "name": tagName
            },
          "tags": [
                    {
                      "name": tagName,
                      "id": 0
                    }
                  ]
            }
        )



# pass fields matching date type to this call to add tags to a column in the DataSourceID

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