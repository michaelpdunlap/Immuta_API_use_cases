#################################
#                               #
#       Immuta API Example:     #
#     Add attribute to user     #
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
# 1.) Enter user and attribute variables
# 2.) Rock and roll
# 3.) You can confirm that the attribute was added via the call below

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
#attribute and user variables
iamID = 'bim' #this is the Immuta internal ID manager
userID = 'magic.johnson@example.com'
attribute = 'TestMe'
attributeValue = 'Success'

# similar approach to above, you could house user attributes externally and pass them in

addAttribute = requests.put(
      IMMUTA_URL + '/bim/iam/'+ iamID + '/user/' + userID + '/authorizations/'+ attribute +'/' + attributeValue,
      headers={'Authorization': authToken,
                 'Content-Type': 'application/json' },
      json=
        {
        }
      
    )

print(addAttribute.json())