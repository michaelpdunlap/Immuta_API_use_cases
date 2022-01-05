#################################
#                               #
#  Immuta Trigger Schema        #
#           Detection           #
#                               #
#                               #
# By: Mike Dunlap, Immuta CSA   #
# Born On: 1/5/2022             # 
#                               #
#################################

# Purpose
# trigger Schema Detection job
#
# Basic instruction
#
# Schema detection must be "on" for the scope you are monitoring
# Can flip to "on" within Schema Project Overview page, "Edit Schema Monitoring"
# Use hostname or DB parameters to limit job scope
# Running without params = running wide open.  Could be impactful to performance

#Install json
import json

#Import requests
import requests

# set Immuta vars
# Set the hostname (and port if not 443) for the Immuta instance
IMMUTA_URL= "https://yourimmuta.com"
# This is your user API key from Immuta first is databrickhouse
API_KEY= "iluvteddybears"

# script variables
yourHost = "1234xxxxx.databricks.com"
yourDB = "customer_success"

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


runSchemaMonitoring = requests.put(
      IMMUTA_URL + '/dataSource/detectRemoteChanges',
      headers={'Authorization': authToken,
                 'Content-Type': 'application/json' },
      json=
        {
            #"hostname": yourHost
            "database": yourDB
        }
      
    )

monitoringResponse = runSchemaMonitoring.json()
print(monitoringResponse)


