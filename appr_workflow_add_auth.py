#################################
#                               #
#       Approval Workflow       #
#             via API #2        #
#                               #
#      Add Authorization        #
#                               #
# By: Mike Dunlap, Immuta CSA   #
# Born On: 10/13/2021           # 
#                               #
#################################

# Purpose
# This sort of call could be used at the end of a custom approval workflow
# executed outside of Immuta.  User granted attribute that allows access 
# via pre-existing tag
#
# Basic instruction

# 1.) Add a pre-populated attribute to support subscription policy
#

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


# attribute to add

key = 'API'
value = 'Test1'


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


# now add an authorization key value pair

iamID = 'bim' #this is the Immuta internal ID manager
userID = 'magic.johnson@example.com'
attribute = 'Access'
attributeValue = 'SeeMe'

addAttribute = requests.put(
      IMMUTA_URL + '/bim/iam/'+ iamID + '/user/' + userID + '/authorizations/'+ attribute +'/' + attributeValue,
      headers={'Authorization': authToken,
                 'Content-Type': 'application/json' },
      json=
        {
        }
      
    )

print(addAttribute.json())


